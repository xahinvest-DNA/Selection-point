# Stage 1 Pilot Evidence Packet — Red Team Review

**ID:** SP-TR-S1-PEP-RT-001  
**Date:** 20 September 2026  
**Reviewed artifact:** SP-TR-S1-PEP-001  
**Gate:** G — Pilot Evidence Packet  
**Status:** red_team_complete_revision_required  
**Gate H:** not opened

---

# 1. Review question

Does the evidence packet make only claims that the 14-record, three-participant corpus can actually support, while preserving privacy, source limitations, measurement reactivity and the fact that most data predate the approved Stage 1 Practice Protocol?

# 2. Verdict

**PASS WITH REQUIRED REFRAMING.**

The packet is useful as a methodological stress test and contains meaningful contradictory evidence.

Its main risk is temporal overreach: the corpus is largely **pre-protocol evidence**. It can test distinctions and expose measurement failures, but it cannot validate the finalized Gate E training protocol.

---

# 3. Main attacks

## RT-PEP-01 — Pre-protocol corpus cannot validate the approved protocol

Most observations were collected before Lane Card, safe rehearsal, explicit OPEN practice and the final Gate F trace existed.

**Required refinement:**

Label the corpus explicitly:

> **pre-protocol / transitional compatibility evidence**

It may support or contradict architecture assumptions, but not demonstrate Gate E efficacy.

---

## RT-PEP-02 — Event reconstructions are analyst-derived

The raw questionnaire did not contain the final NOTICE / OPEN / REALIZE / UPDATE fields.

Mapping older reports into this architecture is retrospective normalization.

**Required refinement:**

Each reconstructed event must distinguish:
- direct source fact;
- derived mapping;
- unknown/unobserved link.

Do not write a complete-looking chain when intermediate links were not observed.

---

## RT-PEP-03 — “Old route” can become an interpretive label

Repeated behavior is not automatically an established automatic route.

**Required refinement:**

Use “reported prior/repeated route” only where source history supports repetition.

Otherwise use neutral wording such as “competing continuation” or “non-planned continuation.”

---

## RT-PEP-04 — Self-report dominates the corpus

Urges, noticing, planning and action are mostly self-reported.

There is little independent or system evidence.

**Required refinement:**

State explicitly that the strongest claims are about:
- reported intentions;
- reported realizations;
- reported discrepancies;
- reported questionnaire salience.

Do not imply direct observation of internal events.

---

## RT-PEP-05 — Owner/designer expectancy is a major confound

P-A is also the project Owner and is deeply familiar with the Selection Point model.

This can affect:
- what is noticed;
- how events are narrated;
- compliance;
- interpretation;
- questionnaire reactivity.

**Required refinement:**

Treat owner self-pilot as high-value design evidence but weak independent efficacy evidence.

---

## RT-PEP-06 — External participants do not remove demand/social effects

P-B and P-C broaden the corpus but still participate in a shared social/research context.

Their short reporting window cannot establish independent replication.

**Required refinement:**

Call this **cross-case recurrence of distinctions**, not replication of efficacy.

---

## RT-PEP-07 — Missing-day / reporting-selection bias is not addressed enough

Only submitted reports are analyzed.

A missing report could correlate with:
- difficult day;
- low motivation;
- forgetting;
- collection friction;
- unrelated circumstances.

**Required refinement:**

Do not treat the submitted corpus as an unbiased sample of all days/opportunities.

Preserve measurement adherence separately.

---

## RT-PEP-08 — Measurement reactivity evidence is strong for existence, weak for mechanism

P-A directly reports future reporting changed behavior.

That supports the proposition:

> questionnaire exposure can be behaviorally active in this participant.

It does not establish:
- prospective-memory mechanism;
- skill internalization;
- accountability mechanism;
- generality.

**Required refinement:** keep mechanism OPEN.

---

## RT-PEP-09 — “Planning appears helpful” may partly be demand language

Participants know they are being asked about plans.

Reports such as “planning makes it easier” may reflect genuine experience, questionnaire framing or both.

**Required refinement:**

Keep as self-reported accessibility, not intervention effect.

---

## RT-PEP-10 — The corpus cannot distinguish absence of automaticity from failure to measure it

No strong aligned-automatic-performance event was identified.

But the questionnaire is designed to elicit consciously reportable events.

Automatic actions may be underreported precisely because they require less attention.

**Required refinement:**

State:

~~~text
automaticity = not demonstrated
not
automaticity = absent
~~~

---

## RT-PEP-11 — OPEN question may itself become a new intervention

Adding “what made the old continuation non-exclusive?” could improve noticing or rationalization.

**Required refinement:**

Treat the proposed OPEN discriminator as a measurement experiment whose reactivity/burden must be tested, not a neutral field.

---

## RT-PEP-12 — Cross-lane narrative can still imply global progress

Even without a score, prose such as “becoming easier” can be read as stage advancement.

**Required refinement:**

Keep every longitudinal interpretation lane-local and source-qualified.

---

## RT-PEP-13 — Manual transfer creates source-lineage risk

External reports passed through the Owner before ingestion.

Potential issues:
- transcription;
- date ambiguity;
- omitted metadata;
- normalization choices.

**Required refinement:**

Future collector must preserve raw participant submission and ingestion separately.

For the current corpus, mark submission time as unavailable where unavailable.

---

## RT-PEP-14 — Privacy boundary must be stronger than pseudonymization

Dates + distinctive behavior can re-identify a person in a small social group.

**Required refinement:**

Public artifact should contain only de-identified derived structures. Do not add raw quotes, exact body metrics, exact quantities or names.

The current packet follows this direction; preserve it.

---

# 4. What survives Red Team

The following conclusions survive with careful wording:

1. **Reported intention and reported realization diverge repeatedly.**
2. **Different lanes can diverge within the same participant/day.**
3. **Reported urge does not deterministically predict reported action.**
4. **Future questionnaire reporting was behaviorally salient for P-A in at least one explicit episode.**
5. **Current legacy questionnaires under-observe NOTICE timing and OPEN.**
6. **Mixed-domain planning fields damage interpretability.**
7. **Current evidence does not demonstrate stable re-automatization or reopenability.**
8. **No composite score is warranted.**

---

# 5. Required packet revisions

Before Owner review:

1. label corpus pre-protocol/transitional;
2. add evidence-status legend: SELF-REPORT / DERIVED / OPEN / CONTRADICTION;
3. state that event chains are partial reconstructions;
4. qualify owner evidence for expectancy/design involvement;
5. state submitted reports are not an unbiased sample of all opportunities/days;
6. downgrade “planning helpful” to reported accessibility;
7. clarify automaticity not-demonstrated ≠ absent;
8. mark proposed OPEN question as reactive measurement experiment;
9. preserve lane-local interpretation;
10. retain public de-identification;
11. distinguish cross-case recurrence from efficacy replication;
12. keep Gate H closed.

# 6. Final recommendation before revision

**REVISE, THEN OWNER REVIEW.**

Gate G can become a sound evidence packet if it is framed as a **pre-protocol reality stress test**, not a pilot efficacy result.
