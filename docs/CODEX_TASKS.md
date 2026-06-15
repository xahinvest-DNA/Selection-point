# CODEX_TASKS

## Working agreement

Codex is the implementation/content executor. It must not redesign product direction unless the task explicitly asks for architecture feedback.

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

Before building the mobile app, the project must first become a clear educational course.

The course is the source of truth. The app will later become a delivery format for the course and its practices.

Reason:

- the app should not be built as a generic tracker;
- the first product must be teachable without app UI;
- the 5-level development structure must be clear before screen design;
- theory must inspire practice, not overload the user;
- practices must be grounded and concrete;
- content can be manually piloted before code.

## Priority order

### P0 — Course foundation

- [x] TASK-000: Prepare initial theory and practice content foundation under `docs/CONTENT/`.
- [ ] TASK-000B: Rebuild content as a Williams 5-level training course under `docs/COURSE/`.

### P1 — Course review and manual pilot packet

- [ ] TASK-000C: Revise course after Андрей review.
- [ ] TASK-000D: Prepare manual pilot packet from course materials.

### P2 — Mobile foundation, after course review

- [ ] TASK-001: Bootstrap mobile app.
- [ ] TASK-002: Create base navigation and placeholder screens.
- [ ] TASK-003: Define TypeScript domain models.

### P3 — First app user loop

- [ ] TASK-004: Implement Day 0 diagnosis form.
- [ ] TASK-005: Implement Daily Check-in form.
- [ ] TASK-006: Implement Potential Difference Map form.
- [ ] TASK-007: Implement Mechanism Selection.
- [ ] TASK-008: Implement Inner Task Builder.
- [ ] TASK-009: Implement Feedback Summary screen.

### P4 — Persistence

- [ ] TASK-010: Add local persistence.
- [ ] TASK-011: Add protocol day state.
- [ ] TASK-012: Add previous entries screen.

### P5 — Protocol logic

- [ ] TASK-013: Implement app protocol phases.
- [ ] TASK-014: Generate simple phase summaries.
- [ ] TASK-015: Add repeated trigger detection.

### P6 — Pilot readiness

- [ ] TASK-016: Polish UX copy.
- [ ] TASK-017: Add visual design pass.
- [ ] TASK-018: Add export/share summary.

## Current active task

`codex/TASK-000B-course-foundation.md`

## Definition of Done for current phase

P0 course foundation is done when:

- `docs/COURSE/` exists;
- the course is built around the 5 Williams-style development levels;
- Dan Millman and Bill Williams are synthesized clearly;
- the practice conversation material is used mostly as a source of concrete practices;
- each level has theory, practices, homework, reflection and transition criteria;
- a 15-lesson course sequence exists;
- no app code is created yet.
