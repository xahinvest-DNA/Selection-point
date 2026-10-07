# Decision — repair project synchronization

**ID:** SP-DEC-SYNC-2026-10-07
**Status:** approved operational repair
**Authority:** Owner directive on 7 October 2026: «Устрани все проблемы по рассинхронизации».

## Scope

Synchronize current documents, recovery, technical task status, consistency checking and reminders with decisions already made. The active route is course-first. The course structure remains approved; the lesson template and full questionnaire v0.2 remain drafts. This repair does not approve new methodology, open S5, SP-LAB-002, external pilot or trainer implementation.

## State authority

- `PROJECT_SYSTEM_STATE.yaml`: current work, topology, active working inputs and recovery.
- `docs/FOUNDATION/PROJECT_STATE.yaml`: canonical architecture progress.
- `docs/PRODUCT_LAB/LAB_STATE.yaml`: Product Lab and telemetry.
- `REMINDER_DELIVERY_STATE.yaml`: verified deployment state of reminders, distinct from questionnaire-design approval.

Historical approval and current execution permission are different fields. Gate-era work is reference material; V0 execution remains suspended by the course-first reset. Original decisions/checkpoints retain their historical meaning and receive successor notices where needed.

## Recovery and publication

Read the seven-item bootstrap in system SSOT, then only task-relevant sources. Active working inputs, including the 5 October direction/route/action proposition, must be loaded. Generated current-state blocks must be rendered from the manifests and checked before publication. CI checks all pushes to main and all pull requests.

## Technical and delivery boundaries

The v0.1 store is reported completed; v0.2 is authorized but completion is unverified in core. Do not invent an implementation repository or completed commit. Resolving this supporting task is not a prerequisite for course development.

Correct the deployed evening question to factual end-of-day position. Restore the previously accepted morning/midday Mode B reminders without requiring new data entry. Update the daily drift audit to all three SSOT layers and active course decisions. Deployment verification dates describe tool confirmation, not successful future delivery.

## Historical branches and PR

PR #49 is an earlier alternative Gate B assembly; main already contains a later approved package and the course-first reset. Close the superseded PR without merging it. Preserve the branch and historical commits, including potentially unique examples, for task-specific retrieval. Other old branches are historical, not active authorization; do not delete unreviewed content.
