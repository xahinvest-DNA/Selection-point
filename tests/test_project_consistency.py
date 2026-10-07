"""Regression tests: deliberately reintroduce real drift and require detection."""
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import yaml

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_project_consistency import validate
from project_state import SYSTEM,LAB,load
from render_project_status import render

class DriftDetectionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'repo'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    def change(self,path,fn):
        doc=load(self.root,path)
        fn(doc)
        (self.root/path).write_text(yaml.safe_dump(doc,allow_unicode=True,sort_keys=False))
    def detected(self,text):
        self.assertTrue(any(text in error for error in validate(self.root)),validate(self.root))
    def test_current_repository_passes(self):
        self.assertEqual(validate(self.root),[])
        self.assertEqual(render(self.root,check=True),[])
    def test_stale_projection_is_rejected_and_renderer_repairs_it(self):
        p=self.root/'README.md';p.write_text(p.read_text().replace('owner_review','old_review'))
        # Change a generated value, not a manually maintained paragraph.
        p.write_text(p.read_text().replace('SP-COURSE-S1-STRUCT-003','SP-COURSE-S1-STRUCT-001'))
        self.detected('generated CURRENT view stale')
        render(self.root)
        self.assertEqual(validate(self.root),[])
    def test_bootstrap_cannot_select_old_checkpoint(self):
        self.change(SYSTEM,lambda d:d['new_chat_bootstrap']['read_first'].__setitem__(1,'docs/PROJECT_SYSTEM/RECOVERY_CHECKPOINT_2026-09-20_STAGE1_COURSE_STRUCTURE.md'))
        self.detected('current checkpoint must be second')
    def test_active_working_input_must_be_loaded(self):
        self.change(SYSTEM,lambda d:d['new_chat_bootstrap']['read_first'].pop())
        self.detected('working input missing')
    def test_suspended_v0_cannot_be_reauthorized_silently(self):
        self.change(SYSTEM,lambda d:d['training_state']['stage_1_post_protocol_validation'].__setitem__('v0_execution_authorized',True))
        self.detected('suspended V0 is authorized')
    def test_unapproved_template_cannot_authorize_execution(self):
        self.change(SYSTEM,lambda d:d['current_work'].__setitem__('execution_authorized',True))
        self.detected('unapproved template')
    def test_unknown_local_file_is_rejected(self):
        self.change(SYSTEM,lambda d:d['current_work'].__setitem__('route_decision','docs/MISSING.md'))
        self.detected('missing local file')
    def test_document_status_must_match_manifest(self):
        p=self.root/'docs/COURSE/STAGE_1_LESSON_TEMPLATE.md'
        p.write_text(p.read_text().replace('**Status:** draft_for_owner_review','**Status:** approved'))
        self.detected('current artifact document status differs')
    def test_duplicate_yaml_keys_fail_closed(self):
        p=self.root/SYSTEM;p.write_text(p.read_text()+'\nschema_version: 1\n')
        self.detected('Duplicate YAML key')
    def test_historical_next_action_cannot_leak_into_current_state(self):
        self.change(SYSTEM,lambda d:d['training_state']['stage_1_stage_review'].__setitem__('next_step','run_validation'))
        self.detected('historical next step leaks')
    def test_questionnaire_status_must_agree_across_manifests(self):
        self.change(LAB,lambda d:d['daily_trajectory_questionnaire'].__setitem__('status','approved'))
        self.detected('questionnaire status differs')
    def test_ci_cannot_reintroduce_path_blind_spots(self):
        p=self.root/'.github/workflows/selection-point-consistency.yml'
        p.write_text(p.read_text().replace('  pull_request:\n','  pull_request:\n    paths: [docs/FOUNDATION/**]\n'))
        self.detected('path filter leaves drift blind spots')
    def test_historical_checkpoint_may_keep_old_state(self):
        p=self.root/'docs/PROJECT_SYSTEM/RECOVERY_CHECKPOINT_2026-09-20_STAGE1_COURSE_STRUCTURE.md'
        p.write_text(p.read_text()+'\nHistorical: Gate B; SP-OPS-001; CAP-001.\n')
        self.assertEqual(validate(self.root),[])
    def test_reminder_does_not_reintroduce_inferred_availability(self):
        self.change('docs/PROJECT_SYSTEM/REMINDER_DELIVERY_STATE.yaml',lambda d:d['evening'].__setitem__('q9','Что стало доступнее?'))
        self.detected('Q9 reintroduces')
    def test_consistency_does_not_freeze_work_at_template_review(self):
        # A later owner-approved transition can select a new artifact without changing the checker.
        template=self.root/'docs/COURSE/STAGE_1_LESSON_TEMPLATE.md'
        template.write_text(template.read_text().replace('**Status:** draft_for_owner_review','**Status:** approved'))
        next_path='docs/COURSE/TEST_NEXT_LESSON.md'
        (self.root/next_path).write_text('# Next lesson\n\n**Status:** draft\n')
        def advance(d):
            d['course_first_reset']['stage_1_course']['lesson_template_status']='approved'
            d['course_first_reset']['next_step']='write_first_lesson'
            d['current_work'].update(artifact=next_path,artifact_status='draft',next_step='write_first_lesson',next_step_label='Write first lesson',owner_decision_required=False,execution_authorized=True)
            d['new_chat_bootstrap']['read_first'].append(next_path)
        self.change(SYSTEM,advance)
        render(self.root)
        self.assertEqual(validate(self.root),[])
    def test_raw_data_boundary_cannot_be_weakened(self):
        self.change(LAB,lambda d:d['measurement_foundation'].__setitem__('raw_participant_data_in_public_repo_allowed',True))
        self.detected('raw-data publication boundary weakened')

if __name__=='__main__':unittest.main()
