# Stage 1 Observability / Measurement

**ID:** SP-TR-S1-OM-001  
**Status:** approved  
**Gate:** F — Observability / Measurement Spec  
**Date:** 19 September 2026  
**Upstream capability:** \`SP-TR-S1-CAP-002\`  
**Upstream Learning Units:** \`SP-TR-S1-LU-001\`  
**Upstream Practice Protocol:** \`SP-TR-S1-PP-001\`  
**Execution contract:** \`SP-TR-S1-OM-SPEC-001\`  
**Red Team:** \`SP-TR-S1-OM-RT-001\`  
**Approval decision:** \`SP-TR-DEC-S1-F-001\`  
**Product Lab compatibility:** \`REALITY_EVENT_MODEL_V0_2.md\`, \`PILOT_METRICS_SPEC_V0_1.md\`  
**Nature:** training-layer observability contract; not a validated psychometric scale, diagnosis or final product schema.

---

# 1. Measurement thesis

Stage 1 cannot be measured by asking only:

> “Did the person make a better choice?”

That collapses several distinct events.

The minimum evidence logic is:

~~~text
DOCUMENTED RELEVANT EVENT / CANDIDATE OPPORTUNITY
→ NOTICING
→ OPEN EDGE / INTERRUPTION
→ SELECTION
→ REALIZATION
→ CONSEQUENCE
→ USED FEEDBACK / UPDATE
~~~

while separately preserving:

~~~text
support provenance
environment configuration
measurement reactivity
rehearsal vs live context
aligned automatic performance
evidence source / capture timing
~~~

The default output is a **trace**, not a score. Normalization never upgrades self-report into objective fact.

---

# 2. Relation to Reality Event Model v0.2

Gate F does not create a competing event model.

It maps Stage 1 observations onto the existing Reality Loop:

~~~text
PositionSnapshot
→ SelectionPointEvent
→ ChoiceRecord
→ RealizationRecord
→ ConsequenceRecord
→ FeedbackRecord
→ ModelUpdateRecord
→ next PositionSnapshot
~~~

Training-layer additions are observational qualifiers around these entities.

## 2.1 Mapping

| Training evidence | Existing Reality Event entity |
|---|---|
| lane / relevant current facts | PositionSnapshot |
| noticing timing / support provenance / open edge | SelectionPointEvent qualifiers |
| selected continuation | ChoiceRecord |
| execution status / prompt exposure | RealizationRecord |
| immediate + delayed consequence | ConsequenceRecord |
| what was noticed from consequence | FeedbackRecord |
| what changed for next recurrence | ModelUpdateRecord |

## 2.2 Non-duplication rule

If the same fact is already represented in the Reality Event Model, Gate F references it rather than inventing a second semantic field.

Gate F only adds fields needed to distinguish Stage 1 training states.

---

# 3. Evidence source and capture provenance

A self-report is evidence of a report, not direct access to hidden mental events.

Every important observation should preserve, where practical:

~~~text
evidence_source:
  participant_self_report
  observer
  system_event
  mixed
  unknown

capture_timing:
  in_event
  immediate_post_event
  same_day_review
  later_reconstruction
  unknown
~~~

These fields do not rank credibility automatically.

They allow later interpretation of recall limitations and measurement reactivity.

## 3.1 No forced reconstruction

If a participant cannot reliably reconstruct timing, support or what was selected:

> record \`unknown\`.

Unknown is better evidence discipline than a plausible story.

## 3.2 Source-lineage rule

Normalization never upgrades epistemic status.

Every normalized field should retain a pointer or lineage to the raw participant report, observer note or system event from which it was derived.

~~~text
structured field
≠
objective fact by default
~~~

---

# 4. Core unit: Documented Relevant Event / Candidate Opportunity

The denominator problem is fundamental.

The system usually cannot know every moment in which a Selection Point “should” have occurred.

Therefore Gate F uses a **documented relevant event / candidate opportunity**, not an inferred total opportunity.

A recurrence is not automatically proof that a meaningful Selection Point was objectively available.

## 4.1 Candidate-opportunity evaluability

~~~text
candidate_opportunity_evaluable:
  yes
  no
  unclear
  unknown
~~~

An open edge is not inferred merely because the lane recurred.

## 4.2 Event status

~~~text
opportunity_status:
  documented_recurrence
  documented_mismatch_without_reentry
  aligned_automatic_performance
  no_relevant_recurrence_reported
  rehearsal_only
  unknown
~~~

### Important boundary

~~~text
no documented opportunity
≠
failed capability
~~~

Likewise:

~~~text
no reported opportunity
≠
proof that no opportunity occurred
~~~

Gate F must not create false denominators from invisible events.

---

# 5. Episode class

Each record receives one descriptive episode class when evaluable:

~~~text
episode_class:
  live_sp_cycle
  live_partial_sp_cycle
  live_old_route_without_reentry
  live_aligned_automatic_performance
  live_aligned_automatic_no_interruption_needed
  rehearsal
  no_relevant_recurrence_reported
  unknown
~~~

## 5.1 Why this matters

A aligned automated response can be a success of training while containing no observable conscious Stage 1 cycle.

Therefore:

~~~text
live_aligned_automatic_performance
≠
live_sp_cycle
~~~

Neither class is automatically “better.”

They answer different questions.

---

# 6. NOTICE observability

Gate F does not attempt to measure “awareness” as a global trait.

It records evidence that a relevant process became distinguishable in the episode.

## 6.1 Noticing evidence

~~~text
noticing_report:
  noticed
  reports_not_noticed
  not_recalled
  not_applicable_aligned_automatic
  unknown
~~~

## 6.2 Noticing timing

When noticing is reported:

~~~text
noticing_timing:
  before_old_route_started
  during_old_route
  late_but_open_edge_remained
  consequence_only
  next_cycle_preparation_only
  timing_unknown
~~~

These are descriptive positions in time, not grades.

Late noticing remains valid Stage 1 evidence if a relevant open edge remained.

## 6.3 Marker recognition

Optional:

~~~text
marker_expected
marker_observed
marker_match:
  match
  partial_match
  non_match
  not_evaluable
~~~

This helps test whether the Lane Card cue is actually retrievable without claiming that the marker caused noticing.

---

# 7. Support provenance

The existing \`prompt_exposure\` field remains binding.

Gate F adds the training distinction:

~~~text
support_provenance:
  A_external_current_prompt
  B_anticipatory_scaffold_linked
  C_participant_initiated
  mixed
  unknown
~~~

This is **not** an ordinal scale.

## 7.1 Suggested mapping to Reality Event Model

Examples:

~~~text
A_external_current_prompt
→ prompt_exposure = plan_recall | trajectory_check | other_scaffold

B_anticipatory_scaffold_linked
→ no immediate prompt, but future reporting/support was salient

C_participant_initiated
→ no identifiable current prompt activation reported
~~~

Important:

~~~text
C_participant_initiated
≠
independent of all prior/environmental/social scaffolding
~~~

## 7.2 Orthogonal support dimensions

Support should not be forced into one mutually exclusive category.

Where relevant, preserve separately:

~~~text
current_prompt_activation:
  yes
  no
  unknown

environment_configuration:
  unchanged
  old_route_access_reduced
  alternative_access_increased
  old_route_physically_unavailable
  other
  unknown

social_support_activation:
  active
  available_not_used
  none_reported
  unknown

future_reporting_salience:
  yes
  no
  unclear
  unknown
~~~

A/B/C remains a compact event-provenance label, but these orthogonal fields preserve overlapping support.

## 7.3 Reactivity flag

When a questionnaire/review is active, one optional low-burden field is allowed:

> **В момент события ты помнил, что потом будешь это фиксировать?**

~~~text
future_reporting_salience:
  yes
  no
  unclear
  unknown
~~~

Optional second field only when necessary:

~~~text
reporting_expectation_changed_behavior:
  yes_reported
  no_reported
  unclear
  unknown
~~~

These remain self-report observations, not causal proof.

---

# 8. OPEN observability

Noticing alone is insufficient.

Gate F must record whether a still-open continuation became usable.

## 8.1 Open-edge evidence

~~~text
open_edge_status:
  identified_and_used
  identified_not_used
  late_edge_identified_and_used
  late_edge_identified_not_used
  no_open_edge_reported
  not_applicable_aligned_automatic
  unknown
~~~

## 8.2 Open-edge identification timing

~~~text
open_edge_identification_timing:
  in_event
  immediate_post_event
  retrospective_hypothesis
  unknown
~~~

A retrospectively hypothesized alternative is not equivalent to evidence that it was available in the live moment.

## 8.3 Interruption result

Where an old route was active:

~~~text
interruption_result:
  old_route_delayed
  old_route_reduced
  old_route_stopped
  context_changed
  access_changed
  competing_action_started
  support_engaged
  information_wait_created
  no_effect_observed
  not_applicable
  unknown
~~~

Multiple values may apply.

## 8.4 Boundary

~~~text
noticed
≠
opened

opened
≠
realized alternative
~~~

The measurement system must preserve all three.

---

# 9. Selection observability

Use the existing \`ChoiceRecord\`.

Required:

~~~text
selected_continuation
selection_timestamp_if_known
selection_basis_optional
~~~

Training layer may additionally note:

~~~text
selection_origin:
  prepared_lane_default
  in_the_moment_revision
  new_fact_revision
  support_suggested_but_participant_selected
  unknown
~~~

The support system must not silently be treated as the chooser.

---

# 10. REALIZE observability

Use existing execution statuses:

~~~text
executed
partially_executed
conscious_non_action
not_executed
circumstances_changed
revised_after_new_fact
forgotten
unknown
~~~

Preserve existing selected → realized relation:

~~~text
match
partial_match
non_match
not_evaluable
~~~

## 10.1 Realization evidence

~~~text
realization_evidence_source:
  participant_self_report
  system_event
  observer
  mixed
  unknown
~~~

Where a system event exists, it should not automatically replace participant context; it only strengthens evidence that an action occurred.

## 10.2 Not-realized is not explained automatically

A \`non_match\` or \`not_executed\` record does not imply:

- weak will;
- sabotage;
- hidden resistance;
- lack of Selection Capacity.

Observed reasons may be recorded only when evidence exists.

---

# 11. Environment contribution

Gate E explicitly allows environment-first design.

Gate F therefore records environmental configuration separately from participant re-entry.

## 11.1 Environment exposure

~~~text
environment_support:
  none_reported
  cue_removed_or_changed
  friction_added_to_old_route
  alternative_made_easier
  access_blocked
  other_person_support
  other
  unknown
~~~

Multiple values may apply.

## 11.2 Environment configuration facts

Avoid counterfactual causal claims.

Prefer directly observable/configuration fields:

~~~text
environment_configuration:
  unchanged
  old_route_physically_unavailable
  old_route_access_reduced
  alternative_access_increased
  support_present
  role_unclear
  unknown
~~~

These describe the action space that existed; they do not claim what the participant would have done in a different environment.

## 11.3 Boundary

~~~text
better continuation under redesigned environment
≠
independent participant re-entry
~~~

Both remain valuable evidence.

---

# 12. CONSEQUENCE observability

Use \`ConsequenceRecord\`.

Gate F distinguishes immediate and delayed windows.

## 12.1 Immediate update

At the end of the live cycle:

~~~text
immediate_position_change
timestamp_observed
source
causal_confidence
~~~

This is enough to close the live practice cycle.

## 12.2 Delayed consequence

Later consequences create additional \`ConsequenceRecord\` entries linked to the same realization when possible.

No fixed delay window is imposed in Gate F.

## 12.3 Boundary

Outcome valence is not capability.

~~~text
desired outcome
≠
proof of Selection Capacity

undesired outcome
≠
proof of incapacity
~~~

---

# 13. FEEDBACK / UPDATE observability

A consequence becomes used feedback only when it changes the working model, next preparation or next continuation.

Use existing \`FeedbackRecord\` and \`ModelUpdateRecord\`.

## 13.1 Update target

Training-layer descriptive classes:

~~~text
update_target:
  no_change
  recognition_marker
  opening_move
  executable_alternative
  environment
  support
  local_anchor
  next_continuation
  direction_revised
  other
  unknown
~~~

## 13.2 Update timing

~~~text
update_timing:
  spontaneous_before_review
  elicited_during_review
  later
  unknown
~~~

An update elicited by the review may still be useful training, but it is not evidence that feedback was independently used before measurement.

## 13.3 Update evidence

~~~text
update_evidence:
  explicit_next_test
  changed_lane_card
  changed_environment
  changed_next_action
  changed_direction_after_new_fact
  verbal_update_only
  none_observed
  unknown
~~~

A verbal insight is recorded honestly but is not automatically counted as behavioral update.

---

# 14. Rehearsal observability

Rehearsal remains separate:

~~~text
practice_context:
  rehearsal
  live
~~~

Optional rehearsal fields:

~~~text
marker_retrieved
opening_move_recalled
alternative_recalled
sequence_completed
~~~

These can inform training design.

They do not substitute for live evidence.

---

# 15. Aligned automatic performance

Gate F must not penalize successful automation.

A live event may be classified:

~~~text
episode_class = live_aligned_automatic_performance
~~~

when:

- the trained/relevant continuation occurred;
- no conscious SP re-entry is identifiable;
- the continuation still fits current reality/local anchor;
- the event is live, not rehearsal.

Optional evidence:

~~~text
deliberation_report:
  none
  minimal
  noticeable
  high
  unknown

retrieval_latency_optional
~~~

These are exploratory proxies, not validated automaticity measures.

## 15.1 Reopenability evidence

If no meaningful mismatch occurs during the observation window:

~~~text
reopenability = not_observed
~~~

Do not infer either rigidity or flexibility from absence of a mismatch event.



The stronger long-term SP target is not automaticity alone but:

> **aligned/useful automaticity + reopenability under meaningful mismatch.**

Gate F may record a separate event when:

~~~text
previously useful automatic route
+
new meaningful mismatch
→ participant re-enters and revises continuation
~~~

This is valuable evidence of flexibility, but no numeric threshold is set.

---

# 16. Lapse / recovery observability

Return of the old route is represented as an event, not a reset.

Use the existing Recovery Latency concept from \`PILOT_METRICS_SPEC_V0_1\`, with one refinement:

recovery begins from **documented detection of a relevant mismatch/deviation**, not from an assumed hidden moment when the person “should” have noticed.

~~~text
recovery_status:
  observed
  censored
  direction_revised
  not_applicable
  unknown
~~~

Possible descriptive data:

~~~text
deviation_detected_at
first_recovery_realization_at
recovery_latency
support_provenance
late_entry_used
~~~

No moral interpretation attaches to latency.

---

# 17. Participant capture surface vs normalized research trace

Gate F separates what the participant is asked from what the research system may normalize.

## 17.1 Minimal participant capture surface

A minimal review surface can be:

~~~text
1. What happened / marker?
2. When did you notice it?
3. Did a prompt or future report come to mind?
4. What was still open?
5. What did you choose?
6. What actually happened?
7. What changed immediately?
8. Is there one next test/change?
~~~

Questions should be conditional and omitted when already known from system/observer evidence.

The learner is **not** required to fill every normalized field.

## 17.2 Normalized research trace

The richer schema below may be derived only when justified, and every normalized value must retain lineage to its raw source and capture timing.

To limit measurement burden, the default Stage 1 live record should be short.

## 17.3 Core research trace

~~~text
lane_id
episode_class

noticing_report
noticing_timing
support_provenance
current_prompt_activation_optional
future_reporting_salience_optional

open_edge_status
open_edge_identification_timing_optional

selected_continuation
execution_status
selected_realized_relation

immediate_position_change

update_target_optional
update_timing_optional
evidence_source
capture_timing
raw_source_reference_optional
~~~

## 17.4 Conditional research fields

Only collect when relevant:

~~~text
future_reporting_salience
reporting_expectation_changed_behavior
environment_support
interruption_result
delayed_consequence
recovery_latency
deliberation_report
marker_match
~~~

## 17.5 Burden rule

> **If a field does not change an important interpretation, do not require it.**

The system should prefer conditional follow-up over a large universal questionnaire.

---

# 18. Minimal longitudinal summaries

Gate F allows transparent summaries that can always be expanded back to episodes.

**Default rule:** summaries are lane-local. Cross-lane aggregation is descriptive only unless comparability is explicitly justified. No participant-to-participant ranking is authorized.

Raw episode count describes data volume/composition only and must never be interpreted as better capacity.

Do not compare rates across lanes as if lane difficulty/exposure were equivalent.

No overall Selection Capacity score is approved.

## S1 — Episode composition

Show counts by:

~~~text
live_sp_cycle
live_partial_sp_cycle
live_old_route_without_reentry
live_aligned_automatic_performance
live_aligned_automatic_no_interruption_needed
rehearsal
unknown
~~~

Interpretation:
- composition, not ranking.

---

## S2 — Noticing timing distribution

Among episodes with evaluable noticing:

~~~text
before_old_route_started
during_old_route
late_but_open_edge_remained
consequence_only
next_cycle_preparation_only
unknown
~~~

Do not interpret “earlier” as universally better.

Noticing timing is descriptive and must not be converted into points or mastery levels.

Earlier may indicate skill improvement in a selected lane, but context and difficulty matter.

---

## S3 — Support provenance distribution

~~~text
A_external_current_prompt
B_anticipatory_scaffold_linked
C_participant_initiated
mixed
unknown
~~~

No causal claim, no mastery ordering, and C does not mean independence from all scaffolding.

---

## S4 — Open-edge utilization

Among documented episodes with a relevant mismatch and evaluable open edge, report descriptive counts:

~~~text
identified_and_used
identified_not_used
late_identified_and_used
late_identified_not_used
unknown
~~~

Do not divide by assumed unseen opportunities.

---

## S5 — Selected → Realized relation

Reuse \`PILOT_METRICS_SPEC_V0_1\`:

~~~text
match
partial_match
non_match
not_evaluable
~~~

If SRCR is calculated, always stratify or expose support/environment context where possible.

---

## S6 — Recovery trace

Show recovery episodes, their descriptive latency and support provenance.

Do not create a universal “good recovery time.”

---

## S7 — Update use

Show whether a consequence led to:

- explicit next test;
- Lane Card change;
- environment change;
- next-action change;
- direction revision;
- verbal-only update;
- no observed update;
- unknown.

This protects the distinction:

~~~text
consequence
≠
used feedback
~~~

---

## S8 — Aligned automatic performance

Show occurrences of aligned automatic performance separately from conscious SP cycles.

Important interpretation:

~~~text
fewer conscious SP events
+
more aligned automatic performance
may be compatible with successful training
~~~

but does not by itself prove robust automaticity or transfer.

---

# 19. What should NOT be calculated yet

Do not calculate:

- “% awareness”;
- “% agency”;
- “% conscious control”;
- “Selection Capacity Score”;
- “automaticity score”;
- “sabotage rate”;
- “independence score”;
- weighted points for A/B/C provenance;
- points for earlier noticing;
- points for desired outcomes.

These would introduce value judgments or construct validity claims not yet earned by evidence.

---

# 20. Coverage capability required before Gate G

Gate F does not define a participant-level numeric readiness threshold.

Before Gate G, the **measurement architecture** must be capable of representing, when they occur:

- live realized SP traces;
- partial/non-realized episodes;
- old-route return and recovery;
- late-entry evidence;
- scaffold/prompt/reporting salience;
- environment-supported performance;
- aligned automatic performance without conscious SP;
- immediate and delayed consequences;
- explicit updates and review-elicited updates;
- unknowns, contradictions and missing evidence.

This is a schema/evidence-packet coverage requirement, not a quota of participant events.

Gate G should not open merely because the available episodes look successful.

---

# 21. Falsification / alternative-explanation matrix

| Apparent improvement | Alternative explanation Gate F must keep visible |
|---|---|
| fewer old-route actions | environment removed opportunities |
| better questionnaire answers | reporting skill / recall improved |
| earlier noticing | questionnaire anticipation increased monitoring |
| more realized alternatives | prompts directly retrieved the response |
| fewer conscious SP events | aligned behavior may have automated |
| better outcomes | external events may explain outcomes |
| more reported SP events | measurement itself may create/surface events |
| stable behavior | lane may not have recurred |
| poor behavior under no prompt | scaffold dependence may remain |
| good behavior with no prompt | participant initiation, prior scaffolding, environment, or established automaticity may each explain it |

Measurement does not resolve all alternatives automatically. It prevents them from disappearing.

---

# 22. Compatibility with external measurement literature

External literature supports caution rather than a specific SP metric.

- Ecological momentary assessment can improve temporal proximity of self-report but still has validity limitations and should be compared with more objective evidence where available (PMID 35719870).
- Digital in-the-moment measurement can itself alter behavior/cognition; a systematic review found small pooled reactivity effects in studied health behaviors, with mixed evidence outside physical activity (PMID 35264084).
- Intention change does not map one-to-one onto behavior change, supporting the project rule that selection/intention and realization remain separate (PMID 16536643; physical-activity meta-analysis PMID 37460164).

These findings support provenance, minimal burden and reality-coupled evidence. They do not validate SP.

---

# 23. Non-inferences

From Stage 1 data alone, do not infer:

- hidden motive;
- personality trait;
- diagnosis;
- stable identity;
- “degree of consciousness”;
- global self-control;
- causal effect of the questionnaire;
- causal effect of SP training without comparative design;
- robust transfer to other domains;
- durable automaticity;
- Stage 2 recurring scenario;
- moral quality of the participant.

---

# 24. Gate F recommendation after Red Team

**Recommendation:** APPROVE WITH BINDING BOUNDARIES — use a trace-first observability architecture layered onto Reality Event Model v0.2.

Core structure:

~~~text
DOCUMENTED RELEVANT EVENT / CANDIDATE OPPORTUNITY
→ NOTICE
→ OPEN
→ SELECT
→ REALIZE
→ CONSEQUENCE
→ UPDATE
~~~

Cross-cutting evidence:

~~~text
source lineage / capture timing
support provenance + orthogonal support dimensions
measurement reactivity
environment configuration
rehearsal vs live
aligned automatic performance
lapse / recovery
~~~

No composite score.

Red Team completed; revised artifact is ready for Owner review.

Gate G remains closed.
