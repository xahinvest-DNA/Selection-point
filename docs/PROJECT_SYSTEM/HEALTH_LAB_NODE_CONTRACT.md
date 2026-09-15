# SP-HLAB-CONTRACT-001 — Health Lab Node Contract

**Node:** `SP-HLAB-001`  
**Repository:** `xahinvest-DNA/Selection-point-health-lab`  
**Visibility:** private  
**Status:** active owner self-pilot evidence node

## 1. Role

Health Lab is the private evidence node for the first Selection Point owner self-pilot in the body / health / physical-efficiency domain.

It is part of the same Selection Point project but has a different authority level from Foundation and Product Lab.

## 2. Upstream contracts

Health Lab must remain compatible with:

- RC-018;
- `docs/PRODUCT_LAB/REALITY_EVENT_MODEL_V0_2.md`;
- `docs/PRODUCT_LAB/PILOT_METRICS_SPEC_V0_1.md`;
- `docs/PRODUCT_LAB/PARTICIPANT_DATA_POLICY_V0_1.md`;
- `docs/PROJECT_SYSTEM/CROSS_REPO_SYNC_PROTOCOL.md`.

## 3. Local responsibilities

Health Lab owns:

- owner self-pilot raw data;
- local normalized event data;
- body-response observations;
- local reviews;
- local hypotheses H-xxx;
- protocol-specific operational fields;
- source traceability from normalized records back to raw records.

## 4. Required distinctions

The node must be able to distinguish whenever observed:

```text
PositionSnapshot
SelectionPointEvent
ChoiceRecord
RealizationRecord
ConsequenceRecord
FeedbackRecord
ModelUpdateRecord
UnexpectedEvent
```

It must preserve:

```text
selected continuation ≠ realized continuation
realization ≠ consequence
consequence ≠ used feedback
```

And must explicitly support:

- `conscious_non_action`;
- `partially_executed`;
- `circumstances_changed`;
- `revised_after_new_fact`;
- `forgotten`;
- `unknown`;
- `prompt_exposure`.

## 5. Health-specific extension

The node may add health/body observations such as weight, sleep, energy, discomfort, training, activity, nutrition and other relevant measurements.

These are **domain observations**, not canonical Selection Point constructs.

Health Lab must preserve at least two analytical layers:

```text
Action / Realization Trajectory
Body Response
```

They must not be collapsed into a single health or Selection Capacity score without separate validation.

## 6. Measurement adherence

Questionnaire completion, reminder response and data-entry continuity are stored as `measurement_adherence` / scaffold data.

They must not be counted as health-domain success or as evidence that Selection Capacity improved.

## 7. Legacy raw records

Raw daily records captured on 2026-09-12 through 2026-09-14 predate the synchronized v0.2 node schema and are retained unchanged.

They are valid source observations but **not schema-v0.2-conformant event records**.

Any normalization must:

- reference the source file;
- mark transformation version;
- use `unknown` / `not_observed` where data are absent;
- avoid reconstructing unobserved choice or prompt exposure as fact.

## 8. Promotion boundary

No H-xxx hypothesis or local pattern changes the Product Lab or Foundation automatically.

Promotion requires a de-identified review that separates:

- observed facts;
- participant interpretation;
- researcher interpretation;
- alternative explanations;
- allowed conclusion;
- disallowed stronger conclusion.

## 9. External participant gate

This contract currently authorizes only the owner self-pilot.

Adding other participants requires a separate explicit decision in the Selection Point control plane/Product Lab and a local participant-data implementation before their data become research evidence.
