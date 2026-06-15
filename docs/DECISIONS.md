# DECISIONS

## D-001. Product format

**Decision:** v1 is a mobile-first application.

**Reason:** The core user behaviour is daily check-in, body observation, food impulse tracking and short practices. A phone is the natural environment for this.

## D-002. First domain

**Decision:** v1 focuses on healthy energetic body + life, not trading.

**Reason:** Body gives faster feedback loops than trading. Weight, sleep, waist, energy, hunger, movement and food impulses can be checked daily.

## D-003. Product is not a diet app

**Decision:** The product must not be positioned as a diet or calorie-counting app in v1.

**Reason:** The core mechanism is internal task formation and feedback, not nutritional micromanagement.

## D-004. MVP protocol length

**Decision:** First protocol length is 14 days.

**Reason:** 14 days is long enough to reveal patterns and short enough to complete without heavy resistance.

## D-005. Initial technical direction

**Decision:** Recommended MVP stack: Expo + React Native + TypeScript.

**Reason:** Fast bootstrap, Android/iOS support, active ecosystem, good fit for Codex execution.

Reference: Expo official docs recommend creating a default project with `create-expo-app`; current docs show `npx create-expo-app@latest --template default@sdk-56` during SDK 56 transition.

## D-006. Storage direction

**Decision:** MVP should be local-first.

**Reason:** User can start without account, backend, privacy concerns or sync complexity.

Possible storage:

- phase 1: in-memory / simple local storage for UI prototype;
- phase 2: SQLite through `expo-sqlite` for persisted journal data.

Reference: Expo SQLite provides a persisted database queried through SQLite API and is available for Android, iOS and web.

## D-007. No backend in first technical slice

**Decision:** No backend until the core loop works locally.

**Reason:** Backend will slow feedback and add unnecessary infrastructure before product behaviour is validated.

## D-008. First user loop

**Decision:** The first implemented loop must be:

```
Onboarding → Daily Check-in → Mechanism Selection → Inner Task → Feedback
```

## D-009. Data before advice

**Decision:** The app must collect observation data before giving strong recommendations.

**Reason:** The system is built on reality contact, not generic advice.

## D-010. Main PM rule

**Decision:** Every feature must answer one question:

> Does this help the user turn tension into a clear internal task and a next action?

If not, it is not MVP.
