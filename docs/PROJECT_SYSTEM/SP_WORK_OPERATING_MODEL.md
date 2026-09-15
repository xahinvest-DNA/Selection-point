# Selection Point Work Operating Model

**ID:** SP-OPS-001  
**Status:** approved  
**Approved:** 15 September 2026  
**Scope:** project operating model for methodology, research, production, technical execution and reality-based validation.

## 1. Purpose

Selection Point separates methodological decisions from research/production work, technical implementation and empirical feedback.

The operating principle is:

```text
Owner
  ↓
Chat — decide WHAT and WHY
  ↓
Work — research, assemble and produce bounded project artifacts
  ↓
Codex — implement approved technical requirements
  ↓
Pilot / Reality — produce consequences and evidence
  ↓
Work — assemble evidence without upgrading its epistemic status
  ↓
Chat — interpret, challenge and run Red Team
  ↓
Owner — approve, reject or revise
```

This mirrors the Selection Point discipline itself: model → continuation → realization → consequence → feedback → model update.

## 2. Roles and authority

### 2.1 Owner — Андрей

Owns project direction and final decisions.

Authority:
- approve or reject methodological decisions;
- open or keep closed project gates;
- approve movement between stages/tasks;
- authorize changes to canon, Product Lab or pilot scope through the relevant governance layer.

An item remains provisional until explicit owner approval such as `утверждаем`.

### 2.2 Chat — Methodological Architect

Primary responsibilities:
- conceptual discussion;
- critical analysis;
- formulation of testable distinctions;
- Red Team;
- protection of canonical boundaries;
- defining what must be learned, observed or tested;
- interpreting evidence without converting uncertainty into a stronger claim.

Chat does not treat production completeness, elegant wording or tool output as evidence that a methodological proposition is correct.

### 2.3 ChatGPT Work — Project / Research Operator

Primary responsibilities:
- read large project context across approved sources;
- collect and structure relevant canon, decisions, examples and evidence;
- identify contradictions, gaps and stale material;
- prepare bounded research packets;
- turn approved methodological decisions into teaching/research/analysis artifacts;
- prepare evidence review packets from pilot material;
- execute multi-step project work that does not require a new methodological decision.

Work may propose but must not silently decide.

Work has no authority to:
- change Selection Point canon;
- declare a hypothesis confirmed;
- declare a participant or the owner to have mastered a stage;
- convert correlation or temporal order into causation;
- treat questionnaire completion or reminder response as proof of Selection Capacity;
- open the next Foundation stage;
- open a Product Lab gate;
- open an external-user pilot;
- promote a Health Lab finding into Product Lab or Foundation without explicit review.

### 2.4 Codex — Technical Executor

Primary responsibilities:
- implement approved software requirements;
- modify repositories within an approved task boundary;
- create parsers, storage, schemas, dashboards, tests, CI and automation;
- verify implementation consistency.

Codex does not define methodological meaning. Terms such as `SelectionPointEvent`, `FeedbackRecord`, stage capability or evidence status must be defined upstream before technical implementation.

### 2.5 Pilot / Reality — Validation Layer

Reality is not an execution agent and has no obligation to validate Selection Point.

Its role is to return:
- actual realization or non-realization;
- consequences;
- unexpected events;
- contradictions;
- missing observability;
- evidence that may weaken, revise or falsify a working model.

Reality outranks explanatory elegance.

## 3. Operating cycle for each Foundation stage

Work on training material proceeds **strictly one approved Foundation stage at a time**. The next stage is not opened by completing educational material for the current one.

### Gate A — Capability definition

In Chat, before designing lessons, define:

> What practically available human capability should exist after this stage that was not sufficiently available before it?

Also define:
- which automatic processes interfere with it;
- what the person must learn to notice;
- what additional internal move becomes available;
- what reality-facing behavior can expose whether the capability is present;
- how the appearance of mastery can be distinguished from actual capability.

Output: **Stage Capability Spec**.

### Gate B — Stage Research Packet

After a working capability definition exists, Work reads the complete approved stage context and assembles:
- canonical propositions;
- relevant decisions and Reality Checks;
- examples and source material;
- contradictions;
- open questions;
- candidate psychological mechanisms;
- evidence boundaries.

Work does not rewrite canon in this step.

Output: **Stage Research Packet**.

### Gate C — Psychological Mechanism Map

The methodological architecture of a stage is not assumed to equal the learning architecture.

For example, N canonical parameters do not imply N lessons.

Work groups the approved content into the minimum coherent set of trainable mechanisms. Chat then reviews whether the grouping preserves the stage's meaning and boundaries.

Output: **Psychological Mechanism Map**.

### Gate D — Learning Units

Each approved mechanism may be turned into a learning unit with the following structure:

```text
what happens
→ why this process may occur
→ how it is experienced from inside
→ how it is commonly misread or rationalized
→ how to recognize it
→ where an additional choice may become available
→ what to try in reality
→ what to observe after realization or non-realization
```

The goal is not intellectual agreement. The unit must return the learner to observable reality.

Output: **Learning Units**.

### Gate E — Practice Protocol

Every practical unit must connect learning to a real event chain rather than finish at insight.

Minimum logic:

```text
noticed
→ distinguished
→ selected a continuation
→ realized / partially realized / consciously did not act / did not realize
→ observed consequence
→ extracted or failed to extract feedback
→ updated or preserved the model
```

Practices should have observable outputs where possible.

Examples of potentially meaningful outputs include:
- an impulse was noticed before action rather than reconstructed only afterwards;
- fact and internal reaction were distinguished in a live event;
- a selected continuation was realized despite a competing automatic sequence;
- a selected-realized gap was observed without moralizing it;
- new reality changed the selected continuation.

Output: **Practice Protocol**.

### Gate F — Observability / Measurement Spec

The measurement layer defines what information is needed to evaluate the training process without making the questionnaire itself part of the claimed capability.

Boundary:

```text
questionnaire = telemetry
questionnaire ≠ Selection Point
measurement adherence ≠ target-domain realization
measurement adherence ≠ Selection Capacity proof
```

Output: **Observability / Measurement Spec**.

### Gate G — Pilot evidence

The approved training material is applied in a real domain. For the current owner self-pilot, the primary training field is body / health / physical efficiency.

The stage remains general; the first field exercises may use:
- sleep;
- nutrition;
- alcohol;
- training;
- recovery;
- fatigue;
- pain/discomfort;
- stress events;
- postponement;
- habitual impulses.

The pilot is not reduced to weight loss or compliance.

Work may assemble observations into an **Evidence Review Packet**, preserving:
- observed facts;
- selected vs realized distinction;
- prompt exposure;
- consequence vs used feedback;
- alternative explanations;
- contradicting cases;
- unknown / not_observed fields.

Output: **Pilot Evidence Packet**.

### Gate H — Stage Review

Chat + Owner review the evidence packet.

The review asks:
- what was actually observed;
- whether the training material appears learnable and usable;
- whether the instrument captured the required distinctions;
- where capability was only verbal or retrospective;
- which mechanisms remain ambiguous;
- what contradicted the working model;
- what should change before another iteration.

Completion of a stage learning package does not by itself open the next Foundation stage.

Output: **Stage Review**.

## 4. Standard stage artifact set

The target artifact chain is:

```text
Stage Capability Spec
        ↓
Stage Research Packet
        ↓
Psychological Mechanism Map
        ↓
Learning Units
        ↓
Practice Protocol
        ↓
Observability / Measurement Spec
        ↓
Pilot Evidence Packet
        ↓
Stage Review
```

Artifacts may be combined physically when useful, but the epistemic distinctions must remain visible.

## 5. Health pilot relationship

The goal `healthy and effective body` is currently a **training and evidence domain**, not the definition of Selection Point.

The project does not teach a diet or an alcohol prohibition as SP itself. Instead it may use body-domain events to expose mechanisms such as:
- automatic interpretation;
- impulse and habitual action;
- fatigue and narrowed option accessibility;
- postponement;
- selected-realized gaps;
- recovery after deviation;
- revision after new facts.

Health-domain observations remain subject to the Health Lab contract and medical-scope boundaries.

## 6. Questionnaire boundary

The questionnaire is a telemetry instrument used to reconstruct or record relevant observations.

Correct relation:

```text
SP training
↓
person lives through real events
↓
selection / automatic process / action / non-action occurs
↓
questionnaire or other capture instrument records evidence
↓
data enters the evidence layer
```

Incorrect relation:

```text
questionnaire completion
→ proof of SP capability
```

## 7. Tool-use boundary

The project chooses the executor based on task type:

- **Chat:** unresolved meaning, tradeoffs, critique, governance and interpretation;
- **Work:** context-heavy research, synthesis, bounded production, audits and evidence packets;
- **Codex:** implementation and repository/software engineering;
- **Pilot / Reality:** empirical contact.

A task should not be delegated to a lower layer when it contains an unresolved higher-layer decision.

## 8. Current next step

**Gate A — Stage 1 Capability Definition is complete and approved as `SP-TR-S1-CAP-001`.**

The currently authorized cycle is:

**Gate B — Stage 1 Research Packet.**

Work must execute the bounded research task defined in:

`docs/TRAINING/STAGE_1_RESEARCH_PACKET_WORK_BRIEF.md`

The expected Work deliverable is:

`docs/TRAINING/STAGE_1_RESEARCH_PACKET.md`

Work may collect, compare, structure and propose candidate mechanism groupings, but it may not approve new methodological meaning. The resulting packet must return to Chat for methodological review and then to Owner for approval before Gate C is opened.

This authorization does not:
- change Foundation Stage 1 canon;
- open Foundation Stage 5;
- open SP-LAB-002;
- open an external-user pilot;
- declare the owner self-pilot effective;
- define numeric Stage 1 transition thresholds;
- validate a trainer or Selection Capacity score.

The next methodological question after Work returns the packet is:

> Which smallest coherent set of trainable psychological mechanisms is actually required to produce the approved Stage 1 capability without collapsing explanation into proof or insight into realized participation?
