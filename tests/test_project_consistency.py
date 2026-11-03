"""Regression tests: deliberately reintroduce real drift and require detection."""
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from check_project_consistency import validate
from project_state import SYSTEM, LAB, load
from render_project_status import render


class DriftDetectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def change(self, path, fn):
        doc = load(self.root, path)
        fn(doc)
        (self.root / path).write_text(
            yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding='utf-8'
        )

    def detected(self, text):
        errors = validate(self.root)
        self.assertTrue(any(text in error for error in errors), errors)

    def test_current_repository_passes(self):
        self.assertEqual(validate(self.root), [])
        self.assertEqual(render(self.root, check=True), [])

    def test_stale_projection_is_rejected_and_renderer_repairs_it(self):
        p = self.root / 'README.md'
        p.write_text(p.read_text(encoding='utf-8').replace('10–15 сценариев', '20 сценариев'), encoding='utf-8')
        self.detected('generated CURRENT view stale')
        render(self.root)
        self.assertEqual(validate(self.root), [])

    def test_bootstrap_cannot_select_old_checkpoint(self):
        self.change(
            SYSTEM,
            lambda d: d['new_chat_bootstrap']['read_first'].__setitem__(
                1, 'docs/PROJECT_SYSTEM/RECOVERY_CHECKPOINT_2026-09-20_STAGE1_COURSE_STRUCTURE.md'
            ),
        )
        self.detected('current checkpoint must be second')

    def test_active_working_input_must_be_loaded(self):
        self.change(
            SYSTEM,
            lambda d: d['new_chat_bootstrap']['read_first'].remove(
                d['active_working_inputs'][0]['document']
            ),
        )
        self.detected('working input missing')

    def test_course_first_cannot_be_reauthorized_silently(self):
        self.change(SYSTEM, lambda d: d['course_first_reset'].__setitem__('execution_authorized', True))
        self.detected('superseded course execution is authorized')

    def test_software_implementation_cannot_open_silently(self):
        self.change(SYSTEM, lambda d: d['current_work'].__setitem__('software_implementation_authorized', True))
        self.detected('software implementation opened')

    def test_external_pilot_cannot_open_silently(self):
        self.change(SYSTEM, lambda d: d['current_work'].__setitem__('external_pilot_authorized', True))
        self.detected('external pilot opened')

    def test_unknown_local_file_is_rejected(self):
        self.change(SYSTEM, lambda d: d['current_work'].__setitem__('route_decision', 'docs/MISSING.md'))
        self.detected('missing local file')

    def test_document_status_must_match_manifest(self):
        state = load(self.root, SYSTEM)
        p = self.root / state['current_work']['artifact']
        current = state['current_work']['artifact_status']
        p.write_text(
            p.read_text(encoding='utf-8').replace(
                f'**Status:** {current}', '**Status:** deliberately_wrong_status', 1
            ),
            encoding='utf-8',
        )
        self.detected('current artifact document status differs')

    def test_duplicate_yaml_keys_fail_closed(self):
        p = self.root / SYSTEM
        p.write_text(p.read_text(encoding='utf-8') + '\nschema_version: 1\n', encoding='utf-8')
        self.detected('Duplicate YAML key')

    def test_simulation_cannot_be_equated_with_reality(self):
        self.change(
            SYSTEM,
            lambda d: d['environment_first_reset']['scientific_boundaries'].__setitem__(
                'simulation_equals_reality', True
            ),
        )
        self.detected('simulation/reality equivalence claim reintroduced')

    def test_simulator_success_cannot_prove_transfer(self):
        self.change(
            LAB,
            lambda d: d['measurement_foundation'].__setitem__(
                'simulator_success_proves_transfer', True
            ),
        )
        self.detected('Lab treats simulator performance as transfer proof')

    def test_v0_cannot_expand_capability_count_silently(self):
        self.change(
            SYSTEM,
            lambda d: d['environment_first_reset']['v0'].__setitem__('target_capabilities', 2),
        )
        self.detected('V0 expanded beyond one target capability')

    def test_v0_cannot_make_vr_required_silently(self):
        self.change(
            SYSTEM,
            lambda d: d['environment_first_reset']['v0'].__setitem__('vr_required', True),
        )
        self.detected('V0 reintroduced a non-required technology')

    def test_questionnaire_status_must_agree_across_manifests(self):
        self.change(LAB, lambda d: d['daily_trajectory_questionnaire'].__setitem__('status', 'approved'))
        self.detected('questionnaire status differs across manifests')

    def test_raw_data_boundary_cannot_be_weakened(self):
        self.change(
            LAB,
            lambda d: d['measurement_foundation'].__setitem__(
                'raw_participant_data_in_public_repo_allowed', True
            ),
        )
        self.detected('raw-data publication boundary weakened')

    def test_ci_cannot_reintroduce_path_blind_spots(self):
        p = self.root / '.github/workflows/selection-point-consistency.yml'
        p.write_text(
            p.read_text(encoding='utf-8').replace(
                '  pull_request:\n', '  pull_request:\n    paths: [docs/FOUNDATION/**]\n'
            ),
            encoding='utf-8',
        )
        self.detected('path filter leaves drift blind spots')

    def test_historical_checkpoint_may_keep_old_course_state(self):
        p = self.root / 'docs/PROJECT_SYSTEM/RECOVERY_CHECKPOINT_2026-09-20_STAGE1_COURSE_STRUCTURE.md'
        p.write_text(
            p.read_text(encoding='utf-8') + '\nHistorical: course-first state retained as history.\n',
            encoding='utf-8',
        )
        self.assertEqual(validate(self.root), [])


if __name__ == '__main__':
    unittest.main()
