
# Stage 1 Post-Protocol Validation Design — Red Team

**ID:** SP-TR-S1-VAL-RT-001  
**Date:** 20 September 2026  
**Reviewed artifact:** SP-TR-S1-VAL-001  
**Status:** red_team_complete_revision_required

## 1. Review question

Can V0 stress-test the final Stage 1 protocol without turning Owner self-pilot into efficacy evidence, without making measurement the intervention and then crediting the protocol, and without using arbitrary event counts as mastery criteria?

## 2. Verdict

**PASS WITH BINDING REFINEMENTS.**

The design is appropriate as a feasibility / architecture stress test.

Its strongest features:
- the exact approved learner-facing protocol is the test object;
- Owner evidence is explicitly weak for independent efficacy;
- NOTICE / OPEN / SELECT / REALIZE remain separate;
- prompt/reporting provenance remains visible;
- event coverage is preferred over a success score;
- Directed Question is not smuggled into V0;
- V1 external execution remains closed.

## 3. Main attacks

### RT-VAL-01 — Phase 1 → Phase 2 is time/practice confounded

Later reduced-prompt performance cannot establish a causal fading effect.

Required boundary:
- V0 describes performance under different support states;
- causal scaffold inference is deferred to V1 comparative design.

### RT-VAL-02 — Six episodes is arbitrary

Required boundary:
- six is only a pragmatic minimum coverage target;
- it is not a mastery, efficacy or scientific sufficiency threshold;
- homogeneous weak data may still be inconclusive.

### RT-VAL-03 — Owner expectancy can clean up the narrative

Required boundary:
- prefer short contemporaneous capture;
- retain raw wording/source lineage;
- contradictory/messy events are high-value evidence.

### RT-VAL-04 — Event capture is itself an intervention

Required boundary:
- capture timing and reporting salience remain visible;
- V0 does not isolate protocol effects from measurement exposure.

### RT-VAL-05 — OPEN may be manufactured retrospectively

Required boundary:
- preserve in_event vs immediate_post_event vs retrospective_hypothesis;
- only in_event supports live OPEN.

### RT-VAL-06 — Lane difficulty can distort the test

Required boundary:
- lane must be relevant and recurrent, but neither deliberately trivial nor maximal-load;
- record why it is suitable before launch.

### RT-VAL-07 — Environment support can mimic participant re-entry

Required boundary:
- environment configuration stays orthogonal;
- environment-enforced behavior is not participant-initiated OPEN.

### RT-VAL-08 — Match-rate optimization risk

Required boundary:
- no running success percentage;
- evaluate distributions only after the evidence window;
- episode count and match rate are not rewards.

### RT-VAL-09 — Support fading must not remove safety

Required boundary:
- reduce only safe research/training prompts;
- never withdraw necessary safety, medical, environmental or social support to prove independence.

### RT-VAL-10 — V0-A must remain weak falsification language

Required wording:

> No architecture contradiction requiring reopening was observed in this bounded Owner feasibility test.

Not validated, confirmed or proven.

### RT-VAL-11 — No-event days can disappear from the record

Required refinement:
- one minimal daily item: yes / no / unclear / not_reported for a noticeable selected-lane episode;
- this is not an invisible opportunity denominator.

### RT-VAL-12 — Automaticity/reopenability may take longer

Required boundary:
- they are opportunistic V0 observations;
- absence cannot block V0-A.

## 4. Final verdict

**PASS WITH BINDING BOUNDARIES** after these refinements.

Recommended governance state:

~~~text
validation_design:
  owner_review_required

V0_execution:
  not_authorized_until_owner_approval

external_user_pilot:
  unopened
~~~
