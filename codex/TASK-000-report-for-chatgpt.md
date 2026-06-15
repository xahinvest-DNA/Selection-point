# TASK-000 report for ChatGPT

## Status

TASK-000 is completed.

The theoretical and practical content foundation has been created under `docs/CONTENT/`.

No app/runtime implementation was created:

- no Expo project;
- no React Native files;
- no TypeScript app/domain files;
- no `package.json`;
- no backend;
- no auth;
- no payments;
- no database.

## Files created

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

## What was prepared

The content foundation now includes:

- a Russian-language overview of the Selection Point method;
- core concepts: point A, point B, fact/story, potential difference, automatic mechanism, second knot, inner task, impulse, feedback;
- a 15-block learning/practice sequence;
- a 16-practice library with scripts, markers and grounding exits;
- the full 14-day "Тело без войны" protocol;
- daily morning/evening messages for manual pilot;
- audio scripts for short and extended practices;
- draft copy for future app screens;
- glossary and user-facing translations;
- boundaries and tone rules;
- manual 14-day pilot notes.

## Main implementation choices

The content follows `docs/METHOD_CORE.md` and `docs/PRACTICE_SYSTEM.md`.

The deep method layer is preserved as the design engine, but user-facing language stays practical and grounded:

- body;
- energy;
- food impulses;
- sleep;
- movement;
- evening overeating;
- avoidance;
- pause;
- one inner task;
- one small next action;
- feedback without shame.

Advanced attention/direct pointing practices are included only as optional advanced material and are clearly marked as not core MVP.

## What Андрей should review first

Recommended review order:

1. `docs/CONTENT/03_BLOCK_SEQUENCE.md`  
   Check whether the 15-block learning path reflects the intended transformation logic.

2. `docs/CONTENT/05_14_DAY_PROTOCOL.md`  
   Check whether the 14-day protocol feels usable and not overloaded.

3. `docs/CONTENT/08_SCREEN_COPY_DRAFT.md`  
   Check tone and future app language.

4. `docs/CONTENT/10_BOUNDARIES_AND_TONE.md`  
   Check safety, product boundaries and wording around medicine, addiction, eating disorders and advanced practices.

## Open product decisions

1. How much should the term "разность потенциалов" appear in user-facing UI?
   Current content keeps it as a core concept but often translates it as "разрыв между сейчас и полезным направлением".

2. Should the first manual pilot include advanced direct pointing practices at all?
   Current recommendation: no, unless a participant is stable, grounded and explicitly interested.

3. Should body metrics include weight and waist by default or as optional fields?
   Current recommendation: optional but visible, to avoid turning the product into a weight tracker.

## Suggested next task

After Андрей reviews the content:

1. revise `docs/CONTENT/` based on product feedback;
2. prepare a manual pilot packet for 5-10 users;
3. only after content/pilot review return to mobile bootstrap.

