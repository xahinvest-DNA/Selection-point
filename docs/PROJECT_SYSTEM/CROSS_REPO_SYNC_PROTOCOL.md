# Cross-Repository Synchronization Protocol v1

## Purpose

Define how Selection Point repositories remain one project without duplicating authority or leaking raw personal data.

## 1. Sync classes

### A. Mandatory downstream sync

A registered evidence node must review and adopt or explicitly reject with reason any upstream change to:

- canonical boundary affecting interpretation;
- Reality Event Model;
- measurement specification;
- participant-data/privacy policy;
- evidence/promotion rules.

A node records adoption in its local `docs/NODE_STATE.yaml`.

### B. Optional downstream sync

Language, explanatory examples, UI ideas and non-binding product hypotheses do not automatically require local schema changes.

### C. Upstream promotion

Evidence-node findings do not synchronize upward automatically. They require a promotion packet or equivalent explicit review.

## 2. Promotion packet minimum

A promoted finding must include:

```text
node_id
source_period
source_schema_version
observation summary
candidate interpretation
alternative explanations
supporting / weakening observations
privacy status
allowed conclusion
disallowed stronger conclusion
requested destination: Product Lab | Foundation review
```

No raw personal record is required in the public repository.

## 3. Version rule

The control plane uses semantic document IDs rather than circular commit pinning.

Example:

```text
upstream_control_plane: SP-PSYS-001
upstream_contract: SP-HLAB-CONTRACT-001
foundation_boundary: RC-018
event_model: v0.2
metrics_spec: v0.1
```

An evidence node may also record the upstream Git commit used at the time of synchronization for audit purposes. The control-plane registry does not need to point back to the node's latest commit.

## 4. Conflict precedence

If documents disagree:

1. `PROJECT_SYSTEM_STATE.yaml` decides topology/authority.
2. `FOUNDATION/PROJECT_STATE.yaml` decides canonical architecture status.
3. `PRODUCT_LAB/LAB_STATE.yaml` decides Product Lab state.
4. Node-local `NODE_STATE.yaml` decides local operational state only.
5. Raw records decide what was actually recorded; later interpretation cannot rewrite them.

A lower-precedence document may expose a conflict but may not silently override a higher-precedence source.

## 5. Historical data and schema changes

Historical raw data remain immutable.

When a new schema is adopted:

- old raw files retain their original representation;
- a normalized layer may map old data into the new schema;
- unavailable fields become `unknown` / `not_observed`;
- inference must be labeled as inference, never written back as observed fact;
- source file and transformation version are retained.

## 6. Privacy boundary

Public repositories may contain:

- schemas;
- protocols;
- synthetic examples;
- de-identified aggregate findings;
- methodological decisions.

Private evidence nodes may contain personal raw records only under the node's privacy gate.

External participants require an explicit external-pilot gate and their own consent/data-handling process. An owner self-pilot does not implicitly authorize external-participant collection.

## 7. Consistency checks

Each repository validates what it can locally.

The public control-plane repository checks:

- node registry and contracts exist;
- gates remain correct;
- Product Lab points to the shared event/measurement contracts.

Each private node checks:

- local node state references the active upstream contract;
- active schema/review protocol align with RC-018;
- legacy raw data are not mistaken for normalized v0.2 records;
- privacy gate remains active.

Cross-repository content access is not required for CI; the synchronization contract is explicit and auditable instead.
