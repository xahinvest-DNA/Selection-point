# TASK-002 — Method domain models

## Role

You are Codex, implementation executor.

Implement only after TASK-001 mobile bootstrap is complete.

## Read first

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/PRODUCT_BRIEF.md`
4. `docs/DECISIONS.md`
5. `docs/METHOD_CORE.md`
6. `docs/PRACTICE_SYSTEM.md`

## Goal

Create the first TypeScript domain model layer for Selection Point.

The app is not a diet tracker. It is a system for turning automatic patterns into pause, inner task and next action.

## Required models

Create TypeScript types/interfaces for:

### UserProfile

- id
- createdAt
- displayName optional
- protocolStartDate optional

### PointA

Represents current fact before interpretation.

Fields:

- id
- createdAt
- category: body | food | energy | sleep | movement | alcohol | task | emotion | other
- factText
- bodySensation optional
- evidence optional

### PointB

Represents flexible direction, not rigid goal.

Fields:

- id
- createdAt
- directionText
- isFlexible: boolean
- bodyMarker: expansion | compression | neutral | unknown
- source: fear | shame | comparison | curiosity | interest | health | energy | unknown

### PotentialDifference

Fields:

- id
- createdAt
- pointAId optional
- pointBId optional
- gapText
- tensionLevel: 0-10
- secondKnotText optional

### Mechanism

Repeated pattern.

Fields:

- id
- createdAt
- type: evening_overeating | food_impulse | alcohol_impulse | avoidance | low_energy | anxiety | self_pressure | other
- triggerText
- automaticStory
- bodyMarker
- usualAction

### PausePractice

Fields:

- id
- createdAt
- practiceType: urge_pause | avoidance_pause | morning_direction | evening_review | direct_prompt
- beforeState
- afterState optional
- marker: plus | zero | minus | unknown
- notes optional

### InnerTask

Fields:

- id
- createdAt
- pointAId optional
- pointBId optional
- mechanismId optional
- taskText
- nextSmallAction
- checkCriteria
- active: boolean

### DailyCheckIn

Fields:

- id
- date
- weightKg optional
- sleepHours optional
- energyMorning: 0-10 optional
- energyDay: 0-10 optional
- energyEvening: 0-10 optional
- movementText optional
- foodImpulseCount optional
- overeatingEpisode: boolean optional
- alcohol: boolean optional
- mainTrigger optional
- oneObservation optional
- nextAction optional

## Required files

Suggested location:

```txt
src/domain/models.ts
src/domain/enums.ts
src/domain/index.ts
```

If the project structure after TASK-001 differs, place them in the closest appropriate domain folder.

## Acceptance criteria

- Types compile.
- Models are exported from a domain index file.
- No UI work required unless needed to prove compilation.
- No backend.
- No persistence yet.
- Add short comments explaining PointA, PointB, PotentialDifference and InnerTask.

## Report back

When done, report:

1. Files created/changed.
2. Any naming assumptions.
3. How models map to `docs/METHOD_CORE.md`.
4. Suggested next task.
