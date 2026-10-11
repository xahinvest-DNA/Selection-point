# Recovery Checkpoint — Orientation Current-Action Layer Approved

**Date:** 11 October 2026  
**Status:** current recovery checkpoint  
**Project:** Selection Point

## 1. Active route

The active route remains **Stage 1 course-first development**.

The course remains a **self-paced online course**. Its core delivery does not require a teacher, facilitator or AI assistant.

The five-core-lesson structure remains unchanged. Orientation is a short standalone module before Lesson 1 and is not counted as a core lesson.

## 2. Approved entry architecture

The current approved Orientation entry is now three-part:

```text
1. Чего я хочу?
   → participant-owned desired result / direction

2. Что есть сейчас?
   → factual current position relative to that result

3. Что я реально делаю или не делаю сейчас в этой области?
   → initial description of current realized movement
```

The third output is part of factual current reality but must remain distinguishable from the current position itself.

It is **not** a causal conclusion. Orientation does not claim that the learner has the present position because of any listed action until later reality work supports such a relation.

The controlling decision is:

`docs/COURSE/DECISION_STAGE_1_ORIENTATION_ACTION_LAYER_AND_LESSON_1_REFRAMING_APPROVED_2026-10-11.md`.

## 3. Approved Lesson 1 reframing

Lesson 1 now begins from one general statement in Orientation output 3 and teaches one operation:

> **Take one general statement about what I actually do or do not do now and ground it in one concrete remembered case where this really happened.**

Learner-facing language should remain simple, for example:

> **Вспомните один конкретный случай, когда это произошло.**

A single case can show that the event happened at least once. It cannot by itself prove frequency, a recurring pattern, causality or representativeness of the learner's whole trajectory.

## 4. Concrete-case memory boundary

A chosen case must be identifiable enough to work with. At minimum the learner must be able to recover:

- approximately when / in what situation it happened;
- what happened;
- what they actually did or did not do;
- the immediate observable result.

For these core event-identifying elements, `не знаю / не помню` is not a normal completed answer. If the learner cannot recover enough of the event, they select another remembered case or wait for a naturally occurring future case.

`Не знаю / не наблюдал` remains valid for genuine unknowns such as causes, unobserved details and whether one case represents a broader pattern.

## 5. Simple learner-language rule

Internal methodological precision and learner-facing language are separate layers.

The learner should not have to learn Selection Point terminology in order to perform the Selection Point operation.

Prefer ordinary language such as:

- «Чего я хочу?»
- «Что есть сейчас?»
- «Что я реально делаю сейчас?»
- «Вспомните один конкретный случай, когда это произошло».

Terms such as `episode`, `релевантный эпизод`, `realization`, `reality check` and similar internal vocabulary remain internal unless they are genuinely needed for the learner's next action.

## 6. Current artifact and next step

`docs/COURSE/STAGE_1_LESSON_1_WORK_BRIEF.md` is now **reopened_for_revision** as version 4 because the previously approved v3 no longer matches the current entry architecture.

Single next step:

> **Пересобрать learner journey Урока 1 вокруг утверждённого трёхчастного входа Orientation и представить на утверждение.**

The final learner-facing Lesson 1 must not be written until the revised journey / brief is approved by the owner.

The old learner-facing Lesson 1 remains withdrawn as a product-format mismatch.

## 7. Authorization boundary

Authorized now:

- redesigning the Lesson 1 learner journey;
- revising the Lesson 1 work brief within the approved entry architecture;
- mechanical repository synchronization that preserves the approved meaning.

Owner approval is required before:

- final learner-facing Lesson 1 writing.

Not authorized now:

- Lesson 2 development;
- changing the five-core-lesson structure;
- Stage 2 or Foundation S5;
- questionnaire redesign;
- re-enabling automatic reminders;
- external pilot;
- trainer implementation;
- efficacy claims.

## 8. Operational state

All automatic Selection Point reminders remain disabled.

`SP-DTQ-002` remains withdrawn pending full redesign and is not part of the current course task.

### Persistent repository-write rule

For every repository change, follow `docs/PROJECT_SYSTEM/PROJECT_MANAGEMENT_PROTOCOL_V1.md`, section **4.1 — Атомарность связанных изменений репозитория**.

If one logical project change touches SSOT, recovery state, decisions, generated views or any other consistency-coupled files, prepare the complete synchronized set first and publish it to `main` as **one atomic commit**. Do not expose intermediate partially synchronized commits on `main`. If direct atomic publication is not technically possible, use a separate branch and move/merge into `main` only after consistency checks pass.

After publication, verify the consistency workflow before claiming synchronization complete.

**Carry this rule or its canonical protocol reference into every successor recovery checkpoint.**

## 9. Recovery order

For a new chat, recover active work from:

1. `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`
2. this checkpoint
3. `docs/PROJECT_SYSTEM/DECISION_COURSE_FIRST_RESET_2026-09-20.md`
4. `docs/COURSE/DECISION_SELF_PACED_COURSE_FORMAT_RESET_2026-10-07.md`
5. `docs/COURSE/DECISION_STAGE_1_STRUCTURE_WMF_APPROVED_2026-09-22.md`
6. `docs/COURSE/STAGE_1_EFFECTIVE_BODY_COURSE_STRUCTURE.md`
7. `docs/COURSE/DECISION_STAGE_1_ORIENTATION_ACTION_LAYER_AND_LESSON_1_REFRAMING_APPROVED_2026-10-11.md`
8. `docs/COURSE/STAGE_1_LESSON_TEMPLATE.md`
9. `docs/COURSE/STAGE_1_LESSON_1_WORK_BRIEF.md`
10. `docs/FOUNDATION/PROJECT_OPERATING_PROTOCOL_ADDENDUM_2026-10-05_DIRECTION_ROUTE_ACTION.md`

Additional documents should be routed by task rather than added to mandatory bootstrap.
