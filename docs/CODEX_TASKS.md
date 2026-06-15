# CODEX_TASKS

## Working agreement

Codex is the implementation executor. It must not redesign product direction unless the task explicitly asks for architecture feedback.

For every task Codex should:

1. Read `README.md`.
2. Read `docs/CURRENT_STATE.md`.
3. Read `docs/PRODUCT_BRIEF.md`.
4. Read `docs/METHOD_CORE.md`.
5. Read `docs/PRACTICE_SYSTEM.md` when the task touches practices or content.
6. Read `docs/DECISIONS.md`.
7. Read the specific task file.
8. Make the smallest coherent implementation.
9. Run available checks when relevant.
10. Report what changed and what remains.

## Current strategic sequence

Before building the mobile app, the project must first prepare the complete theoretical and practical content foundation.

Reason:

- the app should not be built as a generic tracker;
- all screens must later follow the method;
- copy, practices, explanations and protocol logic must be coherent before UI implementation;
- content can be manually piloted before code.

## Priority order

### P0 — Theory and practice foundation

- [ ] TASK-000: Prepare theory and practice content foundation.

### P1 — Mobile foundation, after content review

- [ ] TASK-001: Bootstrap mobile app.
- [ ] TASK-002: Create base navigation and placeholder screens.
- [ ] TASK-003: Define TypeScript domain models.

### P2 — First user loop

- [ ] TASK-004: Implement Day 0 diagnosis form.
- [ ] TASK-005: Implement Daily Check-in form.
- [ ] TASK-006: Implement Potential Difference Map form.
- [ ] TASK-007: Implement Mechanism Selection.
- [ ] TASK-008: Implement Inner Task Builder.
- [ ] TASK-009: Implement Feedback Summary screen.

### P3 — Persistence

- [ ] TASK-010: Add local persistence.
- [ ] TASK-011: Add protocol day state.
- [ ] TASK-012: Add previous entries screen.

### P4 — Protocol logic

- [ ] TASK-013: Implement 14-day protocol phases.
- [ ] TASK-014: Generate simple phase summaries.
- [ ] TASK-015: Add repeated trigger detection.

### P5 — Pilot readiness

- [ ] TASK-016: Polish UX copy.
- [ ] TASK-017: Add visual design pass.
- [ ] TASK-018: Add export/share summary.

## Current active task

`codex/TASK-000-theory-content-foundation.md`

## Definition of Done for current phase

P0 is done when:

- `docs/CONTENT/` exists;
- theoretical blocks are written step by step;
- explanations, practices, 14-day protocol, daily prompts, audio scripts and screen copy drafts exist;
- content is in Russian;
- content can be reviewed before app development;
- no app code is created yet.
