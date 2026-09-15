# Selection Point Recovery Checkpoint

**Checkpoint:** SP-RCP-2026-09-15-S1-CAP  
**Date:** 15 September 2026  
**Purpose:** allow a new chat/operator to reconstruct the current approved project state from repository sources without relying on conversational memory alone.

## 1. Recovery principle

Git history preserves every committed state. Approved project meaning is reconstructed from current SSOT documents, not from remembered chat wording.

Use this checkpoint when context is missing, a new chat starts, or project state appears inconsistent.

## 2. Read order

Read in this order:

1. `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`
2. `docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md`
3. `docs/PROJECT_SYSTEM/SP_WORK_OPERATING_MODEL.md`
4. `docs/FOUNDATION/PROJECT_STATE.yaml`
5. `docs/PRODUCT_LAB/LAB_STATE.yaml`
6. `docs/TRAINING/STAGE_1_CAPABILITY_SPEC.md`
7. If health/self-pilot evidence is relevant: `xahinvest-DNA/Selection-point-health-lab::docs/NODE_STATE.yaml`

Deferred material that must not be treated as active authorization:
- `docs/TRAINING/DEFERRED_TRAINER_AS_STAGE_EVIDENCE_SYSTEM.md`

## 3. Current approved state

### Project system
- `SP-PSYS-001` Project Control Plane is active.
- `SP-OPS-001` Owner + Chat + Work + Codex + Reality operating model is approved.
- Repository split is an authority/privacy boundary, not a split into separate projects.

### Foundation
- Stages 1–4 are completed in Foundation architecture.
- RC-018 is approved.
- Stage 5 is unopened.
- `SP-S5-P01` remains the next unopened Foundation candidate.

### Training development
- Training work proceeds one approved Foundation stage at a time.
- Stage 1 Capability Definition is approved as `SP-TR-S1-CAP-001`.
- Approved capability:

> Человек учится превращать один собственный автоматический эпизод из переживаемой неизбежности в различимый процесс, находить первый реально доступный участок своего участия и фактически менять хотя бы одно дальнейшее продолжение.

- The next allowed training artifact is **Gate B — Stage 1 Research Packet**.
- This does not reopen or change Foundation Stage 1 canon.

### Product Lab / evidence
- Owner self-pilot remains active.
- External-user pilot remains unopened.
- `SP-LAB-002` remains unopened.
- Questionnaire remains telemetry, not SP and not proof of Selection Capacity.
- Health Lab remains `SP-HLAB-001`, a private evidence node.

### Health Lab
At checkpoint creation, verified Health Lab `main` is at commit:
`a4f87de28d66613eac67dcd958b65058498f2b84`

Its raw historical records remain immutable by meaning, and later schema changes do not authorize retrospective invention.

## 4. Parked trainer hypothesis

The following idea has been preserved for later work but is not active implementation scope:

- future trainer may operate as a multi-timeframe **stage evidence system**;
- it should distinguish reality trajectory from capability trajectory;
- higher-scale views must drill down to concrete events;
- facts, self-report and interpretation must remain epistemically distinct;
- prompt/scaffold exposure must be visible;
- the trainer should accumulate evidence for transition review rather than declare mastery via a universal score.

Canonical parking document:
`docs/TRAINING/DEFERRED_TRAINER_AS_STAGE_EVIDENCE_SYSTEM.md`

## 5. Current closed gates

Do not infer any of the following from this checkpoint:

- Stage 5 opened;
- SP-LAB-002 opened;
- external pilot opened;
- trainer implementation authorized;
- Selection Capacity score validated;
- owner self-pilot proven effective;
- Stage 1 transition thresholds numerically defined.

## 6. How to recover a prior repository state

Every Git commit is a technical recovery point. Important merged decisions also exist as PR/merge commits.

Recent major anchors before this checkpoint include:
- `59b705d8362c9c7c7be4690e805093a26fdb758f` — Project Control Plane established;
- `30601cb7a4deef9cdd8fa64595d334c631afaaaf` — SP work operating model approved;
- `c7789a44896a4f3114f443156ca1ccb88a1b6141` — Stage 1 Capability Spec approved.

A rollback or comparison should use Git history/commit diffs rather than rewriting current SSOT from memory.

## 7. New-chat instruction

When a new chat begins, do not assume conversational memory contains the full project. Reconstruct authoritative context from the read order above first. Conversational/project memory may accelerate orientation, but the repository remains the durable source of truth for approved project state.
