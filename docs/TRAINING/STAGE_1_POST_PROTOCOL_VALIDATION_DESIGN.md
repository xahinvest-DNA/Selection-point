
# Stage 1 Post-Protocol Validation Design

**ID:** SP-TR-S1-VAL-001  
**Status:** red_team_complete_owner_review_required  
**Date:** 20 September 2026  
**Parent decision:** SP-TR-DEC-S1-H-001  
**Architecture status:** approved_closed  
**Validation status:** efficacy_not_demonstrated / empirically_open  
**Upstream Practice Protocol:** SP-TR-S1-PP-001  
**Upstream Observability:** SP-TR-S1-OM-001  
**Red Team:** SP-TR-S1-VAL-RT-001  
**Red Team verdict:** pass_with_binding_boundaries  
**Nature:** direct post-protocol validation design; not an efficacy study by itself, not a mastery scale, not an external-user pilot authorization.

## 1. Purpose

Stage 1 architecture is closed. The next task is to test the final learner-facing protocol rather than continue redesigning it by default.

Primary question:

> Can the final Stage 1 protocol be used in live recurring situations, can its core transitions be observed without excessive burden, and does reality reveal a concrete reason to reopen the architecture?

The object under test is deliberately small:

~~~text
one lane
→ short Lane Card
→ NOTICE
→ OPEN
→ REALIZE
→ UPDATE
~~~

Human-facing compression:

> Заметь → открой → сделай → сверься.

The participant must not need the full designer/research architecture in working memory during a live event.

## 2. Validation ladder

### V0 — Owner feasibility / mechanism-compatibility pilot

Purpose:
- test live usability of the final Gate E protocol;
- test whether Gate F can represent actual episodes;
- expose structural contradictions;
- observe scaffold dependence and measurement reactivity;
- generate direct post-protocol traces.

V0 may use the existing Owner self-pilot authority.

It cannot establish independent efficacy because Owner is also designer, informed participant and final decision-maker.

### V1 — Independent-participant validation

Purpose:
- test whether findings survive outside Owner/designer expectancy;
- test usability with participants who did not design the model;
- provide stronger evidence on protocol effects and scaffold dependence.

V1 is design-only here. Execution requires separate explicit authorization for an external-user pilot and participant-data handling.

## 3. Primary validation questions

### VQ1 — Live feasibility

Can the participant use the learner-facing protocol in an actual recurrence without needing the full SP model?

Minimum live chain:

~~~text
marker / relevant recurrence
→ notice enough
→ identify a genuinely still-open edge
→ select or revise a continuation
→ realize something
→ observe what changed
~~~

### VQ2 — NOTICE / OPEN separability

Can evidence distinguish:

~~~text
noticed something
≠
a still-open continuation became usable
~~~

A retrospective alternative invented during review does not count as live OPEN.

### VQ3 — Selection / realization separability

Can live records preserve:

~~~text
selected
≠
realized
~~~

including match, partial match, non-match, conscious non-action, changed circumstances, revision after new fact and unknown.

### VQ4 — Scaffold provenance

Can the pilot distinguish:

~~~text
A — externally/currently prompted
B — anticipatory scaffold-linked
C — participant-initiated
mixed
unknown
~~~

C does not mean independence from all prior training, environment or social support.

### VQ5 — Measurement reactivity

Does future reporting or the capture system become salient during the event?

If yes, measurement is part of the intervention context and must remain visible.

V0 does not isolate protocol effects from measurement exposure.

### VQ6 — Retrieval load

Across recurrences, is there descriptive evidence compatible with:
- easier retrieval of the Lane Card sequence;
- less need to consult the Lane Card;
- reduced current-prompt dependence;
- aligned automatic performance?

These are observations, not proof of re-automatization.

### VQ7 — Reopenability

If aligned automatic performance emerges and reality later changes meaningfully, is participant re-entry observed?

If no relevant mismatch occurs:

~~~text
reopenability = not_observed
~~~

Automaticity and reopenability are opportunistic V0 observations, not required V0 outcomes.

### VQ8 — Burden / safety

Does the protocol create:
- continuous self-monitoring;
- excessive cognitive load;
- unsafe hesitation or interruption;
- living for the questionnaire;
- pressure to manufacture SP episodes?

A persistent burden signal may reopen Gate E even if target-domain outcomes improve.

## 4. What V0 can and cannot establish

V0 may establish:
- whether the protocol is executable or structurally unusable for this informed participant;
- whether the live compression is sufficient or requires hidden designer knowledge;
- whether Gate F fields are observable;
- whether NOTICE and OPEN can sometimes be separated in live episodes;
- whether support provenance can be captured;
- whether measurement/reporting salience occurs;
- whether selected/realized gaps can be represented without moral interpretation;
- specific architecture contradictions.

V0 cannot establish:
- general efficacy;
- population effect size;
- independent replication;
- durable re-automatization;
- robust transfer;
- clinical benefit;
- global Stage 1 mastery;
- independence from all scaffolding;
- causal effect of prompts or questions.

## 5. Participant and lane

Initial execution target:

~~~text
P-A / Owner self-pilot
~~~

Interpretation boundary:

~~~text
Owner evidence
= high-value design / contradiction evidence
≠ independent efficacy evidence
~~~

Select exactly one primary training lane.

The lane must:
- recur or be reasonably expected during the observation window;
- matter relative to a current local task, commitment, safety or direction;
- preserve at least some potentially influenceable continuation;
- be reasonably safe for self-directed practice;
- be neither deliberately trivial nor deliberately maximal-load.

Before launch, record:
- why the lane matters;
- why recurrence is expected;
- why an open edge plausibly exists;
- why self-directed practice is safe.

The lane is frozen for the main V0 window unless safety, sparse recurrence or new facts invalidate it. A lane change is logged rather than silently substituted.

## 6. Lane Card under test

Create one short Lane Card:

~~~text
WHEN — marker
OPEN — smallest opening move
THEN — executable alternative
WHY — local anchor, only if needed
SUPPORT — planned scaffold, if any
~~~

The card should fit on one small screen or note.

No new intervention is added during V0.

Specifically:
- SP-TR-HYP-002 Directed Question remains parked;
- no new motivational script;
- no new score;
- no extra introspective taxonomy.

Otherwise V0 would no longer test the approved Gate E protocol.

## 7. V0 sequence

### Phase 0 — Setup

One setup session:
1. choose one lane;
2. write Lane Card;
3. define safety boundary;
4. define capture route;
5. rehearse the short sequence only if useful;
6. mark rehearsal explicitly as rehearsal.

Rehearsal never counts as live evidence.

### Phase 1 — Supported acquisition

Purpose: test whether the final protocol can be retrieved and used at all before current support is reduced.

Current support may include the already approved Lane Card/reminder structure.

The pilot seeks evaluable live recurrences, not successful outcomes.

A recurrence may produce:
- full live SP cycle;
- partial cycle;
- old route without re-entry;
- revised continuation;
- conscious non-action;
- unknown links.

All are usable evidence.

### Phase 2 — Reduced-current-prompt observation

After the sequence has been used in some live recurrences, remove only safe research/training current prompts where practical.

Do not withdraw:
- medical or safety support;
- necessary protective constraints;
- ordinary social support;
- beneficial environment configuration.

Keep the Lane Card available and preserve ordinary real-life support.

Observe whether participation appears as anticipatory scaffold-linked, participant-initiated, mixed or not retrieved.

Important:

~~~text
reduced current prompt
≠ no scaffold
~~~

Phase 1 → Phase 2 cannot estimate a causal prompt-fading effect because it is confounded with time, practice, event difficulty and expectancy.

### Phase 3 — Natural continuation / mismatch probe

Continue normal use without manufacturing difficult situations.

Capture naturally occurring:
- old-route return;
- late noticing;
- partial realization;
- changed circumstances;
- aligned automatic performance;
- meaningful mismatch after apparent automation;
- recovery/re-entry.

Do not create harmful or high-load events to fill the evidence matrix.

## 8. Pragmatic stopping rule

V0 is a feasibility/architecture stress test, not a powered efficacy study.

Use an event-coverage target plus a calendar cap.

Pragmatic minimum coverage target:

~~~text
at least 6 evaluable live recurrences
with
at least 2 under supported/current-prompt conditions where relevant
and
at least 2 under reduced-current-prompt conditions
~~~

Calendar cap:

~~~text
maximum 21 days
~~~

These numbers are research-management rules only. They are not mastery thresholds, efficacy thresholds or validated scientific cutoffs.

Six homogeneous or weak episodes may still produce an inconclusive review.

Stop earlier if:
- a clear safety problem appears;
- burden becomes unacceptable;
- a decisive architecture contradiction appears.

At the cap, insufficient recurrence is classified as INSUFFICIENT_EXPOSURE, not participant failure.

## 9. Capture architecture

### 9.1 Event capture — minimal participant surface

Capture as soon after the event as practical and safe. Target burden: roughly 30–60 seconds.

1. Что произошло / какой маркер был?
2. Когда ты это заметил?
3. Что в тот момент ещё оставалось открытым?
4. Что ты выбрал и что фактически сделал?
5. Была ли активна подсказка, карточка, мысль о будущем отчёте или другая поддержка?
6. Что изменилось сразу после?

If unknown, record unknown.

For OPEN preserve timing:

~~~text
in_event
immediate_post_event
retrospective_hypothesis
unknown
~~~

Only in_event supports a live OPEN claim.

### 9.2 Minimal daily adherence/context item

Once per day:

> Был ли сегодня заметный эпизод выбранной lane?

~~~text
yes
no
unclear
not_reported
~~~

This is an adherence/context field only.

~~~text
no reported episode
≠ proof no opportunity occurred
~~~

### 9.3 Update capture

At the next minimal review:

> Изменило ли произошедшее следующую попытку, карточку, среду или план?

Possible output:
- no change;
- marker changed;
- OPEN move changed;
- alternative changed;
- environment changed;
- support changed;
- local anchor changed;
- direction revised after new fact;
- verbal insight only;
- unknown.

This preserves:

~~~text
consequence
≠ used feedback
~~~

### 9.4 Reactivity field

When relevant:

> В момент события ты помнил, что потом будешь это фиксировать?

~~~text
yes
no
unclear
unknown
~~~

Optional:

> Как тебе кажется, это повлияло на действие?

This remains self-report, not causal proof.

## 10. Normalized research trace

Participant capture remains short. Research normalization may represent:

~~~text
lane_id
episode_class
candidate_opportunity_evaluable

noticing_report
noticing_timing
marker_match

open_edge_status
open_edge_identification_timing
interruption_result

selected_continuation
execution_status
selected_realized_relation

support_provenance
current_prompt_activation
future_reporting_salience
environment_configuration
social_support_activation

immediate_consequence
delayed_consequence_optional

update_target
update_timing
update_evidence

evidence_source
capture_timing
raw_source_reference
unknown_fields
~~~

Normalization never upgrades self-report into fact.

## 11. Evidence coverage matrix

Report whether each class was observed:

- live full SP cycle;
- live partial cycle;
- old route without re-entry;
- late-entry recovery;
- selected → realized match;
- partial match;
- non-match;
- current-prompt-supported event;
- anticipatory scaffold-linked event;
- participant-initiated event;
- reporting salience;
- environment-supported event;
- aligned automatic performance;
- meaningful mismatch after aligned automation;
- spontaneous UPDATE;
- review-elicited UPDATE.

Missing cells remain not_observed.

No event is manufactured merely to fill the matrix.

## 12. Primary outputs

V0 produces traces and contradictions, not a score.

Required outputs:
1. lane definition + Lane Card;
2. de-identified episode table;
3. coverage matrix;
4. support-provenance summary;
5. measurement-reactivity summary;
6. selected → realized distribution without arbitrary partial weighting;
7. burden/safety notes;
8. explicit contradictions;
9. unresolved fields;
10. validation verdict.

Do not display a running success percentage during V0. The participant should not optimize a metric.

Existing SRCR may be reported only retrospectively as descriptive lane-local information with partial_match, non_match, not_evaluable and support context.

## 13. V0 verdict space

### V0-A — NO REOPENING CONTRADICTION OBSERVED

Meaning:

> No architecture contradiction requiring reopening was observed in this bounded Owner feasibility test.

Required evidence:
- learner-facing protocol was usable in at least some live episodes;
- Gate F represented important distinctions with acceptable burden;
- no structural safety contradiction appeared.

This does not mean efficacy, confirmation or proof.

Next candidate: request authorization for V1 independent-participant validation.

### V0-B — REOPEN GATE E

Use for practice-design contradiction, such as:
- Lane Card unusably heavy;
- live compression requires hidden theory knowledge;
- OPEN is structurally unusable under realistic conditions;
- persistent hypervigilance or unsafe hesitation.

### V0-C — REOPEN GATE F

Use when:
- important live distinctions cannot be captured;
- capture burden overwhelms the skill;
- support/prompt/realization cannot be separated enough for claimed interpretation.

### V0-D — REOPEN EARLIER GATE

Use only if direct evidence contradicts the capability/mechanism architecture itself.

### V0-E — INSUFFICIENT EXPOSURE

Use when the lane does not produce enough evaluable recurrence within the cap.

## 14. Interpretation rules

~~~text
desired outcome
≠ Stage 1 capability proof

undesired outcome
≠ Stage 1 failure

no current prompt
≠ independent skill

no contradiction observed
≠ architecture confirmed true
~~~

Owner has already been exposed to SP. V0 cannot create a true naïve baseline retroactively. Earlier pre-protocol data are context, not a causal control.

Immediate capture and daily review are themselves continuing measurement exposure. V0 does not isolate training from measurement.

## 15. V1 independent-participant design — reserved

V1 opens only after explicit Owner authorization.

Candidate design principles:
- participants do not design the model;
- one lane per participant;
- same Lane Card/live compression;
- raw source preserved separately from normalization;
- support provenance recorded;
- minimal review burden;
- where feasible, staggered or randomized current-prompt timing for stronger scaffold inference;
- no composite Selection Capacity score;
- no participant ranking;
- predefined contradiction/reopen rules;
- privacy contract before recruitment.

Sample size and comparative design must be chosen from the inferential claim V1 is intended to support. They are not fixed in V0.

## 16. Directed-question boundary

SP-TR-HYP-002 remains parked during V0.

The approved live protocol already contains minimal questions. Adding a special question intervention now would confound validation of approved Stage 1 with validation of a new hypothesis.

A later test should introduce directed questions as a separately identifiable intervention condition.

## 17. Data/privacy boundary

V0 raw Owner data remain in the private evidence node.

The public repository may receive only de-identified event structures, coverage summaries, contradictions and methodological findings.

V1 external raw data require a separately approved privacy/collection route.

## 18. Decision requested

Before V0 execution, Owner should approve or revise:
1. V0 purpose;
2. one-lane design;
3. supported → reduced-current-prompt sequence;
4. pragmatic coverage target + 21-day cap;
5. minimal capture surface;
6. verdict space;
7. exclusion of SP-TR-HYP-002 from this pass;
8. external-user execution remaining closed.

**Status before Owner decision:** Red Team complete; proposal only. V0 execution remains unauthorized.
