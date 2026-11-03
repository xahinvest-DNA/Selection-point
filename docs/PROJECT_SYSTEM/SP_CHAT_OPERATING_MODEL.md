# Selection Point Chat Operating Model

**ID:** SP-OPS-002  
**Status:** approved  
**Approved:** 15 September 2026  
**Updated:** 3 November 2026  
**Scope:** project operating model for methodology, research, synthesis, artifact production, technical execution and reality-based validation without dependency on a specific ChatGPT mode.

## 1. Purpose

Selection Point must remain operable without a separate execution mode whose usage limits can block the project.

One persistent Chat may perform methodological architecture, research, synthesis, project operation and bounded repository work. The separation that matters is **epistemic and governance separation**, not product-mode separation.

```text
Owner
  ↓
Chat — methodology + research + synthesis + bounded artifact production
  ↓
Simulation — bounded repeated experience when authorized
  ↓
Reality — actual realization, consequences, contradictions, transfer evidence
  ↓
Chat — evidence assembly + interpretation + Red Team
  ↓
Owner — approve, reject or revise
```

Codex is inserted only when separately authorized software implementation is actually required.

## 2. Roles and authority

### 2.1 Owner — Андрей

Owns project direction and final decisions.

Authority:
- approve or reject methodological/product decisions;
- open or keep closed project gates;
- approve movement between tasks/routes;
- authorize changes to canon, Product Lab or pilot scope through the relevant governance layer.

An item remains provisional until explicit owner approval such as `утверждаем`, except purely mechanical synchronization that does not change meaning.

### 2.2 Chat — Methodological Architect + Project Operator

Responsibilities:
- reconstruct repository/context from SSOT;
- conceptual discussion and methodological architecture;
- critical analysis and Red Team;
- external and internal research where materially useful;
- prepare/revise bounded artifacts;
- audit synchronization and contradictions;
- assemble and interpret evidence without upgrading uncertainty;
- formulate implementation requirements only after the product meaning is stable enough.

Chat may propose but may not silently approve its own methodological proposal on behalf of Owner.

Chat has no authority to:
- change approved Foundation canon without the relevant owner decision;
- declare a hypothesis confirmed because it is coherent;
- treat simulator completion or preferred answers as proof of Selection Capacity;
- treat simulator improvement as real-world transfer;
- convert correlation or temporal order into causation;
- open Foundation Stage 5, SP-LAB-002, external pilot or software implementation without Owner authorization;
- promote private evidence into Product Lab/Foundation without explicit review;
- expand V0 merely because a new idea is interesting.

### 2.3 Codex — Technical Executor

Codex is optional and is used only after software implementation is explicitly opened.

It may implement approved code, schemas, parsers, storage, dashboards, tests, CI and automation. It does not define methodological meaning.

### 2.4 Simulation — Experience Layer

Simulation is a product mechanism, not proof.

Its role is to create repeated representative selection situations and expose:
- relevant cues/constraints;
- available continuations;
- selected vs realized continuation;
- immediate/delayed consequences;
- trajectory effects;
- feedback;
- varied repetition and prompt fading.

Simulation must not become a disguised morality quiz. Success inside simulation is an observation about simulation performance only.

### 2.5 Reality — Validation Layer

Reality returns:
- actual realization or non-realization;
- consequences;
- unexpected events;
- contradictions;
- missing observability;
- transfer / non-transfer evidence;
- evidence that may weaken or falsify the working model.

Reality outranks explanatory elegance.

## 3. Epistemic labels

Use these labels where material:

- **APPROVED** — explicit approved project meaning;
- **DERIVED** — conservative synthesis implied by approved material;
- **HYPOTHESIS** — candidate explanation requiring review/evidence;
- **OPEN** — unresolved question;
- **CONTRADICTION** — tension that must not be smoothed over;
- **ILLUSTRATION** — example that explains but does not prove;
- **OBSERVED** — directly recorded fact/behavior;
- **SELF-REPORT** — participant account;
- **INTERPRETATION** — analyst/project reading of evidence.

A label change that alters methodology requires an explicit reason and, where appropriate, Owner approval.

## 4. Active route

The active route is always read from `PROJECT_SYSTEM_STATE.yaml.current_work`.

As of 3 November 2026:
- the active route is `stage_1_environment_first_development`;
- `DECISION_ENVIRONMENT_FIRST_RESET_2026-11-03.md` supersedes course-first as the active product route;
- `docs/COURSE/` is historical/reference and a scenario/content source;
- A–H training artifacts are research/reference inputs, not an active prerequisite sequence;
- no software implementation or external pilot is authorized.

## 5. Environment-first work sequence

The authorized design sequence is:

```text
one target capability
→ scenario grammar
→ 10–15 representative scenarios
→ manual/simplest viable environment
→ one bounded reality-transfer experiment
→ evidence + contradictions
→ Owner review
```

At the current checkpoint only the first two design objects are authorized. Later steps require the state/owner gates recorded in `PROJECT_SYSTEM_STATE.yaml`.

## 6. Evidence contract

Preserve these distinctions:

```text
selected continuation ≠ realized continuation
simulated realization ≠ real-world realization
scenario completion ≠ Selection Capacity proof
simulator improvement ≠ real-world transfer
questionnaire adherence ≠ target-domain behavior
```

Theory vocabulary is not a mastery criterion.

## 7. Scientific boundary

Do not use “the brain does not distinguish simulated/imagined and real experience” as a project fact.

The active working hypothesis is narrower:
- simulated practice can support learning;
- immersion is not assumed to be the mechanism;
- representative information/action structure matters;
- transfer must be checked in reality.

Source: `docs/FOUNDATION/SOURCE_MATERIALS/29_2026-11-03_ADAPTATION_ENVIRONMENT_AND_TRANSFER.md`.

## 8. Tool-use boundary

Tool choice is implementation detail, not a project authority layer.

- **Chat + repository/web/file tools:** methodology, research, synthesis, audits, documents, evidence packets and bounded repository edits.
- **Codex:** only after approved technical/software implementation.
- **Simulation:** only to the extent authorized by the current route.
- **Reality:** empirical contact.

If a tool is unavailable or rate-limited, project meaning and continuity must remain recoverable from repository SSOT.

## 9. Continuity across chats

Durable state lives in the repository, not in a conversation or product mode.

A new Chat reconstructs context in the order defined in `PROJECT_SYSTEM_STATE.yaml.new_chat_bootstrap.read_first`.

The first two documents are always:
1. `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`;
2. the current recovery checkpoint.

Older course/Gate artifacts may not override the active route merely because they contain earlier approvals.

## 10. Current authorization

Read `PROJECT_SYSTEM_STATE.yaml.current_work`, the current recovery checkpoint and `active_working_inputs`.

Current authorization is **design/specification of the V0 capability and scenario grammar only**.

The environment-first reset does not open:
- Foundation Stage 5;
- SP-LAB-002;
- external-user pilot;
- software implementation.
