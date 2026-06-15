# ROADMAP

## Phase 0 — Project foundation

Goal: make the project executable for Codex.

Deliverables:

- README.md
- CURRENT_STATE.md
- PRODUCT_BRIEF.md
- METHOD_CORE.md
- DECISIONS.md
- ROADMAP.md
- CODEX_TASKS.md
- first Codex bootstrap task

Status: in progress.

## Phase 1 — Mobile app bootstrap

Goal: create a runnable Expo + React Native + TypeScript app.

Deliverables:

- Expo app scaffold;
- TypeScript configured;
- basic navigation;
- clean folder structure;
- placeholder screens;
- ability to run locally on phone / emulator.

Acceptance criteria:

- `npm install` works;
- `npm run start` launches Expo;
- app opens on phone/emulator;
- home screen displays project name and primary action.

## Phase 2 — UX skeleton

Goal: implement the first user path without complex persistence.

Screens:

1. Welcome
2. Point A / Day 0 Diagnosis
3. Daily Check-in
4. Point B / Direction
5. Potential Difference Map
6. Mechanism Selection
7. Inner Task
8. Practice
9. Feedback Summary

Acceptance criteria:

- user can move through all screens;
- form state is preserved during one app session;
- no final visual design needed;
- UX copy follows project tone.
- UX structure follows `docs/METHOD_CORE.md`.

## Phase 3 — Local data model

Goal: persist user journal locally.

Entities:

- UserProfile
- BaselineDiagnosis
- DailyCheckIn
- FoodImpulse
- Mechanism
- InnerTask
- FeedbackCycle

Acceptance criteria:

- data persists after app restart;
- user can view previous daily entries;
- derived summary can be calculated from stored data.

## Phase 4 — 14-day protocol engine

Goal: make app guide user by protocol day.

Protocol:

- Day 0: diagnosis;
- Days 1–3: observation;
- Days 4–7: mechanism focus;
- Days 8–11: system building;
- Days 12–14: feedback and next task.

Acceptance criteria:

- app knows current protocol day;
- screen prompts adapt by phase;
- user can see progress;
- app generates a weekly/phase summary.

## Phase 5 — Feedback and insight layer

Goal: transform raw entries into useful insight.

Outputs:

- repeated triggers;
- repeated food impulses;
- weight trend;
- sleep/energy relationship;
- alcohol impact notes;
- main mechanism hypothesis;
- suggested inner task.

Acceptance criteria:

- app gives simple summaries without pretending to be a doctor;
- insights are traceable to user entries;
- user can accept/edit the suggested inner task.

## Phase 6 — Design and polish

Goal: make prototype pleasant enough for real user testing.

Deliverables:

- visual style;
- typography;
- empty states;
- microcopy;
- error states;
- onboarding clarity.

## Phase 7 — Pilot

Goal: test on 5–10 real users.

Metrics:

- onboarding completion;
- check-ins completed;
- 14-day completion;
- mechanisms identified;
- perceived clarity;
- reported energy/body changes;
- willingness to continue.

## Deferred

Not MVP:

- paid subscriptions;
- backend sync;
- social features;
- calorie database;
- AI coach chat;
- wearable integrations;
- App Store / Google Play release;
- medical recommendations;
- advanced analytics;
- trader version.
