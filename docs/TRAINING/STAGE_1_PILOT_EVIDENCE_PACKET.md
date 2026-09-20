# Stage 1 Pilot Evidence Packet

**ID:** SP-TR-S1-PEP-001  
**Status:** red_team_complete_owner_review_required  
**Gate:** G — Pilot Evidence Packet  
**Date:** 20 September 2026  
**Upstream capability:** SP-TR-S1-CAP-002  
**Upstream Practice Protocol:** SP-TR-S1-PP-001  
**Upstream Observability / Measurement:** SP-TR-S1-OM-001  
**Execution contract:** SP-TR-S1-PEP-SPEC-001  
**Red Team:** SP-TR-S1-PEP-RT-001  
**Evidence scope:** private owner self-pilot + authorized neighboring-project participant data, promoted here only as de-identified findings.  
**Nature:** empirical evidence assembly; not an efficacy study, psychometric validation, diagnosis or external-pilot authorization.

---

# 1. Executive finding

The current evidence does **not** establish that Selection Point training is effective.

This corpus is best classified as **pre-protocol / transitional compatibility evidence**: it was collected largely before the approved Gate E protocol existed in its final form.

It does provide a useful reality test of the Stage 1 architecture.

Across 14 daily records from three participants, the strongest recurring empirical pattern is not “better choices.” It is the instability of the transition:

~~~text
intended / selected continuation
→
actually realized continuation
~~~

The same participant can realize one intended continuation while another competing continuation follows an older route in the same day.

The current data therefore strongly justify keeping separate:

~~~text
intention
≠ selection
≠ realization
≠ outcome
≠ feedback
~~~

A second strong finding is that measurement is not neutral. In the owner self-pilot, future questionnaire reporting became salient during the day and at least one reported behavior change was explicitly attributed by the participant to the expectation of later reporting.

The evidence packet therefore supports the **measurement-reactivity boundary**, while not establishing its mechanism or generality.

The evidence does **not** yet cleanly test the approved Gate E protocol because most of the records were captured before the Lane Card / rehearsal / NOTICE → OPEN → REALIZE → UPDATE practice architecture was operationalized.

---

# 2. Evidence inventory

Raw private data are not copied into this public control-plane repository.

The packet uses de-identified derived findings from four evidence streams.

| Source | Participant | Date range | Records | Capture form | Privacy status |
|---|---|---:|---:|---|---|
| E1 | P-A | 12–15 Sep 2026 | 4 | private Health Lab evening self-report; legacy heterogeneous schema | raw private |
| E2 | P-A | 16–19 Sep 2026 | 4 | neighboring Selection point Lab / local participant store | raw private |
| E3 | P-B | 16–18 Sep 2026 | 3 | neighboring Selection point Lab / local participant store | raw private external participant |
| E4 | P-C | 16–18 Sep 2026 | 3 | neighboring Selection point Lab / local participant store | raw private external participant |

Total current corpus:

~~~text
3 participants
14 participant-days
8 owner-self-pilot days
3 + 3 external-participant days
~~~

Participant identities, exact body measurements and raw free-text reports remain outside this public artifact.

---

# 2.1 Sampling / adherence boundary

The analyzed corpus contains **submitted reports**, not a known unbiased sample of all relevant days or all candidate opportunities.

~~~text
submitted report
≠
all opportunities that occurred
~~~

Missing or unsubmitted data could be related to difficult days, forgetting, low motivation, collection friction or unrelated circumstances.

Measurement adherence must therefore remain separate from behavior/capability interpretation.

---

# 3. Data quality and provenance

## 3.1 P-A / 12–15 September

The first four records are legacy Health Lab data.

Strengths:
- report date known;
- raw self-report preserved privately;
- several realized/non-realized divergences are explicit.

Limitations:
- schema drift across days;
- no reliable in-event timestamps;
- prompt exposure usually not captured;
- NOTICE and OPEN cannot be cleanly separated;
- review timing relative to insight/update is mostly unknown.

## 3.2 P-A / 16–19 September

These records use the expanded daily questionnaire and are more structured.

Strengths:
- clearer separation of prior intention, daily fact and next-day intention;
- more explicit state/context fields;
- one strong direct report of questionnaire salience changing behavior.

Limitations:
- still primarily evening retrospective self-report;
- exact noticing/opening timestamps absent;
- A/B/C provenance cannot be reconstructed for most episodes;
- environment configuration is incompletely captured.

## 3.3 P-B / P-C / 16–18 September

These records provide two additional participants and therefore useful cross-case recurrence/falsification. They do not constitute independent replication of efficacy.

Strengths:
- same general questionnaire structure;
- multiple examples of intention/realization match and non-match;
- competing urges/context are sometimes explicitly described.

Limitations:
- short three-day window;
- report transfer/ingestion was owner-mediated;
- participant submission timestamps are unavailable in the source package;
- no independent behavioral observation;
- no controlled questionnaire-off condition;
- some early fields are ambiguous or mixed-domain.

## 3.4 Source-lineage caveat for external participants

External reports were transferred through the Owner/local collection workflow before normalization.

Where original participant submission timestamps are unavailable:

~~~text
participant_submitted_at_local = unknown
~~~

Ingestion time must not be interpreted as participant response time.

Future collection should preserve the raw participant submission separately from ingestion/normalization.

---

---

# 4. De-identified event reconstruction

The following are **partial derived event reconstructions**, not raw records.

Evidence-status legend:

~~~text
SELF-REPORT — directly reported by participant
DERIVED — analyst mapping/synthesis from source report
OPEN — not observed / not resolvable from current evidence
CONTRADICTION — evidence that weakens a simple current interpretation
~~~

A chain is never treated as fully observed merely because it is presented sequentially. Missing NOTICE / OPEN / timing links remain OPEN.

## 4.1 P-A

### A12 — divergent lanes under high stress

~~~text
high stress / low energy
→ one planned health continuation realized
→ another old-route consumption continuation occurred
→ planned physical training did not occur
~~~

**Evidence value:** one day can contain simultaneous realized and non-realized target continuations.

**Supports:** selected/desired behavior must not be collapsed into one daily “success” state.

**Does not establish:** why the old route occurred.

### A13 — action despite postponement impulse

~~~text
meaningful work available
→ initial urge to postpone
→ work realized
~~~

A separate health route remained unchanged that day.

**Supports:** action can diverge from immediate urge.

**Gap:** noticing timing and opening move were not captured.

### A14 — two different intention→realization transitions in the same day

~~~text
physical fatigue + urge to postpone training
→ training realized

weak intention to avoid an old consumption route
→ old route realized
~~~

**Strong evidence for:** Stage 1 cannot be inferred from daily outcome totals. Different lanes within one person behave differently.

### A15 — explicit intention not realized; another difficult action realized

~~~text
prior avoidance intention
→ unexpected physical discomfort
→ old route realized

low work motivation
→ project work realized
~~~

**Supports:** intention strength and action accessibility are context-sensitive.

**Contradicts:** any simple model in which clear prior intention is sufficient for realization.

### A16 — competing urge present, intended continuation realized

~~~text
old-route urge appears
→ old route not realized
→ intended continuation realized
~~~

A separate physical-training plan was not realized because of schedule/context constraints.

**Supports:** non-realization in one lane must not automatically be called sabotage.

**Gap:** the actual opening operation is not observed.

### A17 — old-route purchase impulse not realized

~~~text
old-route purchase impulse
→ purchase not realized
→ physical-training continuation realized
~~~

**Candidate evidence:** participant participation altered the next continuation.

**Gap:** prompt/future-reporting salience for this specific event is unknown.

### A18 — partial task realization and old-route return

~~~text
planned work
→ work started
→ scope larger than expected
→ work remained incomplete

health old route
→ limited recurrence
~~~

**Supports:** partial realization can reflect planning error / changed task size rather than motivational failure.

**Supports:** old-route return does not mean previous episodes were fictitious or “reset.”

### A19 — strongest measurement-reactivity event

Participant reported a sustained old-route urge and explicitly stated that remembering the future questionnaire affected the continuation.

Derived structure:

~~~text
old-route urge
→ future-reporting salience
→ old route not realized
→ subjective relief afterward
~~~

Provenance candidate:

~~~text
B — anticipatory scaffold-linked
~~~

**OBSERVED SELF-REPORT:** future reporting was salient.

**OBSERVED SELF-REPORT:** participant attributes behavioral change to that salience.

**OPEN:** whether the mechanism was prospective monitoring, accountability/demand, cueing, self-presentation, another mechanism or a combination.

**Critical implication:** questionnaire exposure cannot be treated as neutral telemetry.

---

# 5. P-B evidence

### B16 — high realization, weak construct purity

Several planned actions were completed and the participant reported that planning made action simpler.

However, the intended-action field mixed health-related and ordinary household/logistical actions.

**Supports:** planning may increase action accessibility.

**Measurement contradiction:** when a field mixes domains, a realized plan is not clean evidence of the target Stage 1 capability or the health lane.

### B17 — planned action realized despite competing rest/avoidance impulse

~~~text
planned household action
→ desire to rest / avoid
→ action realized
→ participant reports planning makes action simple
~~~

**Candidate evidence:** selected continuation remained retrievable despite competing impulse.

**Gap:** no in-event NOTICE timing or explicit OPEN operation.

### B18 — prepared plan loses to contextual/social cue

~~~text
prepared evening plan
→ social-information cue + relaxation urge
→ planned alternative not realized
→ old evening route realized
~~~

The participant also reported that limiting the route felt easier than before.

**Supports:** prepared intention is not sufficient under a salient cue.

**Possible partial adaptation:** self-reported reduction/limitation may have occurred.

**Cannot conclude:** that this was a Stage 1 OPEN/REALIZE success without stronger comparison and timing evidence.

---

# 6. P-C evidence

### C16 — mixed realization across multiple intentions

~~~text
exercise intention
→ exercise realized

food-choice intention
→ old food route persisted
~~~

**Supports:** skill expression is lane-specific; one realized intention cannot represent the whole day.

### C17 — action despite “do not want to” impulse; another old route persists

~~~text
planned exercise
→ desire not to do it
→ exercise realized

separate food-choice route
→ old route still present
~~~

Participant reported that the planned action felt more accessible.

**Candidate evidence:** repetition/planning may reduce action friction.

**Not evidence of:** automaticity.

### C18 — prepared food-choice direction survives a competing urge

~~~text
planned alternative
→ urge to take old-route option
→ old-route option not taken
→ participant reports substitute option feels easier
~~~

**Candidate Stage 1 compatibility:** a competing urge was present and another continuation was realized.

**Gap:** whether NOTICE and OPEN occurred consciously in-event remains unknown.

**Automaticity status:** not established.

---

# 7. Cross-case findings

## F-1 — Intention → realization is genuinely unstable

**DERIVED — supported across all three participants.**

The data contain:
- intentions realized;
- intentions not realized;
- partial realizations;
- circumstances/context changes;
- multiple different realization states within the same day/person.

This supports RC-018 and the Stage 1 separation:

~~~text
selected
≠
realized
~~~

It also weakens any training system that treats planning itself as evidence of capacity.

## F-2 — Lane specificity is visible very early

**DERIVED.**

Across participants, improvement/realization in one lane coexists with old-route behavior in another lane.

Therefore:

~~~text
better performance in one lane
≠
global Selection Capacity demonstrated
~~~

This is compatible with the Gate E decision to train one narrow lane rather than “the whole person.”

## F-3 — Competing impulse does not determine realization

**DERIVED.**

Multiple reports contain:
- urge to postpone but action occurred;
- urge to use an old route but it did not occur;
- urge to avoid planned exercise but exercise occurred;
- urge for an old food choice but it was not realized.

Therefore:

~~~text
urge
≠
action
~~~

This distinction is empirically useful in the current data.

## F-4 — Participants report greater accessibility after planning, but planning is not sufficient

**DERIVED + HYPOTHESIS.**

All three participants provide self-reports compatible with greater accessibility of a prepared continuation. Because planning is foregrounded by the questionnaire, this may reflect genuine accessibility, questionnaire framing, or both.

Participants report variants of:
- planning makes action simpler;
- planned action feels more available;
- a repeated substitute feels easier;
- repeated control behavior is becoming easier.

But strong/contextual cues still sometimes override the plan.

Thus the evidence supports:

~~~text
prepared continuation
may improve retrieval/accessibility
≠
guaranteed realization
~~~

It does not establish an implementation-intention mechanism specifically.

## F-5 — Measurement reactivity is directly reported in P-A and must be a first-class confound

**OBSERVED SELF-REPORT for P-A; OPEN for generalization.**

P-A is also the project Owner/designer and is highly familiar with the Selection Point model. This makes the self-pilot high-value design evidence but weak independent efficacy evidence.

Two pieces of owner evidence matter:

1. a meta-observation after several days that anticipated evening reporting began affecting in-day noticing/participation;
2. A19, where future questionnaire completion was explicitly reported as changing the continuation.

This supports the Gate F requirement to record:

~~~text
future_reporting_salience
current_prompt_activation
capture timing
~~~

But there is no equivalent explicit evidence yet for P-B or P-C.

## F-6 — Evidence for lower cognitive load exists; evidence for automaticity does not

**DERIVED.**

Several reports describe action as becoming “easier,” “simpler,” or more available.

This is compatible with reduced retrieval/action friction.

It is **not enough** to classify aligned automatic performance because the records still describe plans, urges and conscious comparisons.

Therefore re-automatization remains **OPEN**. Automaticity is **not demonstrated**; this does not mean automaticity is absent, because low-attention events may be underreported by a reflective questionnaire.

## F-7 — No clean test of reopenability exists

There is no documented sequence of:

~~~text
established aligned automatic route
→ meaningful new mismatch
→ route reopened/revised
~~~

Therefore:

~~~text
reopenability = not_observed
~~~

not “absent.”

---

# 8. What the current data do NOT test

The existing records predate the full Gate E practice protocol.

They do not provide a fair empirical test of:

- Lane Card;
- prepared WHEN / OPEN / THEN structure;
- explicit safe rehearsal;
- deliberate environment-first design;
- the minimum live script as a trained sequence;
- prompt fading;
- transfer across matched contexts;
- robust performance under controlled high load.

Gate G must not criticize these components for lack of evidence when participants were not actually trained with them.

---

# 9. Negative / contradictory evidence

## N-1 — Planning can fail under a salient cue

Observed in P-A and P-B.

This directly prevents the project from equating clear intention with available realization.

## N-2 — Questionnaire can contaminate the phenomenon being measured

A19 is the clearest example.

If a questionnaire changes the action, then a later increase in aligned behavior cannot be read as pure observation of an unchanged person.

The measurement instrument may be part of the causal position.

## N-3 — Current questionnaire does not reliably distinguish NOTICE from OPEN

Many episodes are reconstructable as:

~~~text
urge / planned action
→ different realized action
~~~

but the data often cannot say whether:
- the participant noticed in-event;
- a genuine open edge was recognized;
- a micro-interruption occurred;
- the alternative simply executed from prior planning.

Therefore the central Stage 1 distinction NOTICE ≠ OPEN is methodologically approved but not yet well observed in this corpus.

## N-4 — Mixed-domain intentions damage interpretability

Some reports combine household, health and work actions in one “planned action” field.

This creates false comparability.

The Gate E one-lane architecture is therefore not only cognitively useful; it is also necessary for measurement validity.

## N-5 — Daily self-report can manufacture UPDATE

Most next-position/next-day reflections were elicited in evening review.

The corpus generally cannot distinguish:

~~~text
update existed before review
vs
update was generated by the question
~~~

Gate F's update_timing field is therefore empirically necessary.

---

# 10. Lapse / recovery evidence

Old-route return appears repeatedly.

The most informative structure is not:

~~~text
success → failure
~~~

but:

~~~text
old route present
→ alternative realized in some recurrences
→ old route returns in another context
→ alternative becomes available again later
~~~

This pattern is compatible with the approved boundary:

> old learning may remain retrievable.

However, **Recovery Latency cannot be calculated reliably** because detection and realization timestamps are missing.

Current evidence therefore supports event-level recovery narratives, not latency metrics.

---

# 11. Measurement failures exposed by the corpus

## M-1 — Notice timing is missing

Add a low-burden conditional distinction:
- noticed before;
- during;
- late but something remained open;
- only afterward;
- unknown.

## M-2 — OPEN is under-observed; measuring it may also train it

When a participant reports an urge + changed action, one conditional question is a candidate measurement experiment:

> **Что именно сделало старое продолжение не единственным?**

Possible answer may still be “не знаю.”

## M-3 — Future-reporting salience must be captured

A19 shows this cannot remain invisible in key candidate SP events.

At least for candidate SP events, capture whether later reporting was salient.

## M-4 — Update timing must be captured

Differentiate:
- spontaneous before review;
- elicited during review;
- later;
- unknown.

## M-5 — One lane must be identified

Mixed daily plans make selected→realized analysis ambiguous.

A practice/evidence episode should carry a lane_id or equivalent target label.

## M-6 — Report date and ingestion date must remain separate

External-participant reports were sometimes transferred/imported later.

Ingestion delay is not participant delay.

## M-7 — Manual collection is an operational confound

Owner-mediated copying between group chat, ChatGPT and local store increases:
- missing metadata;
- ingestion delay;
- ambiguity around submission time;
- opportunity for transcription error.

This supports a dedicated collection layer, but does not itself authorize implementation.

---

# 12. Cross-participant interpretation

The three-participant corpus is useful for **cross-case recurrence of distinctions**, not independent replication of efficacy or effect-size estimation.

Across all three participants there is evidence compatible with:
- intention/realization divergence;
- competing impulse not deterministically producing action;
- lane-specific rather than global behavior;
- planning/repetition sometimes making an alternative feel easier.

Only P-A currently provides explicit evidence that questionnaire anticipation altered behavior. P-B and P-C broaden the case set but remain inside the same social/research context and short reporting window.

Therefore:

~~~text
measurement reactivity
= first-class hypothesis / confound

not
universal participant mechanism
~~~

No participant ranking is valid.

No cross-lane ranking is valid.

---

# 13. Automaticity analysis

Evidence potentially relevant to re-automatization is lane-local and source-qualified:
- repeated statements of “easier” or “simpler” action;
- some repeated successful continuations after earlier difficulty;
- substitute choices becoming more accessible in one participant.

But the current corpus lacks:
- no-deliberation execution evidence;
- retrieval latency;
- stable-context repetition count with comparable exposure;
- mismatch after established automatic performance.

Therefore:

**HYPOTHESIS:** some continuations may be becoming lower-load.

**OPEN:** whether any have become genuinely automatic.

**OPEN:** whether mismatch detection can reopen an automated route.

No event is promoted to strong aligned-automatic-performance evidence yet.

---

# 14. Falsification attempts

## Q1 — Could apparent improvement be only better reporting?

**Yes, still possible.**

Self-report dominates and review itself is reactive.

The corpus does not falsify this alternative.

## Q2 — Could better behavior be only prompt/scaffold dependence?

**Possible for some owner episodes.**

A19 explicitly involves anticipatory questionnaire scaffold.

For many other episodes prompt provenance is unknown.

The corpus cannot establish independence.

## Q3 — Does NOTICE alone appear sufficient?

**No evidence supports that claim.**

Some plans/awareness coexist with old-route realization.

This is compatible with the architecture requiring OPEN + REALIZE.

But because NOTICE timing is not captured, this remains indirect evidence.

## Q4 — Is OPEN empirically distinct from NOTICE in the current data?

**Not reliably observable yet.**

This is a measurement failure, not a demonstrated theoretical failure.

## Q5 — Is the new route becoming automatic?

**Not demonstrated.**

Lower-load language exists; automatic execution evidence does not.

## Q6 — Does late entry produce useful recovery?

**Insufficient structured evidence.**

The old questionnaire did not capture late-entry boundaries explicitly.

## Q7 — Does the questionnaire help or distort?

**Both are plausible.**

For P-A it appears to have functioned as a useful scaffold in at least one episode.

The same fact means it also confounds measurement of participant-initiated performance.

---

# 15. Candidate model updates

## U-1 — Make measurement reactivity operational, not just conceptual

**DERIVED.**

For candidate SP events, preserve future-reporting salience and current prompt activation.

No claim that these cause the action.

## U-2 — Enforce one-lane event identity

**DERIVED.**

Every practice/evidence trace should identify the lane being trained/tested.

This prevents “good day” aggregation and mixed-plan contamination.

## U-3 — Add a minimal OPEN discriminator

**HYPOTHESIS.**

A single conditional question may be sufficient, but adding it is itself a **measurement experiment** because the question may train noticing, rationalization or interruption:

> **Что сделало старое продолжение не единственным?**

Possible classes:
- delay/pause;
- context shift;
- reminder;
- prepared alternative;
- support;
- competing action;
- new information;
- cannot identify;
- retrospective hypothesis.

This should be tested for burden **and measurement reactivity** before adoption.

## U-4 — Preserve review-created learning as real but scaffolded

**DERIVED.**

If UPDATE is elicited by the questionnaire, it is still a real learning event.

But it should be labeled elicited_during_review rather than misclassified as spontaneous feedback use.

## U-5 — Do not add an automaticity score

**DERIVED.**

The present evidence is too weak and heterogeneous.

Use event traces plus exploratory lower-load indicators only.

---

# 16. What we still cannot know

From the current evidence we cannot determine:
- how many relevant opportunities were never noticed/reported;
- whether a retrospectively described urge was consciously noticed in-event;
- whether OPEN occurred as a distinct operation in most episodes;
- whether questionnaire anticipation improves skill, only accountability, only memory, or some combination;
- what would happen if the questionnaire were withdrawn;
- whether any continuation is truly automatic;
- whether useful automaticity would remain reopenable under mismatch;
- whether Stage 1 transfers across unrelated domains;
- whether observed changes would occur without Selection Point framing;
- causal effect size of prompts, planning or environment;
- general efficacy beyond these three participants.

---

# 17. Gate G evidence verdict after Red Team

The current 14-record corpus is **methodologically useful but efficacy-insufficient pre-protocol evidence**.

It supports several architecture boundaries:

~~~text
intention ≠ realization
urge ≠ action
one lane ≠ whole person
measurement ≠ neutral observation
old-route return ≠ total reset
lower effort ≠ proven automaticity
~~~

It exposes concrete measurement weaknesses:

~~~text
NOTICE timing under-captured
OPEN under-captured
prompt/reactivity provenance under-captured
update timing under-captured
mixed-lane plans reduce validity
manual ingestion loses metadata
~~~

The corpus does **not** justify:
- efficacy claims;
- mastery claims;
- participant comparison;
- automaticity claims;
- transfer claims;
- Gate H conclusions yet.

Red Team completed; revised packet is ready for Owner review.

Gate H remains closed.


---

# 18. Post-Red-Team binding interpretation

The packet must be read under these constraints:

1. this is a pre-protocol/transitional corpus, not a Gate E efficacy test;
2. event chains are partial reconstructions, not direct recordings of hidden mental sequence;
3. most internal events are participant self-report;
4. P-A owner/designer expectancy is a major confound;
5. P-B/P-C provide cross-case recurrence, not independent efficacy replication;
6. submitted reports are not an unbiased sample of all days/opportunities;
7. planning-related “easier” language is self-reported accessibility, not causal effect;
8. automaticity is not demonstrated, not ruled out;
9. proposed OPEN measurement can itself be reactive;
10. public artifacts remain de-identified; raw participant data stay private;
11. lane-local interpretation remains the default;
12. Gate H remains closed until Owner approval.

**Final Gate G recommendation:** **PASS WITH BINDING BOUNDARIES — READY FOR OWNER REVIEW.**
