# Stage 1 Observability / Measurement Spec — Execution Contract

**ID:** SP-TR-S1-OM-SPEC-001  
**Gate:** F — Observability / Measurement Spec  
**Status:** active  
**Date:** 19 September 2026  
**Upstream capability:** `SP-TR-S1-CAP-002`  
**Upstream Learning Units:** `SP-TR-S1-LU-001`  
**Upstream Practice Protocol:** `SP-TR-S1-PP-001`  
**Gate E decision:** `SP-TR-DEC-S1-E-001`

## 1. Purpose

Gate F defines what can be observed, recorded and cautiously inferred from Stage 1 practice.

It must answer:

> **What evidence would distinguish actual Stage 1 participation from intention, reporting, environmental control, external prompting, useful automatic performance or retrospective explanation?**

Gate F must create an observability architecture, not a seductive single score.

## 2. Core measurement chain

The measurement model must preserve:

```text
current position
→ noticing / Selection Point evidence
→ selected continuation
→ realized continuation
→ consequence
→ feedback / update
→ next position
```

RC-018 remains binding.

No field may silently collapse:

```text
intention
selection
realization
outcome
feedback
```

## 3. Required evidence distinctions

Gate F must distinguish, at minimum:

### F1 — Opportunity / relevant lane
Was there a relevant recurrence or event where the trained lane plausibly applied?

Absence of an episode is not failure.

### F2 — Noticing timing
Where did noticing occur relative to the continuation?

Candidate descriptive classes may include:
- before old continuation began;
- while it was unfolding;
- after main action but before escalation/next continuation closed;
- consequence-only / next-cycle noticing;
- unknown.

These are descriptive, not moral rankings.

### F3 — Support provenance
Preserve:
- A — externally prompted;
- B — anticipatory scaffold-linked;
- C — participant-initiated;
- unknown.

These must not automatically become ordinal mastery levels.

### F4 — Interruption / open-edge evidence
Did the old continuation become non-exclusive, or was a late-entry still-open edge used?

Noticing alone is insufficient.

### F5 — Selection evidence
What continuation was selected?

### F6 — Realization evidence
What was actually realized?

At minimum preserve statuses already used by the project:
- executed;
- partially_executed;
- conscious_non_action;
- not_executed;
- circumstances_changed;
- revised_after_new_fact;
- forgotten;
- unknown.

### F7 — Environment contribution
Did environmental redesign, friction, removed cue or another person materially produce the better continuation?

Environment-supported success is useful but distinct from independent participant re-entry.

### F8 — Consequence evidence
What happened immediately after realization?

### F9 — Delayed consequence
What later consequence became observable, if any?

### F10 — Feedback/update evidence
Did the observed consequence alter the next model, preparation or continuation?

Consequence does not automatically equal used feedback.

## 4. Automaticity evidence problem

Gate F must explicitly handle the case:

```text
cue
→ useful trained response
```

with no identifiable conscious Selection Point.

This may be a desirable outcome.

It must not be misclassified as a conscious Stage 1 SP event.

Required distinction:

```text
useful automated performance
≠
observable conscious re-entry
```

The measurement architecture should allow both to coexist.

## 5. Questionnaire / measurement-reactivity problem

Measurement can change the phenomenon.

Therefore Gate F must preserve:
- questionnaire exposure;
- reminder exposure;
- whether future reporting was salient in the event;
- whether the participant reports changing behavior partly because it would later be reported;
- whether performance differs under different support conditions.

Gate F must not assume:
- questionnaire compliance = capacity;
- better reporting = better noticing;
- better outcome = internalized capability.

## 6. Rehearsal boundary

Rehearsal data must remain separate from real-world episode data.

```text
successful rehearsal
≠
successful retrieval under live conditions
```

Gate F may use rehearsal as contextual evidence but not substitute it for live performance.

## 7. Measurement burden boundary

The observability system itself must not overwhelm or redefine the skill.

Required principle:

> **Collect the minimum evidence needed to distinguish the important states.**

Every added field must justify its intervention cost.

Gate F must consider missing/unknown as valid values rather than forcing reconstruction.

## 8. No composite score by default

Gate F must not begin by inventing a single Selection Capacity score.

If any aggregation is proposed, it must first show:
- what distinct constructs are being combined;
- why aggregation is legitimate;
- what information is lost;
- how scaffold provenance is preserved;
- how no-opportunity periods are handled;
- how useful automatic performance is represented;
- how late-entry events are treated.

Default preference: transparent component measures / traces.

## 9. Candidate observability families

Gate F should evaluate candidate measures such as:

- opportunity count / exposure;
- noticing occurrence;
- noticing timing;
- prompt/scaffold provenance;
- open-edge identification;
- selected-to-realized relation;
- realization status;
- recovery after lapse;
- consequence registration;
- feedback/update use;
- recurrence under same lane;
- changes in support dependence;
- evidence of easier retrieval / lower cognitive load;
- useful automatic performance;
- mismatch-triggered reopenability.

These are candidate families, not approved metrics yet.

## 10. Trajectory boundary

Stage 1 measurement may summarize repeated events over time but must not silently become Stage 2 scenario interpretation.

Allowed:
- counts/traces of repeated realized/non-realized continuations;
- prompt-supported vs participant-initiated event history;
- recurrence timing;
- repeated late-entry vs earlier noticing;
- repeated environment dependence;
- repeated return of old route.

Not automatically allowed:
- asserting hidden recurring function;
- diagnosing a stable scenario;
- inferring identity structure.

## 11. Required falsification questions

Gate F must be able to reveal cases where apparent improvement is not evidence of the intended capability, for example:

- fewer bad outcomes because the environment removed the opportunity entirely;
- better questionnaire answers without earlier in-the-moment noticing;
- perfect reminder compliance with collapse when reminders are absent;
- participant reports more awareness but realized behavior is unchanged;
- useful automatic behavior improves while conscious SP events decrease;
- desired outcomes improve for reasons unrelated to participant action;
- participant creates more reportable episodes because the questionnaire changed behavior.

Measurement must make these possibilities visible where practical.

## 12. Gate F outputs expected

The final artifact should define:

1. event-level observable fields;
2. field semantics and allowed unknowns;
3. support provenance;
4. rehearsal vs live distinction;
5. opportunity/exposure handling;
6. selected-to-realized relation;
7. consequence / delayed-consequence handling;
8. feedback/update evidence;
9. automatic useful performance representation;
10. lapse/recovery representation;
11. minimal longitudinal summaries;
12. candidate readiness evidence without premature numeric mastery thresholds;
13. measurement-reactivity safeguards;
14. strongest limitations / non-inferences;
15. what evidence is sufficient to open Gate G.

## 13. Required Red Team attacks

Red Team must test whether the measurement system:

- measures reporting skill instead of Selection Capacity;
- creates the behavior it claims to observe;
- rewards hypervigilance;
- confuses prompt dependence with independent capacity;
- penalizes useful automaticity because fewer conscious SP events occur;
- penalizes no-opportunity periods;
- rewards easy lanes over difficult lanes;
- turns late detection into failure;
- treats good outcomes as capability;
- treats bad outcomes as lack of capability;
- ignores environmental support;
- over-infers causality;
- becomes too burdensome for real-life use;
- smuggles Stage 2 interpretation into Stage 1;
- encourages gaming.

## 14. Non-goals

Gate F does not authorize:
- a validated psychometric scale;
- clinical assessment;
- diagnostic thresholds;
- final composite Selection Capacity score;
- external-user pilot;
- software implementation;
- Stage 2 scenario scoring;
- Foundation canon changes.

## 15. Completion criterion

Gate F is ready for Owner review when it can distinguish the core evidence states with minimal burden, preserve support/measurement reactivity, represent useful automaticity without forcing conscious events, avoid causal overclaim, and specify what evidence Gate G would later assemble.

Gate G remains closed until explicit Owner approval.
