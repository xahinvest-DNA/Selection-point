# PSYS-001 — Establish Selection Point Project Control Plane

**Date:** 2026-09-15  
**Owner decision:** synchronize `Selection-point` and `Selection-point-health-lab` as one project with different internal authority/evidence levels before returning to detailed pilot design.

## Decision

Selection Point is treated as one project with multiple repository nodes.

The public `Selection-point` repository becomes the control-plane repository for:

- system topology;
- authority boundaries;
- canonical and Product Lab contracts;
- cross-repository synchronization;
- promotion gates.

The private `Selection-point-health-lab` repository is registered as `SP-HLAB-001`, a private evidence node for the owner self-pilot.

## Consequences

1. Repository separation is a privacy/authority boundary, not a project split.
2. Health Lab adopts RC-018 and the Product Lab Reality Event / metrics contracts.
3. Existing raw records remain immutable and become legacy-source records.
4. New capture is versioned forward; normalization may map legacy raw records without inventing missing observations.
5. Measurement adherence is separated from target-domain behavior.
6. Evidence moves upward only through de-identified promotion review.
7. External-user pilot remains unopened.
8. Stage 5 and SP-LAB-002 remain unopened.

## Non-decision

This decision does not yet define the final pilot questionnaire, participant protocol, duration, comparison design, intervention schedule or success/falsification thresholds. Those return to discussion after synchronization is complete.
