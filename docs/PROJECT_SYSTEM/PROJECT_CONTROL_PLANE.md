# Selection Point Project Control Plane

**ID:** SP-PSYS-001  
**Status:** active  
**Date:** 15 September 2026

## 1. Why this exists

Selection Point is one project, even when different layers live in different repositories.

Repository boundaries serve different needs:

- public methodological work must remain inspectable and free from personal raw data;
- private pilot evidence must preserve longitudinal detail without contaminating the public theory layer;
- local experiments must be able to change quickly without silently redefining Selection Point.

The Project Control Plane is the governance layer that keeps these parts synchronized.

## 2. Layers

```text
FOUNDATION / CANON
    ↓ defines allowed meaning and boundaries
PRODUCT LAB
    ↓ defines product hypotheses, event/measurement contracts
EVIDENCE NODES
    ↓ collect real observations under those contracts
REVIEWS / PROMOTION PACKETS
    ↑ return de-identified findings, contradictions and falsification signals
GOVERNANCE
    ↑ decides whether the general model changes
```

The first registered evidence node is `SP-HLAB-001` in the private repository `xahinvest-DNA/Selection-point-health-lab`.

## 3. Authority rule

A lower layer may add local detail but may not silently acquire the authority of a higher layer.

Therefore:

- Foundation owns canonical meaning.
- Product Lab owns working product hypotheses and research contracts.
- Evidence nodes own their raw data, local normalization, reviews and open hypotheses.
- An evidence-node hypothesis is not a Product Lab conclusion.
- A Product Lab conclusion is not automatically canon.

## 4. Contract propagation

When an approved upstream boundary changes, every active evidence node must explicitly record its sync state.

Current shared contract:

- RC-018;
- `REALITY_EVENT_MODEL_V0_2.md`;
- `PILOT_METRICS_SPEC_V0_1.md`;
- participant-data boundary;
- no composite Selection Capacity / trajectory score without validation.

For RC-018 the minimum distinction is:

```text
selected continuation
≠ realized continuation
≠ consequence
≠ noticed / used feedback
```

## 5. Evidence return path

Evidence does not move upward as raw personal records.

The allowed return path is:

```text
raw event
→ local normalized event
→ local review
→ candidate finding / contradiction
→ de-identification
→ promotion review
→ Product Lab hypothesis or falsification signal
→ Foundation governance only if canonical change is proposed
```

Every promoted finding must preserve enough traceability to state:

- what was observed;
- under which schema/protocol;
- what alternative explanations remain;
- what conclusion is allowed;
- what stronger conclusion is not allowed.

## 6. No circular synchronization

Repositories do not mirror each other wholesale.

The main repository owns the **node contract**. Each evidence repository owns its **NODE_STATE** and records which upstream control-plane version it has adopted.

This avoids a commit loop in which each repository must continually point at the other's newest commit.

## 7. Raw-data immutability

Upstream schema changes do not authorize rewriting historical raw records.

Legacy raw observations remain as captured. If a newer schema is needed, a normalized/derived representation may be produced with:

- source reference;
- transformation version;
- explicit `unknown` where the old record did not observe a field;
- no invented values.

## 8. Measurement adherence boundary

Completing a questionnaire, responding to a reminder, or remaining in the study can be operationally important, but must be stored separately from behavior in the target domain.

```text
measurement adherence ≠ health-domain action
measurement adherence ≠ Selection Capacity proof
prompted realization ≠ unprompted realization
```

This prevents the research instrument from validating itself merely because the participant continues using it.

## 9. Gates preserved by this decision

Creating or changing the Project Control Plane does **not**:

- open Stage 5;
- open SP-LAB-002;
- open an external-user pilot;
- create an efficacy claim;
- turn the health pilot into a medical protocol;
- authorize external participant raw data in the public repository.

## 10. Active operating model

Project execution follows `SP-OPS-002` in `docs/PROJECT_SYSTEM/SP_CHAT_OPERATING_MODEL.md`.

The execution layers are:

```text
Owner — direction and final approval
Chat — methodology + research + synthesis + audits + bounded artifacts + evidence review + Red Team
Codex — approved technical implementation only when required
Pilot / Reality — empirical validation layer
```

There is no required ChatGPT Work layer. Tool or mode availability must not become a project-level dependency.

The critical separation is maintained through governance and epistemic labels inside Chat rather than by handing work to a separate product mode.

A task must not be delegated to Codex while it still contains an unresolved methodological decision.

For stage-training development the standard artifact chain is:

```text
Stage Capability Spec
→ Stage Research Packet
→ Psychological Mechanism Map
→ Learning Units
→ Practice Protocol
→ Observability / Measurement Spec
→ Pilot Evidence Packet
→ Stage Review
```

The questionnaire remains a telemetry instrument and is not Selection Point itself.

Current authorization is Gate B — Stage 1 Research Packet, executed directly in Chat. Gate C remains closed until Red Team review and Owner approval.

## 11. Sources of truth

System topology: `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`.

Project operating model: `docs/PROJECT_SYSTEM/SP_CHAT_OPERATING_MODEL.md`.

Current recovery checkpoint: `docs/PROJECT_SYSTEM/RECOVERY_CHECKPOINT_2026-09-15_SP_OPS_002.md`.

Foundation state: `docs/FOUNDATION/PROJECT_STATE.yaml`.

Product Lab state: `docs/PRODUCT_LAB/LAB_STATE.yaml`.

Health evidence-node local state: `xahinvest-DNA/Selection-point-health-lab::docs/NODE_STATE.yaml`.
