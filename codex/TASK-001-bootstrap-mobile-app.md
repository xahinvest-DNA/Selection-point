# TASK-001 — Bootstrap mobile app

## Role

You are Codex, implementation executor.

Do not redesign product strategy. Implement the first runnable technical foundation.

## Read first

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/PRODUCT_BRIEF.md`
4. `docs/DECISIONS.md`
5. `docs/ROADMAP.md`
6. `docs/CODEX_TASKS.md`

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

## Required implementation

Create a runnable app with:

1. TypeScript.
2. Basic navigation or a simple screen router.
3. A Welcome screen.
4. Placeholder screens for the first user loop:
   - Welcome
   - Day 0 Diagnosis
   - Daily Check-in
   - Potential Difference
   - Mechanism Selection
   - Inner Task
   - Feedback Summary
5. Clean folder structure.
6. README run instructions.

## Suggested folder structure

```txt
app/
  _layout.tsx
  index.tsx
  diagnosis.tsx
  check-in.tsx
  potential-difference.tsx
  mechanism.tsx
  inner-task.tsx
  feedback.tsx
src/
  domain/
  features/
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

## Acceptance criteria

- `npm install` succeeds.
- `npm run start` launches Expo.
- App opens on emulator or physical phone.
- User can navigate between placeholder screens.
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
