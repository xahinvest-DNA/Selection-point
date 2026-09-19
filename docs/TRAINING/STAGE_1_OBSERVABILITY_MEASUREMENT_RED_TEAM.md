# Stage 1 Observability / Measurement — Red Team Review

**ID:** SP-TR-S1-OM-RT-001  
**Date:** 19 September 2026  
**Reviewed artifact:** SP-TR-S1-OM-001  
**Gate:** F — Observability / Measurement  
**Status:** red_team_complete_owner_review_required  
**Gate G:** not opened

# 1. Review question

Can the proposed observability architecture distinguish Stage 1 participation from reporting, prompting, environment effects and useful automatic performance without inventing invisible denominators, creating a pseudo-psychometric score, or making the measurement system itself heavier than the skill?

# 2. Verdict

**PASS WITH REQUIRED REFINEMENTS.**

The trace-first approach is methodologically stronger than a composite score and is compatible with the existing Reality Event Model.

The strongest parts are:

- separation of noticing, opening, selection, realization, consequence and update;
- explicit support provenance;
- rehearsal/live separation;
- automatic performance represented separately from conscious SP cycles;
- unknown accepted rather than reconstructed;
- no invisible total-opportunity denominator.

However, several fields still risk overclaiming or becoming too burdensome.

# 3. Main attacks

## RT-OM-01 — “Documented opportunity” can still imply that the system knows an opportunity existed

A reported recurrence does not prove that a meaningful Selection Point was objectively available.

**Required refinement:** use **documented relevant event / candidate opportunity** and preserve:

~~~text
candidate_opportunity_evaluable:
  yes
  no
  unclear
  unknown
~~~

Do not infer an open edge until open-edge evidence exists.

## RT-OM-02 — reported absence of noticing is retrospective

A participant saying later “I did not notice” is evidence of retrospective report, not proof of no noticing.

**Required refinement:** noticing evidence must always be interpreted with evidence_source and capture_timing.

Prefer:

~~~text
noticing_report:
  noticed
  reports_not_noticed
  not_recalled
  not_applicable
  unknown
~~~

## RT-OM-03 — Mode C is not “independent capacity”

No immediate prompt may be present while the environment, prior training, social commitment, questionnaire expectancy or Lane Card still shapes behavior.

**Required refinement:**

~~~text
C_participant_initiated
= no identifiable current prompt activation
≠ independent of all scaffolding
~~~

Never use C as a synonym for independent capability.

## RT-OM-04 — “useful automatic performance” is evaluative too early

An automatic response may match the local anchor but later prove ineffective or inappropriate.

**Required refinement:** at event capture use:

~~~text
live_aligned_automatic_performance
~~~

meaning that the automatic continuation appears aligned with the current local anchor / facts at capture time.

“Useful” may be a later interpretation after consequence/update.

## RT-OM-05 — environment-role counterfactuals overclaim

Even if access was blocked, the system usually cannot know what the participant would have done without it.

**Required refinement:** replace counterfactual role claims with directly observable facts:

~~~text
old_route_physically_unavailable
old_route_access_reduced
alternative_access_increased
support_present
role_unclear
~~~

## RT-OM-06 — the research trace is too large for a participant-facing questionnaire

The richer schema is acceptable as backend/research normalization but not as a mandatory learner form.

**Required refinement:** separate:

~~~text
CAPTURE SURFACE
minimal participant questions

RESEARCH TRACE
normalized event fields derived only where justified
~~~

Gate F defines semantics, not a requirement that the learner manually fill every field.

## RT-OM-07 — counts across lanes can reward easy lanes and punish difficult lanes

Ten easy phone-use episodes cannot be compared naively with two high-load conflict or alcohol episodes.

**Required refinement:** longitudinal summaries are lane-local by default. Cross-lane aggregation is descriptive only unless comparability is justified. No participant ranking is authorized.

## RT-OM-08 — episode counts can reward hypervigilance

A participant who reports more events may appear to have more capacity.

**Required refinement:** raw episode count is data volume/composition only, never a performance score.

## RT-OM-09 — noticing timing can become a hidden score

“Before route started” looks intuitively better than “late edge,” but late detection may be exactly the available Stage 1 move.

**Required refinement:** timing remains descriptive. No points or ordinal mastery mapping.

## RT-OM-10 — open-edge status can be reconstructed after the fact

After an episode, participants may invent an alternative that was not actually available in the moment.

**Required refinement:** distinguish:

~~~text
open_edge_identification_timing:
  in_event
  immediate_post_event
  retrospective_hypothesis
  unknown
~~~

Retrospective alternatives remain hypotheses.

## RT-OM-11 — review can manufacture the update it claims to measure

If the questionnaire asks “what did you learn?”, the update may be created during measurement.

**Required refinement:** preserve:

~~~text
update_timing:
  spontaneous_before_review
  elicited_during_review
  later
  unknown
~~~

An elicited update may be useful training but is not evidence that feedback was independently used before measurement.

## RT-OM-12 — Gate G readiness accidentally becomes a hidden threshold

Any fixed “at least one of each” list can become a participant-level quota.

**Required refinement:** Gate F should specify **schema coverage capability**, not fixed participant evidence counts. The system must be able to represent success, non-realization, late entry, scaffold effects, automatic aligned performance, unknowns and contradictions when they occur.

## RT-OM-13 — reopenability has its own denominator problem

If no meaningful mismatch occurs during observation, lack of reopenability evidence does not show rigidity.

**Required refinement:**

~~~text
no mismatch observed
→ reopenability = not_observed
~~~

## RT-OM-14 — support dimensions overlap

A visible reminder is environment and prompt; another person can be background support or an active prompt.

**Required refinement:** use orthogonal dimensions:

~~~text
current_prompt_activation
environment_configuration
social_support_activation
future_reporting_salience
~~~

Do not force one mutually exclusive support type.

## RT-OM-15 — structured normalization does not make self-report objective

Normalizing a participant report into a field does not increase its epistemic status.

**Required refinement:** every normalized field retains source lineage to raw self-report, observer evidence or system event.

# 4. Recommended minimal measurement architecture

## 4.1 Participant capture surface

Keep the live/review surface minimal, for example:

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

Questions should be conditional and omitted when already known from system evidence.

## 4.2 Normalized research trace

The richer fields from SP-TR-S1-OM-001 may remain if source lineage is preserved, unknown is allowed and retrospective inference is labeled.

# 5. Minimal longitudinal reporting after attack

Default reporting should be lane-local and show:

- event composition;
- noticing timing;
- prompt / anticipatory-reporting provenance;
- open-edge use;
- selected → realized relation;
- consequence/update traces;
- recovery after old-route return;
- aligned automatic-performance events;
- evidence gaps / unknowns.

Do not produce rank, score, awareness percentage or cross-lane performance index.

# 6. Final Red Team recommendation

**REVISE, THEN OWNER REVIEW.**

Required before Owner review:

1. rename opportunity language to candidate/documented relevant event;
2. reframe noticing absence as retrospective report;
3. state C ≠ independence from all scaffolding;
4. rename useful automatic event to aligned automatic performance at capture;
5. remove counterfactual environment-role claims;
6. separate participant capture surface from normalized research trace;
7. make summaries lane-local by default;
8. prevent episode count / noticing timing from becoming hidden scores;
9. label retrospective open-edge reconstruction;
10. preserve update timing relative to review;
11. convert Gate G readiness from participant quota to schema coverage capability;
12. set reopenability to not_observed when no mismatch occurs;
13. make support dimensions orthogonal;
14. preserve raw-source lineage;
15. keep Gate G closed.

---

# 7. Post-revision verification

The revised SP-TR-S1-OM-001 incorporates the required refinements:

- opportunity language is candidate/documented rather than assumed;
- reported absence of noticing remains source-bound retrospective evidence;
- C participant-initiated is explicitly not independence from all scaffolding;
- automatic events are captured as aligned automatic performance, not prematurely “useful” fact;
- counterfactual environment-role claims were removed;
- participant capture surface is separated from normalized research trace;
- longitudinal summaries are lane-local by default;
- episode count and noticing timing are explicitly non-scoring;
- retrospective open-edge reconstruction is labeled;
- update timing relative to review is preserved;
- Gate G readiness is schema coverage capability, not participant quota;
- reopenability is not-observed when no mismatch occurs;
- support dimensions are orthogonalized;
- raw-source lineage is preserved;
- Gate G remains closed.

**Final Red Team verdict:** **PASS WITH BINDING BOUNDARIES — READY FOR OWNER REVIEW.**
