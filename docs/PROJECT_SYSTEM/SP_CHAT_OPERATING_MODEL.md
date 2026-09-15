# Selection Point Chat Operating Model

**ID:** SP-OPS-002  
**Status:** approved  
**Approved:** 15 September 2026  
**Supersedes:** SP-OPS-001  
**Scope:** project operating model for methodology, research, synthesis, artifact production, technical execution and reality-based validation without dependency on ChatGPT Work.

## 1. Purpose

Selection Point must remain operable without a separate execution mode whose usage limits can block the project.

The project therefore uses one persistent Chat as both:
- methodological architect;
- research / synthesis / project operator for all non-technical work.

The separation that matters is **epistemic and governance separation**, not product-mode separation.

The operating principle is:

```text
Owner
  ↓
Chat — methodology + research + synthesis + bounded artifact production
  ↓
Codex — only when approved technical implementation is required
  ↓
Pilot / Reality — actual realization, consequences, contradictions, evidence
  ↓
Chat — evidence assembly + interpretation + Red Team
  ↓
Owner — approve, reject or revise
```

There is no required handoff to ChatGPT Work.

## 2. Roles and authority

### 2.1 Owner — Андрей

Owns project direction and final decisions.

Authority:
- approve or reject methodological decisions;
- open or keep closed project gates;
- approve movement between stages/tasks;
- authorize changes to canon, Product Lab or pilot scope through the relevant governance layer.

An item remains provisional until explicit owner approval such as `утверждаем`, unless it is a purely mechanical repository synchronization that does not change meaning.

### 2.2 Chat — Methodological Architect + Project Operator

Chat owns all non-technical project work that does not require a separate software implementation environment.

Responsibilities:
- conceptual discussion and methodological architecture;
- critical analysis and Red Team;
- repository/context reconstruction from SSOT;
- research across approved project sources;
- external research when materially useful;
- synthesis, comparison and contradiction mapping;
- preparation of research packets;
- preparation of learning/research/analysis artifacts;
- evidence assembly and review packets;
- repository audits and synchronization;
- bounded document changes through available repository tools;
- formulation of technical requirements before Codex handoff;
- interpretation of evidence without upgrading uncertainty into stronger claims.

Chat may propose but may not silently approve its own methodological proposal on behalf of Owner.

Chat has no authority to:
- change approved Selection Point canon without Owner approval through the relevant governance process;
- declare a hypothesis confirmed merely because it is coherent;
- declare a participant or Owner to have mastered a stage without the required evidence/review;
- convert correlation or temporal order into causation;
- treat questionnaire completion or reminder response as proof of Selection Capacity;
- open the next Foundation stage, Product Lab gate or external-user pilot without Owner authorization;
- promote Health Lab findings into Product Lab or Foundation without explicit review.

### 2.3 Codex — Technical Executor

Codex is optional and is used only when actual software/repository engineering requires a coding execution environment beyond ordinary bounded repository editing.

Responsibilities:
- implement approved software requirements;
- create or modify application code, schemas, parsers, storage, dashboards, tests, CI and automation;
- verify implementation consistency against an approved technical brief.

Codex does not define methodological meaning. Terms such as `SelectionPointEvent`, `FeedbackRecord`, stage capability or evidence status must be defined upstream in Chat before implementation.

### 2.4 Pilot / Reality — Validation Layer

Reality is not an execution agent and has no obligation to validate Selection Point.

Its role is to return:
- actual realization or non-realization;
- consequences;
- unexpected events;
- contradictions;
- missing observability;
- evidence that may weaken, revise or falsify a working model.

Reality outranks explanatory elegance.

## 3. Epistemic separation inside one Chat

Because research, synthesis and methodological review now occur in the same Chat, the project must preserve explicit epistemic labels rather than relying on separate product modes.

Use these labels where material:

- **APPROVED** — explicit approved project meaning;
- **DERIVED** — conservative synthesis directly implied by approved material;
- **HYPOTHESIS** — candidate explanation/grouping requiring review or evidence;
- **OPEN** — unresolved question;
- **CONTRADICTION** — tension that cannot safely be smoothed over;
- **ILLUSTRATION** — example that explains but does not prove;
- **OBSERVED** — directly recorded fact/behavior;
- **SELF-REPORT** — participant account;
- **INTERPRETATION** — project or analyst reading of evidence.

A change of label requires an explicit reason and, where it changes methodology, Owner approval.

## 4. Gate discipline without mode handoff

The absence of Work does not remove gates.

The project still proceeds one approved Foundation stage at a time:

```text
Gate A — Stage Capability Spec
Gate B — Stage Research Packet
Gate C — Psychological Mechanism Map
Gate D — Learning Units
Gate E — Practice Protocol
Gate F — Observability / Measurement Spec
Gate G — Pilot Evidence Packet
Gate H — Stage Review
```

Each gate must have an explicit status in SSOT. Chat must not silently move to the next gate merely because it can continue working in the same conversation.

## 5. Gate responsibilities

### Gate A — Capability definition

Chat + Owner define what practically available human capability should exist after the stage.

Output: **Stage Capability Spec**.

### Gate B — Stage Research Packet

Chat reconstructs the complete approved stage context and assembles:
- canonical propositions;
- relevant decisions and Reality Checks;
- examples and source material;
- contradictions;
- open questions;
- candidate psychological mechanisms;
- evidence boundaries.

Chat does not rewrite canon in this step.

Output: **Stage Research Packet**.

### Gate C — Psychological Mechanism Map

Chat proposes the minimum coherent set of trainable mechanisms and runs Red Team against the proposal. Owner approval is required before the map becomes approved methodology.

Output: **Psychological Mechanism Map**.

### Gate D — Learning Units

Chat turns approved mechanisms into learning units while preserving evidence boundaries and returning each unit to reality-facing action.

Output: **Learning Units**.

### Gate E — Practice Protocol

Every practice must connect learning to a real event chain:

```text
noticed
→ distinguished
→ selected continuation
→ realized / partially realized / consciously did not act / did not realize
→ consequence
→ noticed / interpreted data
→ feedback used or not used
→ model preserved or updated
```

Output: **Practice Protocol**.

### Gate F — Observability / Measurement Spec

Chat defines what information is required to evaluate the training process while preserving:

```text
questionnaire = telemetry
questionnaire ≠ Selection Point
measurement adherence ≠ target-domain realization
measurement adherence ≠ Selection Capacity proof
```

Output: **Observability / Measurement Spec**.

### Gate G — Pilot evidence

Reality produces events and consequences. Chat assembles the evidence packet while preserving:
- facts vs self-report vs interpretation;
- selected vs realized continuation;
- prompt exposure;
- consequence vs used feedback;
- alternative explanations;
- contradicting cases;
- unknown / not_observed fields.

Output: **Pilot Evidence Packet**.

### Gate H — Stage Review

Chat performs interpretation and Red Team; Owner approves, rejects or revises the stage package.

Completion of the educational package does not itself open the next Foundation stage.

Output: **Stage Review**.

## 6. Tool-use boundary

Tool choice is implementation detail, not a project authority layer.

- **Chat + repository/web/file tools:** default for methodology, research, synthesis, audits, documents, evidence packets and bounded repository edits.
- **Codex:** only for approved technical/software implementation that materially benefits from a coding execution environment.
- **Pilot / Reality:** empirical contact.

No project step may depend on access to ChatGPT Work.

If a tool is unavailable or rate-limited, the project should continue using the ordinary Chat and repository SSOT unless the task itself is technically impossible without that tool.

## 7. Continuity across chats

Durable state lives in the repository, not in a specific conversation or mode.

A new Chat reconstructs context from:
1. `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`;
2. the current recovery checkpoint;
3. `docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md`;
4. this operating model;
5. task-specific SSOT.

Long tasks may be split across chats by committing intermediate artifacts/status to the repository. No separate Work handoff is required.

## 8. Current authorization

**Gate A — Stage 1 Capability Definition is approved as `SP-TR-S1-CAP-001`.**

The currently authorized training cycle is:

**Gate B — Stage 1 Research Packet.**

Gate B is executed directly in Chat under:

`docs/TRAINING/STAGE_1_RESEARCH_PACKET_SPEC.md`

Expected deliverable:

`docs/TRAINING/STAGE_1_RESEARCH_PACKET.md`

Gate C remains closed until Gate B receives methodological review and Owner approval.

This authorization does not:
- change Foundation Stage 1 canon;
- open Foundation Stage 5;
- open SP-LAB-002;
- open an external-user pilot;
- declare the owner self-pilot effective;
- define numeric Stage 1 transition thresholds;
- validate a trainer or Selection Capacity score.
