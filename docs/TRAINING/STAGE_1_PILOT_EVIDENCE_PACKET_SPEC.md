# Stage 1 Pilot Evidence Packet — Execution Contract

**ID:** SP-TR-S1-PEP-SPEC-001  
**Gate:** G — Pilot Evidence Packet  
**Status:** active  
**Date:** 19 September 2026  
**Upstream capability:** `SP-TR-S1-CAP-002`  
**Upstream Practice Protocol:** `SP-TR-S1-PP-001`  
**Upstream Observability / Measurement:** `SP-TR-S1-OM-001`  
**Gate F decision:** `SP-TR-DEC-S1-F-001`

## 1. Purpose

Gate G assembles empirical Stage 1 evidence and tests whether the approved training and measurement architecture survives contact with real data.

The task is not to prove Selection Point works.

The task is to ask:

> **What do the available real episodes support, what do they contradict, what remains unknown, and where does the current Stage 1 model fail to explain or measure reality cleanly?**

## 2. Evidence authority

Gate G may use:
- Owner self-pilot evidence already captured under the approved evidence-node policy;
- de-identified promoted findings from authorized evidence nodes;
- repository-stored pilot traces and reviews that comply with privacy rules.

Gate G must not:
- move raw personal/private data into the public repo;
- infer facts not present in the evidence;
- convert one self-pilot into proof of general efficacy;
- open an external-user pilot without separate authorization.

## 3. Required evidence packet structure

The packet must include:

### G1 — Evidence inventory
What real evidence sources exist, their dates, domains, capture method and privacy status.

### G2 — Data quality / provenance
For each evidence stream:
- source;
- capture timing;
- prompt/questionnaire exposure;
- known missingness;
- retrospective vs in-event status;
- normalization status.

### G3 — Stage 1 trace reconstruction
Where possible, reconstruct:
```text
candidate event
→ NOTICE
→ OPEN
→ SELECT
→ REALIZE
→ CONSEQUENCE
→ UPDATE
```
without inventing missing links.

### G4 — Support/scaffold analysis
Separate:
- current prompt activation;
- anticipatory reporting salience;
- environment configuration;
- social support;
- participant-initiated events;
- aligned automatic performance.

### G5 — Positive evidence
Episodes genuinely compatible with the Stage 1 model.

### G6 — Negative / contradictory evidence
Episodes where:
- intention did not realize;
- noticing did not open the route;
- opening did not produce an executable alternative;
- realization did not produce the expected consequence;
- questionnaire effects confounded interpretation;
- the model could not cleanly classify the event.

### G7 — Old-route return / recovery
Represent lapses as new positions, not reset/failure.

### G8 — Automaticity evidence
Identify any episodes where a continuation appears to have become easier, lower-load or automatic, while keeping:
- automaticity evidence exploratory;
- reopenability not_observed unless mismatch occurred.

### G9 — Measurement failures
Show where the approved Gate F schema is too heavy, ambiguous, redundant or unable to distinguish key states.

### G10 — Model update candidates
Only propose changes that are grounded in observed evidence.

Each proposal must be labeled:
- DERIVED;
- HYPOTHESIS;
- CONTRADICTION;
- OPEN.

No automatic promotion to canon.

## 4. Required comparison logic

The packet must distinguish at least:

```text
intention vs realization
prompted vs anticipatory-scaffold-linked vs participant-initiated
environment-supported vs participant re-entry
conscious SP cycle vs aligned automatic performance
rehearsal vs live
immediate consequence vs delayed consequence
consequence vs used feedback
```

## 5. Questionnaire-reactivity requirement

Because the Owner self-pilot already produced a plausible measurement-reactivity signal, Gate G must explicitly examine whether:

- later reporting became salient during the day;
- reporting salience changed behavior;
- reporting improved recall only;
- the questionnaire became a retrieval cue;
- the questionnaire created dependence;
- evidence is insufficient to distinguish these.

No causal conclusion is permitted without adequate design.

## 6. Falsification requirement

Gate G must actively search for evidence that weakens the current architecture.

At minimum ask:

- Are some “Selection Points” only retrospective stories?
- Does the model over-detect choice where no meaningful open edge existed?
- Does Lane Card preparation actually appear in live retrieval?
- Does OPEN add anything beyond NOTICE?
- Are realized alternatives mainly prompt-driven?
- Does aligned automatic performance emerge at all?
- Does late-entry practice produce meaningful recovery?
- Does the review create more update than it observes?
- Are some fields consistently unknown, making the schema impractical?
- Does the protocol create self-monitoring burden?
- Is the same event classifiable in multiple incompatible ways?

## 7. No score / no efficacy claim

Gate G must not produce:
- Selection Capacity Score;
- treatment-effect estimate;
- causal efficacy claim;
- participant ranking;
- domain ranking;
- “success percentage” detached from lane/provenance.

Descriptive counts/traces are allowed when their denominators and limitations are explicit.

## 8. Evidence gaps

The packet must include a dedicated section:

> **What we still cannot know from current evidence**

This should include missing opportunities, unobserved mismatch, uncertain support effects, recall limits, lack of counterfactuals, and any transfer questions.

## 9. Gate H readiness

Gate G is ready for Owner review when it presents a balanced evidence packet containing:
- supporting evidence;
- contradictory/negative evidence;
- unknowns;
- measurement limitations;
- falsification attempts;
- candidate updates;
- no hidden-cause inflation;
- no efficacy overclaim.

Gate H — Stage Review — remains closed until explicit Owner approval.
