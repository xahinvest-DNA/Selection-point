# Recovery checkpoint — synchronization repaired

**ID:** SP-RCP-2026-10-07-SYNC
**Date:** 7 October 2026
**Role:** current recovery checkpoint selected by system SSOT.

1. Read `PROJECT_SYSTEM_STATE.yaml` and its `current_work`.
2. The active route is course-first under `DECISION_COURSE_FIRST_RESET_2026-09-20.md`.
3. STRUCT-003 is approved: orientation + five lessons + integration. Read the current structure and its approval decision.
4. TEMPLATE-001 is `draft_for_owner_review`. Next action: owner review/revision of the template; do not mark it approved from the synchronization request.
5. Read the active 5 October direction/route/action working addendum. Keep selected and realized steps distinct; means must not become goals.
6. Gate-era artifacts are reference material. Post-protocol V0 execution is suspended. No Foundation S5, SP-LAB-002, external pilot or trainer implementation opens automatically.
7. Questionnaire telemetry remains separate from the course. The deployed Q9 correction does not approve the whole v0.2 draft. Deployment facts are in `REMINDER_DELIVERY_STATE.yaml`.
8. Technical store v0.2 completion is unverified. This does not block course design.

Foundation: stages 1–4 complete, RC-018 approved, S5 unopened. Historical checkpoints preserve their dates and do not override this recovery entry.

Run `python scripts/render_project_status.py --check`, `python scripts/check_project_consistency.py` and the regression tests after future synchronization changes.
