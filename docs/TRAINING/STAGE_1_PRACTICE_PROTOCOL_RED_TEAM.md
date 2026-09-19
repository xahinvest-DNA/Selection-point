# Stage 1 Practice Protocol — Red Team Review

**ID:** SP-TR-S1-PP-RT-001  
**Date:** 19 September 2026  
**Reviewed artifact:** \`SP-TR-S1-PP-001\`  
**Gate:** E — Practice Protocol  
**Status:** red_team_complete_owner_review_required  
**Gate F:** not opened

---

# 1. Review question

Is the proposed practice protocol actually trainable in ordinary life, sufficiently simple under load, and capable of strengthening selective re-entry without creating hypervigilance, reminder dependence, false autonomy or a new rigid automaticity?

---

# 2. Verdict

**PASS WITH REQUIRED REFINEMENTS.**

The two-layer architecture is strong:

~~~text
PREPARE
→ make the future Selection Point easier to retrieve

LIVE
NOTICE → OPEN → REALIZE → UPDATE
~~~

The narrow training-lane design is especially useful because it limits continuous self-monitoring.

However, the current draft still risks excessive preparation load and lacks a clean distinction between rehearsal, supported real-world performance and independent real-world performance.

---

# 3. Main attacks

## RT-PP-01 — PREPARE has too many learner-facing fields

Local anchor + marker + opening move + alternative + scaffold is methodologically clear but can become another analytical worksheet.

If preparation itself is cognitively expensive, the protocol contradicts the low-load objective.

**Required refinement:**

Compress PREPARE into one learner-facing **Lane Card**:

~~~text
WHEN — marker
OPEN — opening move
THEN — executable alternative
WHY — one local anchor, only if needed for relevance
SUPPORT — optional and visibly labeled
~~~

The learner need not memorize field names.

---

## RT-PP-02 — relying only on naturally occurring episodes may make practice unsafe, sparse or too difficult

Real episodes can arrive at peak load before the new sequence has ever been rehearsed.

**Required refinement:**

Add a **safe rehearsal mode** in which the participant practices:

~~~text
marker → opening move → alternative
~~~

outside the high-load event.

Rehearsal is skill preparation, not proof of real-life Selection Point capability.

This distinction must remain explicit.

---

## RT-PP-03 — a prepared if–then response can bypass conscious NOTICE

A successfully trained alternative may eventually trigger automatically.

That is compatible with the long-term goal, but it creates an evidence problem.

**Required refinement:**

If:

~~~text
marker → useful alternative automatically
~~~

occurs without a distinguishable conscious re-entry, record it as **useful automated performance**, not as evidence that a conscious Stage 1 SP cycle occurred.

Do not force extra awareness merely to produce an observable SP event.

---

## RT-PP-04 — “meaningful mismatch” remains too abstract in the live moment

The learner cannot run a philosophical evaluation every time.

**Required refinement:**

The mismatch criterion should be pre-bound to the training lane.

Before practice, specify one concrete local reason the lane matters:

- safety;
- explicit rule/commitment;
- current task;
- known consequence to avoid/limit;
- selected operational direction.

Live practice should not require re-proving the reason.

---

## RT-PP-05 — environment-first can outsource all performance to the environment

Changing cues/friction may solve the behavior without training internal re-entry.

That can be a valid outcome, but it should not be mislabeled Selection Capacity.

**Required refinement:**

Keep two questions separate:

~~~text
Did the environment produce the better continuation?
Did the participant regain participation?
~~~

Both can be useful; they are not the same evidence.

Gate E should allow environment redesign but preserve provenance for Gate F.

---

## RT-PP-06 — the review can become the dominant intervention

Because the Owner already observed questionnaire reactivity, the evening review may train behavior, alter reporting, create social desirability or cause “living for the report.”

**Required refinement:**

The review must be deliberately minimal.

It should capture the chain without requiring an essay.

The protocol should state:

> **Do not add questions merely because more data could be interesting. Every question increases intervention load.**

Final measurement design belongs to Gate F.

---

## RT-PP-07 — practice can reward “catching” more problems and create pathology scanning

A learner may begin searching the day for failures in order to produce practice episodes.

**Required refinement:**

The training lane should be selected in advance.

Outside the lane, no duty exists to scan or interrupt ordinary automaticity.

Unexpected relevant SP events may be used, but the protocol should not reward episode count.

---

## RT-PP-08 — OPEN may be dangerous in skilled motor or time-critical activity

A generic instruction to pause or redirect attention can degrade safe skilled performance, especially while driving, operating equipment, fighting, swimming or performing other time-critical tasks.

**Required refinement:**

Safety rule:

> **Do not deliberately insert introspective interruption into an activity where shifting attention itself creates risk.**

In such cases, practice begins before the activity, after it, or at a safe operational boundary.

---

## RT-PP-09 — one replacement may be too rigid

A preselected alternative can be appropriate in one context and wrong after facts change.

**Required refinement:**

Prepared alternative means:

> default candidate if the relevant facts still hold.

The live protocol preserves a fast veto:

~~~text
new fact invalidates plan
→ revise
~~~

This keeps preparation from becoming blind rule-following.

---

## RT-PP-10 — lapse review can reintroduce causal archaeology

The draft lists candidate explanations after a lapse. A learner may turn them into a post-hoc story.

**Required refinement:**

After lapse, use only **actionable/testable update hypotheses**.

Preferred form:

~~~text
Observed: marker noticed only after action began.
Next test: move cue earlier.

Observed: prepared alternative could not be executed in that location.
Next test: choose an available alternative.
~~~

Avoid:

~~~text
I failed because my hidden need / ego / trauma...
~~~

---

## RT-PP-11 — Mode A/B/C provenance can be mistaken for a linear developmental ladder

A → B → C is intuitively seductive.

But participant-initiated performance may fluctuate with context, and supported performance can remain strategically useful.

**Required refinement:**

Explicitly state:

~~~text
A / B / C = source of support in this event
not
beginner / intermediate / advanced
~~~

No forced scaffold fading is authorized in Gate E.

---

## RT-PP-12 — no explicit criterion for when not to run the full cycle

If the useful response has become automatic, forcing UPDATE after every recurrence recreates monitoring burden.

**Required refinement:**

Introduce a **compression rule**:

~~~text
if useful automatic continuation fits current reality
→ let it run
→ no full SP cycle required

if mismatch appears
→ reopen SP
~~~

Periodic review of automatic performance may exist later, but continuous checking is not part of the live protocol.

---

## RT-PP-13 — UPDATE timing can be ambiguous

Some consequences are immediate; others are delayed. Waiting for a distant outcome can leave the practice episode open indefinitely.

**Required refinement:**

Gate E should allow:

~~~text
UPDATE-1 immediate factual next position
UPDATE-2 later consequence if/when it becomes observable
~~~

The first closes the live cycle. Later information can reopen/update the record.

No fixed delay is prescribed.

---

## RT-PP-14 — real-life protocol alone does not train discrimination between fact and interpretation enough

NOTICE is intentionally minimal, but some learners may label interpretations as facts and then train efficient action on a distorted model.

**Required refinement:**

Lane preparation or review should include one minimal check only when consequential:

> **Что здесь известно, а что я сейчас предполагаю?**

Do not turn it into a universal taxonomy exercise.

---

# 4. Recommended final practice architecture

## Layer 0 — Select one lane

One currently relevant automatic continuation.

No whole-life monitoring.

## Layer 1 — Lane Card

~~~text
WHEN — what marker can I notice?
OPEN — what small move makes the old route non-exclusive?
THEN — what executable alternative will I try if facts still fit?
WHY — what local reality/task/commitment makes this relevant?
SUPPORT — what external scaffold is active, if any?
~~~

## Layer 2 — Optional rehearsal

Safely rehearse:

~~~text
WHEN → OPEN → THEN
~~~

Rehearsal ≠ real-life execution evidence.

## Layer 3 — Live cycle

> **Заметь → открой → сделай → сверься.**

## Layer 4 — Minimal review

Capture only:

~~~text
marker / noticing source
what remained open
selected
realized
immediate next position
later consequence if available
one actionable update
~~~

## Layer 5 — Recurrence

Repeat only when the lane recurs.

Do not manufacture episodes.

Let useful automaticity run when it fits.

Reopen only under meaningful mismatch.

---

# 5. Final Red Team recommendation

**REVISE, THEN OWNER REVIEW.**

Required before Owner review:

1. compress PREPARE into Lane Card;
2. add rehearsal mode and distinguish rehearsal from real-world evidence;
3. add safety/no-introspective-interruption boundary;
4. make review minimal by design;
5. add automatic-performance compression rule;
6. make UPDATE immediate + later consequence capable;
7. preserve A/B/C as event provenance, not developmental levels;
8. convert lapse analysis into testable/actionable updates only;
9. preserve environment-effect vs participant-re-entry distinction;
10. keep Gate F closed.


---

# 6. Post-revision verification

The revised \`SP-TR-S1-PP-001\` incorporates the required refinements:

- PREPARE compressed into the Lane Card;
- safe rehearsal added and separated from real-world evidence;
- unsafe introspective interruption boundary added;
- review minimized by design;
- useful automatic performance is allowed to remain automatic;
- UPDATE split into immediate next position + later consequence;
- A/B/C retained as event provenance, not mastery ranks;
- lapse review constrained to actionable/testable updates;
- environment-produced improvement separated from participant re-entry evidence;
- Gate F remains closed.

**Final Red Team verdict:** **PASS WITH BINDING BOUNDARIES — READY FOR OWNER REVIEW.**
