# Stage 1 Psychological Mechanism Map — Execution Contract

**Artifact ID:** SP-TR-S1-PMM-SPEC-001  
**Gate:** C — Psychological Mechanism Map  
**Status:** active  
**Date:** 15 September 2026  
**Upstream:** `SP-TR-S1-CAP-001`, `SP-TR-S1-RP-001`, `SP-TR-S1-RP-RT-001`, decision `SP-TR-DEC-S1-B-001`

## 1. Purpose

Gate C must identify the smallest defensible set of psychological processes and trainable operations required to explain and train the approved Stage 1 capability without converting the Stage 1 canon into an unfalsifiable causal theory.

Approved capability:

> Человек учится превращать один собственный автоматический эпизод из переживаемой неизбежности в различимый процесс, находить первый реально доступный участок своего участия и фактически менять хотя бы одно дальнейшее продолжение.

Gate C is not a lesson plan, practice protocol, measurement system, trainer design or product implementation.

## 2. Central methodological rule

Do not begin with a target number of mechanisms.

Begin by classifying each candidate item:

```text
phenomenon
→ possible contributing process
→ trainable operation
→ observable expression
→ reality test / weakening condition
```

A canonical parameter does not become a psychological mechanism merely because it has a stable name.

## 3. Required classification dimensions

Every retained candidate must be evaluated through this matrix:

| Dimension | Required question |
|---|---|
| Phenomenon | What is actually experienced, reported or observed? |
| Candidate mechanism/process | What process could contribute to the phenomenon? |
| Epistemic status | APPROVED description, DERIVED relation, HYPOTHESIS, or OPEN? |
| Trainable operation | What operation must become more available to the learner? |
| Observability | What behavior/event would indicate that operation occurred? |
| Competing explanation | What else could explain the same episode? |
| Falsifier / weakening condition | What would reduce confidence in the proposed relation? |
| Stage boundary | Does the item require Stage 2–4 capability? |
| Support boundary | Can a prompt/AI produce the answer instead of the learner? |
| RC-018 check | Is selected continuation being confused with realized continuation or feedback? |

## 4. Mandatory source set

Gate C must use at minimum:

- `docs/TRAINING/STAGE_1_CAPABILITY_SPEC.md`;
- `docs/TRAINING/STAGE_1_RESEARCH_PACKET.md`;
- `docs/TRAINING/STAGE_1_RESEARCH_PACKET_RED_TEAM.md`;
- `docs/TRAINING/DECISION_STAGE_1_GATE_B_APPROVED_2026-09-15.md`;
- `docs/FOUNDATION/CANONICAL/02_STAGE_1_CANONICAL.md`;
- `docs/FOUNDATION/CANONICAL/03_STAGE_1_P11_CANONICAL.md`;
- `docs/FOUNDATION/CANONICAL/04_STAGE_1_P12_CANONICAL.md`;
- `docs/FOUNDATION/CANONICAL/05_STAGE_1_P13_CANONICAL.md`;
- `docs/FOUNDATION/CANONICAL/01_HUMAN_CHANGE_MODEL_CANONICAL.md`;
- `docs/FOUNDATION/CANONICAL/01B_CORE_CHOICE_ACTION_FEEDBACK_BOUNDARY_CANONICAL.md`;
- relevant Stage 1 full-theory files;
- `docs/FOUNDATION/LIBRARIES/RISKS_AND_BOUNDARIES.md`;
- `docs/FOUNDATION/LIBRARIES/EVIDENCE_MAP.md`;
- `docs/FOUNDATION/LIBRARIES/EXAMPLE_LIBRARY.md`.

## 5. Binding Red Team constraints

### C1 — no tautological mechanism

Do not explain “the person experiences the links as fused” by inventing a hidden entity called `fusion` unless independent explanatory content is added.

Keep distinct:

```text
experienced closure
≠ named causal mechanism
```

### C2 — operational task stays hypothetical

The functional question “what did this action solve or obtain now?” is useful.

But the answer must allow:

- unknown;
- several competing functions;
- objective necessity;
- physiological need;
- habit;
- skill/resource deficit;
- evidence against the first interpretation.

No hidden motive is required for successful Stage 1 reconstruction.

### C3 — mechanism vs capability

Do not define the Stage 1 capability itself as the mechanism that causes the capability.

Separate:

```text
what organizes / narrows the automatic episode
from
what operation the learner develops to regain participation
```

### C4 — RC-018 is a verification layer

Keep distinct:

```text
selected continuation
≠ realized continuation
≠ consequence
≠ used feedback
```

RC-018 surrounds the mechanism map as an empirical discipline. It is not automatically another psychological mechanism.

### C5 — transition and anti-trap material

P12 and P13 primarily specify readiness/learning-quality boundaries unless a narrower process is independently justified.

### C6 — body is cross-cutting

P09 does not authorize a universal bodily marker or a special “body mechanism.” Specific causal body claims require separate evidence.

### C7 — do not import later-stage competence

Stage 1 may use immediate next-position consequences but must not require:

- recurring-scenario detection from Stage 2;
- mature self-model restructuring from Stage 3;
- stable multi-timeframe trajectory reading under load from Stage 4.

### C8 — participant must produce substantive content

A system/AI may:

- preserve sequence;
- ask discriminating questions;
- show competing hypotheses;
- point out missing observations.

It may not:

- assign the participant's hidden motive as fact;
- construct the whole episode and count agreement as skill;
- decide psychological availability on the participant's behalf;
- count a selected move as executed.

### C9 — availability is evidence-sensitive and partly uncertain

For a proposed alternative continuation distinguish:

```text
objectively possible
noticed
known / understood
psychologically available
resource-supported
actually executable
actually realized
```

Retrospective availability may remain `unknown`.

### C10 — map must be able to lose

Every explanatory candidate must preserve at least one competing explanation and one condition that would weaken it.

## 6. Expected artifact structure

The Gate C artifact should contain:

1. **Map thesis** — what the map explains and what it does not.
2. **Category architecture** — explicit distinction between phenomena, candidate processes, trainable operations and safeguards.
3. **Candidate process map** — minimal process set, with epistemic status.
4. **Trainable operation map** — operations required for the Stage 1 capability.
5. **Relationship map** — how processes and operations interact without asserting unsupported causality.
6. **Competing explanations / falsifiers** — per retained mechanism/process.
7. **Observability hooks** — what later Gate F could potentially observe; no thresholds yet.
8. **Stage-boundary audit** — proof that Stage 2–4 capability has not been smuggled into Stage 1.
9. **AI/support boundary** — what participant must do versus what scaffolding may do.
10. **Unresolved questions** — explicit OPEN items.
11. **Red Team section** — strongest attacks against the proposed final map.
12. **Gate C verdict recommendation** — approve / revise / reject; Owner approval required to close Gate C.

## 7. Candidate starting families — not approved mechanisms

Gate C may examine, but must not assume, candidate contributors such as:

```text
state-dependent attentional weighting
perceived-model certainty / appraisal closure
self-image or role constraint
local functional priority
habitual response availability
objective/resource constraints
```

And candidate trainable operations such as:

```text
episode localization
fact / interpretation / state distinction
functional hypothesis formation without overclaiming
realistic availability discrimination
selection of one continuation
realization / execution discrimination
consequence noticing
feedback incorporation
```

These are starting hypotheses only. Gate C may merge, split, rename or reject them.

## 8. Explicit non-goals

Gate C must not produce:

- finished exercises;
- lesson sequence;
- course copy;
- prompts for the final trainer;
- validated metrics;
- transition thresholds;
- personality typology;
- clinical diagnosis;
- universal causal claims;
- a composite Selection Capacity score;
- software implementation.

## 9. Completion criterion

Gate C is ready for Owner review only when:

- every retained mechanism/process has a clear epistemic status;
- mechanism and trainable operation are not circularly defined;
- competing explanations remain visible;
- the map can be contradicted by reality;
- P11/P12/P13 and RC-018 are placed in the correct architectural role;
- Stage 2–4 abilities have not been imported;
- support/scaffold boundaries are explicit;
- the map remains sufficient to explain what needs to be trained for `SP-TR-S1-CAP-001`.

Until explicit Owner approval, Gate D remains closed.