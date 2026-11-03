# Selection Point Project Control Plane

**ID:** SP-PSYS-001  
**Status:** active  
**Created:** 15 September 2026  
**Updated:** 3 November 2026

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
    ↓ defines product hypotheses, environment mechanics and evidence contracts
EVIDENCE NODES / REALITY
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
- Product Lab owns working product hypotheses, environment architecture and research contracts.
- Evidence nodes own their raw data, local normalization, reviews and open hypotheses.
- An evidence-node hypothesis is not a Product Lab conclusion.
- A Product Lab conclusion is not automatically canon.

The environment-first reset is a **Product Lab / project-route decision** and does not silently rewrite Foundation.

## 4. Current shared contract

Current shared boundaries include:

- RC-018;
- `REALITY_EVENT_MODEL_V0_2.md`;
- participant-data boundary;
- no composite Selection Capacity / trajectory score without validation;
- simulation performance is not evidence of real-world transfer by itself.

Minimum distinction:

```text
selected continuation
≠ realized continuation
≠ consequence
≠ noticed / used feedback
```

Environment-first adds:

```text
simulated continuation
≠ real-world continuation
simulator improvement
≠ demonstrated transfer
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

For environment-first work, simulator evidence and real-world transfer evidence must remain distinguishable.

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

Completing a questionnaire, responding to a reminder, finishing scenarios or remaining in the study can be operationally important, but must be stored separately from behavior in the target domain.

```text
measurement adherence ≠ target-domain action
scenario completion ≠ Selection Capacity proof
simulator success ≠ real-world transfer proof
prompted realization ≠ unprompted realization
```

This prevents the research instrument or simulator from validating itself merely because the participant continues using it.

## 9. Gates preserved by this decision

Creating or changing the environment-first route does **not**:

- open Foundation Stage 5;
- open SP-LAB-002;
- open an external-user pilot;
- authorize software implementation;
- create an efficacy claim;
- turn the health field into a medical protocol;
- authorize external participant raw data in the public repository.

## 10. Active operating model

Project execution follows `SP-OPS-002` in `docs/PROJECT_SYSTEM/SP_CHAT_OPERATING_MODEL.md`.

```text
Owner — direction and final approval
Chat — methodology + research + synthesis + audits + bounded artifacts + evidence review + Red Team
Codex — approved technical implementation only when required
Simulation / Reality — experience and empirical validation layers
```

There is no required ChatGPT Work layer. Tool or mode availability must not become a project-level dependency.

A task must not be delegated to Codex while it still contains an unresolved methodological decision or while software implementation remains closed.

The active development route is always `PROJECT_SYSTEM_STATE.yaml.current_work`.

As of 3 November 2026:
- environment-first supersedes course-first as the active route;
- `docs/COURSE/` remains historical/reference and a scenario-source layer;
- A–H training artifacts remain research/reference inputs;
- the questionnaire remains separate telemetry;
- software implementation and external pilot remain closed.

## 11. Sources of truth

- Active system topology: `docs/PROJECT_SYSTEM/PROJECT_SYSTEM_STATE.yaml`.
- Current recovery checkpoint: `docs/PROJECT_SYSTEM/RECOVERY_CHECKPOINT_2026-11-03_ENVIRONMENT_FIRST_RESET.md`.
- Active route decision: `docs/PROJECT_SYSTEM/DECISION_ENVIRONMENT_FIRST_RESET_2026-11-03.md`.
- Active environment architecture: `docs/PRODUCT_LAB/ADAPTIVE_ENVIRONMENT_ARCHITECTURE_V0.md`.
- Project management protocol: `docs/PROJECT_SYSTEM/PROJECT_MANAGEMENT_PROTOCOL_V1.md`.
- Project operating model: `docs/PROJECT_SYSTEM/SP_CHAT_OPERATING_MODEL.md`.
- Foundation state: `docs/FOUNDATION/PROJECT_STATE.yaml`.
- Product Lab state: `docs/PRODUCT_LAB/LAB_STATE.yaml`.
- Health evidence-node local state: `xahinvest-DNA/Selection-point-health-lab::docs/NODE_STATE.yaml`.
