# TASK-000 — Theory and practice content foundation

## Role

You are Codex, acting as a structured content implementer for Selection Point.

This is a pre-app task. Do not create mobile app code, Expo files, React Native screens, TypeScript domain models, package files, or runtime implementation.

The current project decision is: before building the app, prepare the complete theoretical and practice content foundation step by step.

## Read first

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/PRODUCT_BRIEF.md`
4. `docs/METHOD_CORE.md`
5. `docs/PRACTICE_SYSTEM.md`
6. `docs/DECISIONS.md`
7. `docs/ROADMAP.md`
8. `docs/CODEX_TASKS.md`

## Goal

Create a complete first version of the theoretical and practical content base for Selection Point.

This content will later become:

- onboarding explanations;
- lesson blocks;
- practice instructions;
- daily protocol texts;
- screen copy;
- audio practice scripts;
- app prompts;
- pilot materials.

## Product direction

Selection Point is not a diet app, meditation app, habit tracker, or motivational system.

It is a transformation system built around the choice point between automatic reaction and conscious/natural next action.

The first applied entry point is:

```txt
healthy energetic body + life
```

The user-facing language should be practical and grounded:

- body;
- energy;
- food impulses;
- evening overeating;
- sleep;
- movement;
- avoided tasks;
- pause;
- one inner task;
- one small next action;
- feedback without shame.

Do not lead with advanced nondual/philosophical language. Advanced material may be included only as an optional later appendix.

## Required output structure

Create the following folder and files:

```txt
docs/CONTENT/
  00_INDEX.md
  01_METHOD_OVERVIEW.md
  02_CORE_CONCEPTS.md
  03_BLOCK_SEQUENCE.md
  04_PRACTICE_LIBRARY.md
  05_14_DAY_PROTOCOL.md
  06_DAILY_PROMPTS.md
  07_AUDIO_SCRIPTS.md
  08_SCREEN_COPY_DRAFT.md
  09_GLOSSARY.md
  10_BOUNDARIES_AND_TONE.md
  11_PILOT_NOTES.md
```

## Content requirements

All content should be written in Russian.

Use clear, grounded language. Avoid mystical, grandiose, medical, or manipulative claims.

The tone should be:

- calm;
- precise;
- human;
- non-judgmental;
- practical;
- without shame;
- without motivational noise.

## Required conceptual blocks

`03_BLOCK_SEQUENCE.md` must define the learning/practice path step by step from the beginning.

Minimum blocks:

1. Entry: why this is not a diet and not self-improvement by force.
2. Point A: current fact without interpretation.
3. Fact vs story: what happened vs what the mind added.
4. Automatic pattern: repeated program, impulse, avoidance, craving, resistance.
5. Pause: how to create a gap before action.
6. Body/environment expansion: breath + body contact + sounds + urge/tension.
7. Point B: flexible direction, not rigid goal.
8. Potential difference: gap between current state and useful direction.
9. Second knot: extra pressure from “I must / I failed / I am weak”.
10. Inner task: one trainable transition, not the whole life at once.
11. Impulse vs automatic reaction: compression vs expansion, push vs invitation.
12. Small action: one movement, not the whole task.
13. Feedback: reality gives data, not judgment.
14. Repetition: building the new sensitivity through short cycles.
15. Optional advanced layer: direct pointing and current moment visibility, only after grounding.

For each block include:

- purpose;
- short explanation;
- user-facing text draft;
- practice;
- example for body/food/energy;
- example for life/household/task avoidance;
- common misunderstanding;
- transition to the next block.

## Practice library requirements

`04_PRACTICE_LIBRARY.md` must include complete practice instructions for:

1. Fact without story.
2. 30-second urge pause.
3. Body/environment expansion.
4. Evening overeating pause.
5. Avoidance/laziness micro-step.
6. Morning 2-minute direction.
7. Evening 2-minute review.
8. Point A / Point B map.
9. Potential difference map.
10. Second knot detection.
11. Inner task formulation.
12. Impulse vs automatic check.
13. One visible movement.
14. Feedback without shame.
15. Short direct pointing practice, marked as optional advanced.
16. Extended direct pointing practice, marked as optional advanced.

For each practice include:

- when to use;
- duration;
- step-by-step script;
- what to record;
- marker: + / 0 / -;
- grounding exit if the user feels strange, empty, tense, or disoriented.

## 14-day protocol requirements

`05_14_DAY_PROTOCOL.md` must define the full first protocol:

- Day 0: diagnosis and baseline.
- Days 1–3: observation without fixing.
- Days 4–7: one main mechanism.
- Days 8–11: system instead of willpower.
- Days 12–14: feedback, next inner task, continuation.

For each day include:

- day purpose;
- short explanation;
- user prompt;
- daily practice;
- check-in fields;
- example answer;
- what the app should not say.

## Screen copy requirements

`08_SCREEN_COPY_DRAFT.md` must draft copy for future app screens:

1. Welcome.
2. Day 0 Diagnosis / Point A.
3. Daily Check-in.
4. Point B / Direction.
5. Potential Difference.
6. Mechanism Selection.
7. Inner Task Builder.
8. Practice screen.
9. Feedback Summary.
10. Previous entries / journal.
11. Protocol progress.

For each screen include:

- title;
- subtitle;
- body copy;
- primary CTA;
- secondary CTA if useful;
- empty state;
- one warning about what not to say.

## Boundaries and tone requirements

`10_BOUNDARIES_AND_TONE.md` must define product boundaries using neutral wording.

Include:

- not a medical service;
- not addiction treatment;
- not eating disorder treatment;
- not psychotherapy;
- not guaranteed weight loss;
- advanced attention practices are optional and must be grounded;
- avoid shame, pressure, superiority, spiritual promises, extreme restriction and “fix yourself” language.

## Pilot notes requirements

`11_PILOT_NOTES.md` must define how to test the content before app development.

Include:

- manual 14-day pilot format;
- how to send daily prompts manually;
- what to collect from users;
- completion criteria;
- learning questions;
- signs that the content is unclear;
- signs that the method works.

## Acceptance criteria

The task is complete when:

- all required files exist under `docs/CONTENT/`;
- content is written in Russian;
- content follows `docs/METHOD_CORE.md` and `docs/PRACTICE_SYSTEM.md`;
- no app code is created;
- no package/runtime files are created;
- no backend, auth, payments, database or UI implementation is added;
- materials are detailed enough to later build the app screens and the 14-day protocol.

## Report back

When done, report:

1. Files created.
2. The final content structure.
3. Any unclear points or product decisions needed.
4. Which content should be reviewed by Андрей first.
5. Suggested next task after content review.
