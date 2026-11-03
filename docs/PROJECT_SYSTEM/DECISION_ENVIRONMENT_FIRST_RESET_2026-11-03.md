# DECISION — Environment-first reset

**ID:** SP-PSYS-004  
**Status:** approved  
**Approved:** 3 November 2026  
**Owner:** Андрей  
**Scope:** active Selection Point product-development route.

## Decision

Selection Point is no longer developed primarily as a course that transfers knowledge to a learner.

The active product hypothesis is an **adaptive environment / simulator of selection and trajectory**: a person repeatedly encounters representative situations, perceives relevant signals, chooses a continuation, sees consequences across meaningful time scales, receives feedback, and then meets structurally similar situations under changed conditions.

The intended mechanism is not “explanation -> understanding -> correct behaviour”. The working mechanism is:

```text
representative situation
-> perceived position and constraints
-> available Selection Point
-> selected continuation
-> realized / non-realized continuation inside the simulation
-> consequences and trajectory change
-> feedback
-> next varied situation
-> adaptation
```

A second loop is mandatory:

```text
simulation experience
-> one bounded real-world experiment
-> observed real realization / non-realization
-> real consequences and contradictions
-> update of the next simulation / interpretation
```

Simulation performance is not evidence of real-world transfer by itself.

## Product meaning

Selection Point does not need to teach a person the project vocabulary before action. Concepts such as position, direction, route, action, selected versus realized continuation, feedback and trajectory become primarily **laws and mechanics of the environment**.

Theory may be used after or around experience to name a distinction that the person has already encountered, but theory is not the primary training mechanism.

The environment must avoid a hidden answer key that rewards obedience to the author. It should expose consequences, constraints and trajectory effects while preserving participant agency.

## Scientific claim boundary

The project does **not** adopt the claim that the brain cannot distinguish imagined, simulated and real experience.

The defensible working hypothesis is narrower:

- mental/simulated practice can engage learning-relevant processes and can improve some skills;
- immersion itself is not sufficient and is not assumed to be the mechanism;
- representative information-action relations and repeated experience matter;
- transfer to real behaviour must be measured separately rather than inferred from simulated performance.

Relevant evidence notes are recorded in `docs/FOUNDATION/SOURCE_MATERIALS/29_2026-11-03_ADAPTATION_ENVIRONMENT_AND_TRANSFER.md`.

## V0 boundary

The first product slice is intentionally small:

- one trainable capability / distinction;
- 10–15 representative situations;
- repeated structure with changed surface conditions;
- consequences visible at more than one time scale where meaningful;
- one bounded real-world transfer experiment;
- manual or very simple delivery is allowed;
- no VR requirement;
- no AI requirement;
- no platform requirement;
- no need to implement the full five-stage system.

The first domain remains **effective body / health and physical efficiency** as an observable practice field, without reducing the full method to health.

## Status of the course route

`docs/PROJECT_SYSTEM/DECISION_COURSE_FIRST_RESET_2026-09-20.md` is superseded **as the active development route**.

The course artifacts are not deleted. They remain historical/reference material and a source of:

- distinctions;
- scenario seeds;
- examples;
- failure modes;
- language candidates;
- evidence and safety constraints.

No course lesson, template or structure currently authorizes execution merely because it was previously approved.

## Status of Foundation and Gates

This decision is a product-route decision, not a silent rewrite of approved Foundation canon.

Therefore:

- approved Foundation material remains unchanged;
- Stage 5 remains unopened;
- previous A–H training artifacts remain research/reference inputs;
- SP-LAB-002 remains unopened;
- external-user pilot remains unopened;
- software implementation remains unopened until a separate explicit owner decision.

## Active next task

Define the **single V0 capability** and the **scenario grammar** required to train it inside the adaptive environment.

Do not build a platform, full course, VR system, AI agent or external pilot before this definition is reviewed.

## Supersedes

As active route only:
- `DECISION_COURSE_FIRST_RESET_2026-09-20.md`;
- course-first Lesson 1 execution as current next action.

Historical approvals and artifacts remain valid as history/reference unless separately revoked.