# Selection Point Recovery Checkpoint

**Checkpoint:** SP-RCP-2026-09-15-SP-OPS-002  
**Date:** 15 September 2026  
**Purpose:** reconstruct the current approved project state without dependence on conversational memory or ChatGPT Work.

## 1. Recovery principle

Git history preserves committed states. Current approved meaning is reconstructed from SSOT documents.

The project must remain operable in ordinary Chat even if optional product modes are unavailable or rate-limited.

## 2. Read order

Read in this order:

1. `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`
2. `docs/PROJECT_SYSTEM/PROJECT_CONTROL_PLANE.md`
3. `docs/PROJECT_SYSTEM/SP_CHAT_OPERATING_MODEL.md`
4. `docs/FOUNDATION/PROJECT_STATE.yaml`
5. `docs/PRODUCT_LAB/LAB_STATE.yaml`
6. `docs/TRAINING/STAGE_1_CAPABILITY_SPEC.md`
7. `docs/TRAINING/STAGE_1_RESEARCH_PACKET_SPEC.md`
8. If health/self-pilot evidence is relevant: `xahinvest-DNA/Selection-point-health-lab::docs/NODE_STATE.yaml`

Deferred material that must not be treated as active authorization:
- `docs/TRAINING/DEFERRED_TRAINER_AS_STAGE_EVIDENCE_SYSTEM.md`

## 3. Current approved state

### Project system
- `SP-PSYS-001` Project Control Plane is active.
- `SP-OPS-002` is the active operating model.
- `SP-OPS-001` is superseded and has no active authority.
- No project step requires ChatGPT Work.
- Ordinary Chat owns methodology, research, synthesis, audits, bounded artifact production, evidence assembly and Red Team.
- Codex is optional and limited to approved technical/software implementation.
- Repository split is an authority/privacy boundary, not a split into separate projects.

### Foundation
- Stages 1–4 are completed in Foundation architecture.
- RC-018 is approved.
- Stage 5 is unopened.
- `SP-S5-P01` remains the next unopened Foundation candidate.

### Training development
- Training development proceeds one approved Foundation stage at a time.
- Stage 1 Capability Definition is approved as `SP-TR-S1-CAP-001`.
- Approved capability:

> Человек учится превращать один собственный автоматический эпизод из переживаемой неизбежности в различимый процесс, находить первый реально доступный участок своего участия и фактически менять хотя бы одно дальнейшее продолжение.

- Current gate: **Gate B — Stage 1 Research Packet**.
- Gate B is executed directly in ordinary Chat using `docs/TRAINING/STAGE_1_RESEARCH_PACKET_SPEC.md`.
- Expected artifact: `docs/TRAINING/STAGE_1_RESEARCH_PACKET.md`.
- Gate C remains closed until Red Team review and Owner approval.

### Product Lab / evidence
- Owner self-pilot remains active.
- External-user pilot remains unopened.
- `SP-LAB-002` remains unopened.
- Questionnaire remains telemetry, not SP and not proof of Selection Capacity.
- Health Lab remains `SP-HLAB-001`, a private evidence node.

### Health Lab
At checkpoint creation, verified Health Lab `main` is:
`06990ea2bb7a261c64fa07e87fa102c44e4020f5`

Historical raw records remain immutable by meaning; later schema changes do not authorize retrospective invention.

## 4. Epistemic discipline

Because one Chat now performs both research/synthesis and methodological review, preserve visible labels where relevant:

`APPROVED`, `DERIVED`, `HYPOTHESIS`, `OPEN`, `CONTRADICTION`, `ILLUSTRATION`, `OBSERVED`, `SELF-REPORT`, `INTERPRETATION`.

The same Chat may propose and critique, but may not convert a proposal into approved methodology without Owner approval.

## 5. Parked trainer hypothesis

The trainer-as-stage-evidence-system hypothesis remains parked.

Canonical parking document:
`docs/TRAINING/DEFERRED_TRAINER_AS_STAGE_EVIDENCE_SYSTEM.md`

Trainer implementation is not authorized.

## 6. Current closed gates

Do not infer any of the following:
- Stage 5 opened;
- SP-LAB-002 opened;
- external pilot opened;
- trainer implementation authorized;
- Selection Capacity score validated;
- owner self-pilot proven effective;
- Stage 1 transition thresholds numerically defined.

## 7. Historical operating-model change

- `SP-OPS-001` introduced a separate Work execution layer.
- On 15 September 2026 Owner explicitly rejected that dependency because usage limits could stop the project.
- Decision `PSYS-003` approved `SP-OPS-002` and removed Work from the active operating system.

Git history remains the technical record of the superseded model; new chats must not restore it as active authority.

## 8. New-chat instruction

Reconstruct authoritative context from the read order above first. Conversational/project memory may accelerate orientation, but the repository is the durable source of truth.

Do not ask the Owner to launch or hand work off to ChatGPT Work. Continue Gate B directly in Chat unless the Owner changes the operating model explicitly.
