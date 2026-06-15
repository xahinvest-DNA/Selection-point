# TASK-001 — Bootstrap mobile app

## Role

You are Codex, implementation executor.

Do not redesign product strategy. Implement the first runnable technical foundation.

## Read first

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/PRODUCT_BRIEF.md`
4. `docs/METHOD_CORE.md`
5. `docs/DECISIONS.md`
6. `docs/ROADMAP.md`
7. `docs/CODEX_TASKS.md`

## Goal

Create the first runnable mobile app skeleton for Selection Point.

Recommended stack:

- Expo
- React Native
- TypeScript

Official Expo docs currently show project creation with:

```bash
npx create-expo-app@latest --template default@sdk-56
```

Use the most practical approach for this repository. If the exact SDK template creates conflicts, use the closest stable Expo TypeScript setup and document the choice.

## Product frame

The app is not a diet app.

It is a mobile protocol for:

- body awareness;
- energy;
- food impulses;
- sleep;
- movement;
- potential difference;
- inner task formation;
- feedback loops.

The app is also not a generic habit tracker or meditation app. Its core is the training of a choice point:

```txt
Point A -> Point B -> Potential Difference -> Automatic Program or Inner Task -> Practice -> Action -> Feedback
```

Use the method from `docs/METHOD_CORE.md` as the product spine. Do not expose advanced philosophical language in the first UI, but make sure the structure, naming and copy already reflect it.

## Method-aware implementation guidance

The first runnable skeleton should make the core method visible even before full forms exist.

Use these concepts in screen names, placeholder copy and early data structure:

- Point A: current fact / diagnosis without judgment.
- Point B: direction or orientation, not a rigid goal.
- Potential Difference: tension between current state and possible direction.
- Automatic Program: repeated impulse, avoidance, craving or resistance.
- Inner Task: one trainable transition from automatic reaction to next action.
- Practice: pause, distinguish, expand, choose one small move.
- Feedback: what reality showed, without praise or blame.

Important UX distinction:

- Avoid: "lose weight fast", "fix yourself", "be disciplined", "control cravings".
- Prefer: "notice the mechanism", "pause before the automatic move", "choose one small next action", "use feedback".

## Required implementation

Create a runnable app with:

1. TypeScript.
2. Basic navigation or a simple screen router.
3. A Welcome screen.
4. Placeholder screens for the first user loop:
   - Welcome
   - Point A / Day 0 Diagnosis
   - Daily Check-in
   - Point B / Direction
   - Potential Difference
   - Mechanism Selection
   - Inner Task
   - Practice
   - Feedback Summary
5. Clean folder structure.
6. README run instructions.
7. A small typed domain skeleton for the method concepts.

## Suggested folder structure

```txt
app/
  _layout.tsx
  index.tsx
  diagnosis.tsx
  check-in.tsx
  direction.tsx
  potential-difference.tsx
  mechanism.tsx
  inner-task.tsx
  practice.tsx
  feedback.tsx
src/
  domain/
    protocol.ts
    method.ts
  features/
    checkIn/
    diagnosis/
    feedback/
    innerTask/
    mechanism/
    practice/
  shared/
  storage/
  ui/
```

If using Expo Router, follow its conventions.

## UX copy direction

Tone:

- calm;
- precise;
- non-judgmental;
- no shame;
- no motivational noise;
- fact → task → action.

Welcome screen should communicate:

> Selection Point helps you turn body chaos, food impulses and low energy into a clear inner task and a next action.

Suggested Welcome copy direction:

> This is not a diet. Selection Point helps you notice the moment before an automatic reaction and turn body chaos into one clear next action.

Placeholder screens should not be empty. Each screen should contain one or two sentences that explain its role in the method:

- Point A: "Start with facts, not blame."
- Point B: "Choose a direction lightly enough to test."
- Potential Difference: "See the tension between what is and what could be."
- Mechanism: "Name the repeated program before changing it."
- Inner Task: "Train one transition, not your whole life at once."
- Practice: "Pause, distinguish, expand, then choose one small move."
- Feedback: "Reality gives data, not judgment."

## Acceptance criteria

- `npm install` succeeds.
- `npm run start` launches Expo.
- App opens on emulator or physical phone.
- User can navigate between placeholder screens.
- Placeholder copy follows `docs/METHOD_CORE.md`.
- Domain skeleton includes types for Point A, Point B, Potential Difference, Automatic Program/Mechanism, Inner Task, Practice and Feedback.
- README includes run instructions.
- No backend is added.
- No authentication is added.
- No payment/subscription is added.

## Report back

When done, report:

1. Files created/changed.
2. How to run.
3. What assumptions were made.
4. Any blockers.
5. Suggested next task.
