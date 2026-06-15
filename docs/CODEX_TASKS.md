# CODEX_TASKS

## Working agreement

Codex is the implementation executor. It must not redesign product direction unless the task explicitly asks for architecture feedback.

For every task Codex should:

1. Read `README.md`.
2. Read `docs/CURRENT_STATE.md`.
3. Read `docs/DECISIONS.md`.
4. Read the specific task file.
5. Make the smallest coherent implementation.
6. Run available checks.
7. Report what changed, how to run, and what remains.

## Priority order

### P0 — Foundation

- [ ] TASK-001: Bootstrap mobile app.
- [ ] TASK-002: Create base navigation and placeholder screens.
- [ ] TASK-003: Define TypeScript domain models.

### P1 — First user loop

- [ ] TASK-004: Implement Day 0 diagnosis form.
- [ ] TASK-005: Implement Daily Check-in form.
- [ ] TASK-006: Implement Potential Difference Map form.
- [ ] TASK-007: Implement Mechanism Selection.
- [ ] TASK-008: Implement Inner Task Builder.
- [ ] TASK-009: Implement Feedback Summary screen.

### P2 — Persistence

- [ ] TASK-010: Add local persistence.
- [ ] TASK-011: Add protocol day state.
- [ ] TASK-012: Add previous entries screen.

### P3 — Protocol logic

- [ ] TASK-013: Implement 14-day protocol phases.
- [ ] TASK-014: Generate simple phase summaries.
- [ ] TASK-015: Add repeated trigger detection.

### P4 — Pilot readiness

- [ ] TASK-016: Polish UX copy.
- [ ] TASK-017: Add visual design pass.
- [ ] TASK-018: Add export/share summary.

## Current active task

`codex/TASK-001-bootstrap-mobile-app.md`

## Definition of Done for current phase

Phase 1 is done when:

- app is runnable locally;
- app opens on phone/emulator;
- project has clean TypeScript structure;
- at least Welcome screen exists;
- no backend required;
- README has run instructions.
