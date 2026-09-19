# Stage 1 Observability / Measurement

**ID:** SP-TR-S1-OM-001  
**Status:** ready_for_chat_red_team  
**Gate:** F — Observability / Measurement Spec  
**Date:** 19 September 2026  
**Upstream capability:** \`SP-TR-S1-CAP-002\`  
**Upstream Learning Units:** \`SP-TR-S1-LU-001\`  
**Upstream Practice Protocol:** \`SP-TR-S1-PP-001\`  
**Execution contract:** \`SP-TR-S1-OM-SPEC-001\`  
**Product Lab compatibility:** \`REALITY_EVENT_MODEL_V0_2.md\`, \`PILOT_METRICS_SPEC_V0_1.md\`  
**Nature:** training-layer observability contract; not a validated psychometric scale, diagnosis or final product schema.

---

# 1. Measurement thesis

Stage 1 cannot be measured by asking only:

> “Did the person make a better choice?”

That collapses several distinct events.

The minimum evidence logic is:

~~~text
DOCUMENTED OPPORTUNITY
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
environment contribution
measurement reactivity
rehearsal vs live context
useful automated performance
evidence source / capture timing
~~~

The default output is a **trace**, not a score.

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

---

# 4. Core unit: Documented Practice Opportunity

The denominator problem is fundamental.

The system usually cannot know every moment in which a Selection Point “should” have occurred.

Therefore Gate F uses **documented opportunity**, not inferred total opportunity.

## 4.1 Opportunity status

~~~text
opportunity_status:
  documented_recurrence
  documented_mismatch_without_reentry
  useful_automatic_performance
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
  live_useful_automatic_performance
  live_aligned_automatic_no_interruption_needed
  rehearsal
  no_relevant_recurrence_reported
  unknown
~~~

## 5.1 Why this matters

A useful automated response can be a success of training while containing no observable conscious Stage 1 cycle.

Therefore:

~~~text
live_useful_automatic_performance
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
noticing_evidence:
  present
  absent_reported
  not_applicable_useful_automatic
  not_observed
  unknown
~~~

## 6.2 Noticing timing

When \`present\`:

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
→ no identifiable current scaffold activation reported
~~~

## 7.2 Reactivity flag

When a questionnaire/review is active, one optional low-burden field is allowed:

> **В момент события ты помнил, что потом будешь это фиксировать?**

~~~text
future_reporting_salient:
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

## 8.2 Interruption result

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

## 8.3 Boundary

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

Gate F therefore records environmental support separately from internal re-entry.

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

## 11.2 Environment role

Avoid unsupported causal claims.

Prefer:

~~~text
environment_role_report:
  participant_reports_material
  system_condition_was_necessary
  present_but_role_unclear
  no_material_role_reported
  unknown
~~~

The stronger \`system_condition_was_necessary\` label should be used only where objectively defensible, for example when access was technically blocked.

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

## 13.2 Update evidence

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

# 15. Useful automatic performance

Gate F must not penalize successful automation.

A live event may be classified:

~~~text
episode_class = live_useful_automatic_performance
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

The stronger long-term SP target is not automaticity alone but:

> **useful automaticity + reopenability under meaningful mismatch.**

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

# 17. Minimal Event Trace

To limit measurement burden, the default Stage 1 live record should be short.

## 17.1 Core trace

~~~text
lane_id
episode_class

noticing_evidence
noticing_timing
support_provenance

open_edge_status

selected_continuation
execution_status
selected_realized_relation

immediate_position_change

update_target_optional
evidence_source
capture_timing
~~~

## 17.2 Conditional fields

Only collect when relevant:

~~~text
future_reporting_salient
reporting_expectation_changed_behavior
environment_support
interruption_result
delayed_consequence
recovery_latency
deliberation_report
marker_match
~~~

## 17.3 Burden rule

> **If a field does not change an important interpretation, do not require it.**

The system should prefer conditional follow-up over a large universal questionnaire.

---

# 18. Minimal longitudinal summaries

Gate F allows transparent summaries that can always be expanded back to episodes.

No overall Selection Capacity score is approved.

## S1 — Episode composition

Show counts by:

~~~text
live_sp_cycle
live_partial_sp_cycle
live_old_route_without_reentry
live_useful_automatic_performance
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

No causal claim and no mastery ordering.

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

## S8 — Useful automatic performance

Show occurrences of useful automated performance separately from conscious SP cycles.

Important interpretation:

~~~text
fewer conscious SP events
+
more useful automated performance
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

# 20. Candidate readiness evidence for Gate G

Gate F should not define a numeric mastery threshold.

Instead, Stage 1 is ready to move into Gate G evidence assembly when the measurement system can capture a **diverse, interpretable evidence set** rather than only idealized successes.

A useful evidence packet should be capable of containing:

- at least one live realized SP trace;
- supported and/or unsupported live evidence where naturally available;
- at least one non-realized or old-route return episode;
- late-entry evidence where it occurs;
- environment-supported evidence where used;
- immediate consequence and at least some update evidence;
- useful automatic performance if it emerges;
- explicit unknowns and contradictory evidence;
- questionnaire/reactivity provenance.

This is a **coverage requirement for the evidence packet architecture**, not a participant mastery threshold.

Gate G should not open merely because all episodes look successful.

---

# 21. Falsification / alternative-explanation matrix

| Apparent improvement | Alternative explanation Gate F must keep visible |
|---|---|
| fewer old-route actions | environment removed opportunities |
| better questionnaire answers | reporting skill / recall improved |
| earlier noticing | questionnaire anticipation increased monitoring |
| more realized alternatives | prompts directly retrieved the response |
| fewer conscious SP events | useful behavior may have automated |
| better outcomes | external events may explain outcomes |
| more reported SP events | measurement itself may create/surface events |
| stable behavior | lane may not have recurred |
| poor behavior under no prompt | scaffold dependence may remain |
| good behavior with no prompt | participant initiation, environment, or established automaticity may each explain it |

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

# 24. Gate F recommendation before Red Team

**Recommendation:** use a trace-first observability architecture layered onto Reality Event Model v0.2.

Core structure:

~~~text
DOCUMENTED OPPORTUNITY
→ NOTICE
→ OPEN
→ SELECT
→ REALIZE
→ CONSEQUENCE
→ UPDATE
~~~

Cross-cutting evidence:

~~~text
source / capture timing
support provenance
measurement reactivity
environment support
rehearsal vs live
useful automatic performance
lapse / recovery
~~~

No composite score.

Run dedicated Gate F Red Team before Owner review.

Gate G remains closed.
