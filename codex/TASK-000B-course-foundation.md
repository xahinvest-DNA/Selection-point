# TASK-000B — Rebuild content as a Williams 5-level training course

## Role

You are Codex, acting as a structured course architect and content implementer for Selection Point.

This is still a pre-app task. Do not create mobile app code, Expo files, React Native screens, TypeScript files, package files, backend, database, auth or payment implementation.

## Why this task exists

TASK-000 created a broad app-oriented content foundation under `docs/CONTENT/`.

That material is useful, but the project must return to the original simplicity and clarity:

- the core structure is the **5-stage development model inspired by Bill Williams**;
- the course must start from the beginning and lead a person step by step from novice to expert;
- Dan Millman and Bill Williams are the main conceptual sources;
- file `4.txt` / the deep practice conversation may provide philosophy, but its primary value is concrete practices;
- the product should first exist as an educational course, not app copy;
- only after the course logic is clear should the app be designed.

## Read first

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/PRODUCT_BRIEF.md`
4. `docs/METHOD_CORE.md`
5. `docs/PRACTICE_SYSTEM.md`
6. `docs/DECISIONS.md`
7. `docs/CONTENT/00_INDEX.md`
8. `docs/CONTENT/01_METHOD_OVERVIEW.md`
9. `docs/CONTENT/03_BLOCK_SEQUENCE.md`
10. `docs/CONTENT/04_PRACTICE_LIBRARY.md`
11. `docs/CONTENT/05_14_DAY_PROTOCOL.md`

Use existing `docs/CONTENT/` as draft material, not as final structure.

## Goal

Create the first clear version of Selection Point as an educational course.

The course should give enough theory to ignite interest and enough practice to create immediate lived feedback.

It should be simple, strong and teachable.

## Course center

The backbone must be the 5 development levels:

1. **Новичок** — lives inside automatic reactions and external solutions.
2. **Продвинутый новичок** — understands ideas but cannot apply them under pressure.
3. **Компетентный практик** — builds structure, observation and repeatable practice.
4. **Опытный практик** — sees patterns across domains and acts with less inner violence.
5. **Эксперт** — acts from clarity, natural impulse and feedback without identity drama.

Do not use 15 equal blocks as the main structure. Smaller concepts may live inside these 5 levels.

## Required output structure

Create a new course folder:

```txt
docs/COURSE/
  00_COURSE_INDEX.md
  01_COURSE_POSITIONING.md
  02_SOURCE_SYNTHESIS.md
  03_FIVE_LEVEL_MODEL.md
  04_LEVEL_1_NOVICE.md
  05_LEVEL_2_ADVANCED_BEGINNER.md
  06_LEVEL_3_COMPETENT_PRACTITIONER.md
  07_LEVEL_4_EXPERIENCED_PRACTITIONER.md
  08_LEVEL_5_EXPERT.md
  09_PRACTICE_PROGRESSION.md
  10_LESSON_SEQUENCE.md
  11_STUDENT_WORKBOOK.md
  12_AUDIO_AND_MICRO_PRACTICES.md
  13_TEACHER_NOTES.md
  14_APP_TRANSLATION_NOTES.md
```

All content must be in Russian.

## Course positioning

The course should not be positioned as:

- a diet;
- a motivational challenge;
- a meditation course;
- therapy;
- medical treatment;
- addiction treatment;
- spirituality or enlightenment training.

The first practical field remains:

```txt
healthy energetic body + life
```

But the deeper learning is universal:

```txt
how to notice automatic reactions and develop the ability to choose the next action from reality, not from inner noise
```

## Source synthesis requirements

`02_SOURCE_SYNTHESIS.md` must explain the sources clearly:

### Dan Millman contribution

- present moment;
- body as entry point;
- simple action;
- not making achievement a condition for life;
- freedom from the noise of the mind;
- peaceful warrior as a person who stops fighting reality.

### Bill Williams contribution

- market/life as nonlinear chaos;
- trader/person does not see reality directly, but through inner structure;
- belief systems shape perception;
- development through levels;
- feedback from reality;
- wanting what the market/reality wants instead of forcing reality to confirm desire.

### File 4 / practice conversation contribution

Use carefully:

- do not lead with deep metaphysics;
- extract concrete practices: distinction, pause, expansion, direct prompt, impulse vs automatic reaction, small movement;
- keep advanced direct pointing optional;
- translate into grounded language.

## Five-level file requirements

Each level file must include:

1. Level name.
2. Human condition at this level.
3. Main illusion.
4. Main pain.
5. What the person believes they need.
6. What they actually need to train.
7. Theory that should ignite the student.
8. Key concepts introduced at this level.
9. Core practices for this level.
10. Body/food/energy examples.
11. Life/house/task avoidance examples.
12. Typical mistakes.
13. Criteria for moving to the next level.
14. Short lesson script.
15. Practice homework.
16. Reflection questions.

## Required course logic

The course must start from simplicity.

Suggested learning arc:

### Level 1 — Новичок

Core movement:

```txt
I am not my first reaction.
```

Teach:

- fact vs story;
- automatic reaction;
- body as first checkpoint;
- 30-second pause;
- no shame, only data.

### Level 2 — Продвинутый новичок

Core movement:

```txt
Understanding is not transformation.
```

Teach:

- why knowledge does not change behaviour;
- repeated mechanisms;
- second knot: “I must / I failed / I am weak”;
- observation under pressure;
- simple daily tracking.

### Level 3 — Компетентный практик

Core movement:

```txt
One trainable transition, not the whole life.
```

Teach:

- Point A;
- Point B as direction;
- potential difference;
- inner task;
- practice cycles;
- feedback without judgment.

### Level 4 — Опытный практик

Core movement:

```txt
The same structure repeats in every area.
```

Teach:

- pattern recognition across body, food, tasks, money, relationships;
- impulse vs automatic program;
- compression vs expansion;
- small movement;
- trust after pause.

### Level 5 — Эксперт

Core movement:

```txt
Action without inner violence.
```

Teach:

- natural action;
- flexible Point B;
- direction without rigidity;
- advanced optional pause prompts;
- ordinary life as practice;
- how not to turn the method into a new identity.

## Practice progression requirements

`09_PRACTICE_PROGRESSION.md` must map practices to levels.

Example:

- Level 1: fact/story, 30-second pause, body check.
- Level 2: mechanism log, second knot detection, evening review.
- Level 3: Point A/B map, inner task builder, feedback cycle.
- Level 4: impulse vs program, one visible movement, cross-domain pattern map.
- Level 5: natural action, flexible direction, direct prompt, ordinary life practice.

## Lesson sequence requirements

`10_LESSON_SEQUENCE.md` must convert the course into a teachable sequence.

Create a first version with:

- 5 modules;
- 3 lessons per module;
- each lesson: title, promise, theory, practice, homework, completion criterion.

Total: 15 lessons.

This replaces the previous 15-block app learning path.

## Student workbook requirements

`11_STUDENT_WORKBOOK.md` must include worksheets:

- fact/story worksheet;
- automatic reaction map;
- second knot worksheet;
- Point A / Point B worksheet;
- inner task worksheet;
- practice log;
- feedback review;
- 5-level self-diagnosis;
- level transition checklist.

## Audio and micro practice requirements

`12_AUDIO_AND_MICRO_PRACTICES.md` must include scripts grounded in the course, not abstract spirituality:

- 2-minute body check;
- 30-second pause before impulse;
- 3-minute evening overeating pause;
- 3-minute avoidance/laziness micro-action;
- 5-minute fact/story reset;
- optional advanced direct prompt short version.

The advanced prompt must be marked as optional and not necessary for course completion.

## Teacher notes requirements

`13_TEACHER_NOTES.md` must explain how to teach this course manually:

- what to emphasize;
- what not to overexplain;
- how to keep simplicity;
- how to prevent intellectualization;
- how to bring students back to practice;
- how to work with students who want deep philosophy too early;
- what counts as real progress.

## App translation notes

`14_APP_TRANSLATION_NOTES.md` must explain what later goes into the app:

- onboarding;
- lesson cards;
- practice screens;
- daily prompts;
- progress by level;
- course-first architecture;
- what from `docs/CONTENT/` can be reused;
- what should be discarded or rewritten.

## Rewrite guidance

Do not delete existing `docs/CONTENT/` files.

Treat them as raw materials.

The new `docs/COURSE/` is the new primary structure.

Prefer clarity over completeness.

If a concept does not help the student move from theory to practice, reduce it or move it to teacher notes.

## Acceptance criteria

The task is complete when:

- all required files exist under `docs/COURSE/`;
- course is built around the 5-level model;
- each level is clear enough to teach as a module;
- theory is motivating but not bloated;
- practices are concrete;
- app is not implemented;
- course can be reviewed before any further app work.

## Report back

When done, report:

1. Files created.
2. Final course structure.
3. How the 5 levels are expressed.
4. What material from `docs/CONTENT/` was reused.
5. What became simpler compared with TASK-000.
6. Which file Андрей should review first.
