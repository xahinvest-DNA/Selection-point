#!/usr/bin/env python3
"""Fail closed when Selection Point active state drifts from the environment-first contract."""
from pathlib import Path
import sys
import yaml

from project_state import (
    ROOT,
    SYSTEM,
    FOUNDATION,
    LAB,
    load,
    managed_views,
    metadata,
    replace_block,
)


def _walk(value):
    if isinstance(value, dict):
        for v in value.values():
            yield from _walk(v)
    elif isinstance(value, list):
        for v in value:
            yield from _walk(v)
    else:
        yield value


def _add(errors, condition, text):
    if condition:
        errors.append(text)


def validate(root=ROOT):
    errors = []
    try:
        s = load(root, SYSTEM)
        f = load(root, FOUNDATION)
        lab = load(root, LAB)
    except Exception as exc:
        return [str(exc)]

    # All local document pointers in active manifests must resolve.
    for manifest_name, manifest in ((SYSTEM, s), (LAB, lab)):
        for value in _walk(manifest):
            if isinstance(value, str) and value.startswith('docs/'):
                if not (root / value).exists():
                    errors.append(f'missing local file referenced by {manifest_name}: {value}')

    w = s.get('current_work', {})
    env = s.get('environment_first_reset', {})
    course = s.get('course_first_reset', {})
    gates = s.get('current_gates', {})
    bootstrap = s.get('new_chat_bootstrap', {}).get('read_first', [])

    _add(errors, s.get('schema_version') != 6, 'system schema must be environment-first schema v6')
    _add(errors, s.get('updated_at') != '2026-11-03', 'system synchronization date differs from environment-first reset')
    _add(errors, w.get('route') != 'stage_1_environment_first_development', 'active route is not environment-first')
    _add(errors, w.get('objective') != env.get('active_objective'), 'current objective differs from environment reset objective')
    _add(errors, w.get('artifact') != env.get('active_architecture'), 'current artifact differs from environment architecture')
    _add(errors, w.get('artifact_status') != env.get('active_architecture_status'), 'current artifact status differs from environment manifest')
    _add(errors, s.get('operating_model', {}).get('current_authorization') != w.get('route'), 'operating authorization differs from active route')

    # Active artifact metadata must agree with the manifest.
    artifact = w.get('artifact')
    if artifact and (root / artifact).exists():
        _add(
            errors,
            metadata(root, artifact, 'Status') != w.get('artifact_status'),
            'current artifact document status differs from manifest',
        )

    # Recovery/bootstrap must start from the current state, not an older course checkpoint.
    checkpoint = env.get('recovery_checkpoint')
    _add(errors, len(bootstrap) < 2 or bootstrap[0] != SYSTEM, 'project state must be first bootstrap document')
    _add(errors, len(bootstrap) < 2 or bootstrap[1] != checkpoint, 'current checkpoint must be second bootstrap document')
    for required in (
        env.get('decision'),
        env.get('active_architecture'),
        env.get('product_thesis'),
        env.get('evidence_source'),
    ):
        if required:
            _add(errors, required not in bootstrap, f'active environment document missing from bootstrap: {required}')
    for item in s.get('active_working_inputs', []):
        document = item.get('document')
        _add(errors, document not in bootstrap, f'working input missing from bootstrap: {document}')

    # Superseded course route may remain as history but may not silently regain execution authority.
    _add(errors, course.get('status') != 'superseded_as_active_route', 'course-first route is not marked superseded')
    _add(errors, course.get('superseded_by') != env.get('decision'), 'course-first route is not superseded by current decision')
    _add(errors, course.get('execution_authorized') is not False, 'superseded course execution is authorized')

    # Design is open; implementation/pilot/Foundation progression remain closed.
    _add(errors, w.get('design_execution_authorized') is not True, 'environment design is not authorized')
    _add(errors, w.get('software_implementation_authorized') is not False, 'software implementation opened without owner decision')
    _add(errors, w.get('external_pilot_authorized') is not False, 'external pilot opened without owner decision')
    for key in ('foundation_stage_5', 'product_lab_002', 'environment_v0_software_implementation', 'external_user_pilot'):
        _add(errors, gates.get(key) != 'unopened', f'closed gate changed without explicit owner decision: {key}')
    _add(errors, s.get('foundation_state', {}).get('stage_5_status') != 'unopened', 'Foundation Stage 5 opened silently')
    _add(errors, s.get('foundation_state', {}).get('canon_changed_by_environment_reset') is not False, 'environment reset silently changes Foundation canon')

    # V0 anti-expansion boundary.
    v0 = env.get('v0', {})
    _add(errors, v0.get('target_capabilities') != 1, 'V0 expanded beyond one target capability')
    _add(errors, v0.get('scenario_count_min') != 10 or v0.get('scenario_count_max') != 15, 'V0 scenario boundary drifted from 10–15')
    _add(errors, v0.get('real_world_transfer_experiments') != 1, 'V0 transfer experiment boundary changed')
    for key in ('vr_required', 'ai_required', 'platform_required', 'scoring_required'):
        _add(errors, v0.get(key) is not False, f'V0 reintroduced a non-required technology: {key}')

    # Scientific and methodological boundaries.
    science = env.get('scientific_boundaries', {})
    _add(errors, science.get('simulation_equals_reality') is not False, 'simulation/reality equivalence claim reintroduced')
    _add(errors, science.get('simulator_success_proves_transfer') is not False, 'simulator success is treated as transfer proof')
    _add(errors, science.get('real_world_transfer_must_be_observed') is not True, 'real-world transfer observation boundary weakened')
    product = env.get('product_boundaries', {})
    _add(errors, product.get('hidden_correct_answer_target') is not False, 'hidden correct-answer training target reintroduced')
    _add(errors, product.get('selected_is_realized') is not False, 'selected continuation collapsed into realized continuation')
    _add(errors, product.get('theory_is_primary_mechanism') is not False, 'theory restored as primary product mechanism')

    # Product Lab must describe the same active route and preserve data/evidence boundaries.
    _add(errors, lab.get('owner_decision', {}).get('decision') != env.get('decision'), 'Product Lab owner decision differs from project state')
    _add(errors, lab.get('active_architecture', {}).get('document') != env.get('active_architecture'), 'Product Lab architecture differs from project state')
    _add(errors, lab.get('active_product_thesis', {}).get('document') != env.get('product_thesis'), 'Product Lab thesis differs from project state')
    _add(errors, lab.get('v0_scope', {}).get('external_pilot_authorized') is not False, 'Product Lab external pilot opened')
    _add(errors, lab.get('measurement_foundation', {}).get('raw_participant_data_in_public_repo_allowed') is not False, 'raw-data publication boundary weakened')
    _add(errors, lab.get('measurement_foundation', {}).get('simulator_success_proves_transfer') is not False, 'Lab treats simulator performance as transfer proof')
    _add(errors, lab.get('scientific_boundaries', {}).get('brain_does_not_distinguish_simulation_and_reality_claim_accepted') is not False, 'Lab reintroduced brain simulation/reality equivalence claim')

    # Questionnaire status is mirrored by the system state.
    q_lab = lab.get('daily_trajectory_questionnaire', {})
    q_sys = s.get('measurement_state', {})
    _add(errors, q_lab.get('id') != q_sys.get('questionnaire_id') or q_lab.get('status') != q_sys.get('questionnaire_status'), 'questionnaire status differs across manifests')

    # Preserve the last approved Foundation point without requiring this product decision to rewrite canon.
    try:
        foundation_status = f.get('status', {})
        if isinstance(foundation_status, dict) and foundation_status.get('last_approved'):
            _add(errors, foundation_status.get('last_approved') != s.get('foundation_state', {}).get('last_approved_point'), 'Foundation last-approved point differs across manifests')
    except Exception as exc:
        errors.append(f'Foundation status check failed: {exc}')

    # Generated CURRENT projections must be exact.
    try:
        for path, name, body in managed_views(root):
            p = root / path
            old = p.read_text(encoding='utf-8')
            expected = replace_block(old, name, body)
            if old != expected:
                errors.append(f'generated CURRENT view stale: {path}')
    except Exception as exc:
        errors.append(f'generated view check failed: {exc}')

    # CI must run on all relevant changes; path filters create blind spots.
    workflow = root / '.github/workflows/selection-point-consistency.yml'
    if workflow.exists():
        text = workflow.read_text(encoding='utf-8')
        if 'paths:' in text or 'paths-ignore:' in text:
            errors.append('path filter leaves drift blind spots')

    return errors


def main():
    errors = validate(ROOT)
    if errors:
        for error in errors:
            print(f'ERROR: {error}')
        return 1
    print('Selection Point project consistency: OK')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
