# TASK — Local Participant Storage v0.1

**Status:** ACTIVE / explicitly authorized by owner on 2026-09-15  
**Scope:** infrastructure only  
**Project:** Selection Point  
**Do not open:** Stage 5, SP-LAB-002, new methodology, app/product scope

## 1. Goal

Implement a local-first private data layer for the current three-person Selection Point health/trajectory micropilot.

The repository may contain code, schemas, validators, documentation and de-identified fixtures only.

**Real participant raw data must never be committed to Git or pushed to GitHub.**

## 2. Storage boundary

Use an external local directory selected by the owner through environment variable:

```text
SP_PRIVATE_DATA_DIR
```

Rules:

- the directory MUST be outside the Git repository;
- if `SP_PRIVATE_DATA_DIR` is absent, write operations MUST fail safely with a clear message;
- never silently fall back to a directory inside the repository;
- never upload, sync or transmit participant raw data;
- do not create cloud integrations;
- do not put participant identity in file names.

Participant IDs:

```text
SPP-001
SPP-002
SPP-003
```

No identity mapping is required in v0.1.

## 3. Local directory layout

Initialize the external directory as:

```text
<SP_PRIVATE_DATA_DIR>/
  README_PRIVATE.txt
  participants/
    SPP-001/
      baseline.yaml
      daily/
    SPP-002/
      baseline.yaml
      daily/
    SPP-003/
      baseline.yaml
      daily/
  derived/
    individual/
    cohort/
  reviews/
    weekly/
    monthly/
  exports/
  audit/
```

`exports/` must remain local. No automatic export is allowed.

## 4. Data contracts

Reuse, do not redefine, the current project contracts where applicable:

- `docs/PRODUCT_LAB/REALITY_EVENT_MODEL_V0_2.md`
- `docs/PRODUCT_LAB/PILOT_METRICS_SPEC_V0_1.md`
- `docs/PRODUCT_LAB/PARTICIPANT_DATA_POLICY_V0_1.md`
- Health Lab schema concepts from the private evidence node, but do not require remote writes.

Create local schemas for:

### Baseline

Minimum fields:

```yaml
participant_id:
source: intake_self_report
consent_status: confirmed
captured_at_date:
body_context:
  age_years:
  height_cm:
  weight_kg:
  weight_change_12m_kg:
  physical_state_self_rating_1_10:
  relevant_constraints: []
recovery:
  typical_sleep_hours:
  typical_sleep_quality_1_5:
nutrition:
  meal_pattern:
  portion_control_current:
  recurring_risk_contexts: []
habits:
  alcohol_frequency:
  alcohol_contexts: []
  other_relevant_habits: []
movement:
  training_current:
  activity_level:
  work_activity_type:
state:
  typical_energy_1_5:
  typical_discomfort_0_10:
  typical_stress_0_10:
trajectory:
  self_reported_current_direction:
  helpful_actions: []
  opposing_actions: []
selection_points:
  recurring_branch_points: []
  typical_self_justifications: []
direction:
  participant_wording:
  observable_signals: []
first_next_day_intention:
  action:
  reason:
notes:
  omitted_or_unasked_context: []
```

Unknown fields must be `null` / `unknown`; never infer missing participant data.

### Daily D1

Support at minimum:

```yaml
date:
participant_id:
source: evening_self_report
prior_intention:
  text:
  result: executed | partially_executed | not_executed | circumstances_changed | unknown
weight_kg:
sleep:
  hours:
  quality_1_5:
nutrition:
  overeating:
  chosen_structure_followed:
alcohol:
  used:
  amount_text:
training:
  performed:
  description:
activity:
  level: low | normal | high | unknown
state:
  energy_1_5:
  physical_discomfort_0_10:
  stress_0_10:
selection_point:
  planned_action:
  immediate_impulse:
  realized_action:
  context_notes:
next_position:
  more_available: []
  less_available: []
next_day_intention:
  action:
  if_then_optional:
free_note:
```

Do not convert self-report into causal claims.

## 5. Required repository code

Implement a small Python CLI under a suitable repository path, for example:

```text
tools/local_participant_store/
```

Required commands:

```text
python -m tools.local_participant_store init
python -m tools.local_participant_store validate
python -m tools.local_participant_store add-baseline <participant_id> <yaml-file>
python -m tools.local_participant_store add-daily <participant_id> <yaml-file>
python -m tools.local_participant_store list-days <participant_id>
python -m tools.local_participant_store weekly-review-input <participant_id>
```

Behavior:

- `init` creates only the external local structure;
- `validate` checks structure, IDs, schemas and accidental repo-local storage;
- `add-baseline` and `add-daily` validate before copying/writing;
- duplicate daily date must not overwrite silently;
- source records are append-only by meaning; correction requires a revision record or explicit overwrite flag with audit entry;
- `weekly-review-input` creates a local derived input bundle without modifying raw files.

## 6. Privacy guardrails

Implement automated checks that fail if:

- `SP_PRIVATE_DATA_DIR` resolves inside repository root;
- a participant raw-data directory appears anywhere under Git root;
- participant raw files are staged/tracked by Git, where detectable;
- the CLI is asked to write without explicit local storage configuration.

Add or strengthen `.gitignore` only for defensive patterns such as:

```text
local_private_data/
participant_data/
.private_data/
```

This is defense-in-depth only; external storage remains mandatory.

Do not commit actual participant baselines or daily records, even as examples. Synthetic fixtures must be clearly marked `synthetic` and contain no copied personal values from the pilot.

## 7. Consent and withdrawal metadata

Local metadata should support:

```yaml
consent:
  status: confirmed | withdrawn
  confirmed_date:
  withdrawn_date:
```

Provide a command or documented procedure to stop future collection and delete that participant's identifiable/local raw directory on owner request.

Do not implement irreversible secure deletion claims. State clearly that normal filesystem deletion does not guarantee forensic erasure.

## 8. Tests

Tests must cover at least:

1. missing `SP_PRIVATE_DATA_DIR`;
2. path inside repo is rejected;
3. valid external path initializes;
4. valid baseline accepted;
5. invalid participant ID rejected;
6. valid D1 accepted;
7. duplicate date protected;
8. unknown/missing optional fields remain unknown rather than inferred;
9. weekly review bundle reads but does not mutate raw records;
10. synthetic fixtures only.

## 9. Documentation

Create a short operator guide:

```text
docs/PRODUCT_LAB/LOCAL_PARTICIPANT_STORAGE_OPERATOR_GUIDE.md
```

It must explain:

- how owner chooses local folder;
- how to set `SP_PRIVATE_DATA_DIR` on Windows PowerShell and cmd;
- initialization;
- adding baseline/D1 data;
- validating storage;
- making a local backup;
- withdrawal/deletion procedure;
- strict rule that raw participant data never enter GitHub.

Do not include real local paths, names or participant values.

## 10. Acceptance criteria

Task is complete only when:

- all tests pass;
- no real participant raw data exists in Git history/worktree;
- no local data path is hardcoded;
- external-directory guard works;
- three participant IDs can be initialized locally;
- baseline and D1 schemas validate;
- duplicate protection works;
- operator guide exists;
- implementation does not alter Foundation canon, Stage status or open SP-LAB-002.

## 11. Final Codex report

Return:

1. files changed;
2. commands added;
3. tests run + result;
4. privacy checks performed;
5. any unresolved issue;
6. exact local bootstrap commands for the owner to run next.
