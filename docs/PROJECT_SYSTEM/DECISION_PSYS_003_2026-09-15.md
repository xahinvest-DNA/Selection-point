# Decision PSYS-003 — Remove Work Dependency

**Date:** 2026-09-15  
**Status:** approved  
**Decision owner:** Андрей  
**Operating model:** `SP-OPS-002`  
**Supersedes:** `SP-OPS-001` / Decision PSYS-002 as active operating authority

## Decision

Remove ChatGPT Work from the active Selection Point operating system because hard usage limits create a project-level dependency capable of blocking progress.

The project will not rely on a separate Work mode for research, synthesis, audits, artifact production or evidence assembly.

Approved operating flow:

```text
Owner
→ Chat — methodology + research + synthesis + bounded artifact production
→ Codex only where approved technical implementation is required
→ Pilot / Reality
→ Chat — evidence assembly + interpretation + Red Team
→ Owner decision
```

## Core rationale

The useful distinction introduced by the previous model was not the product mode itself. It was the separation between:
- methodological authority;
- research/synthesis;
- technical implementation;
- empirical validation;
- final approval.

Those distinctions are preserved as governance and epistemic boundaries inside ordinary Chat and repository SSOT.

The project must remain able to continue when any optional product mode is unavailable, rate-limited or removed.

## Chat responsibilities expanded

Chat now owns all non-technical project operations, including:
- repository/context reconstruction;
- research across approved sources;
- external research when useful;
- synthesis and contradiction mapping;
- research packets;
- learning/research/analysis artifacts;
- evidence assembly;
- Red Team and interpretation;
- bounded repository synchronization;
- preparation of technical briefs for Codex.

This does not allow Chat to silently self-approve methodological changes. Owner retains final approval authority.

## Codex boundary

Codex remains optional and is used only for approved technical/software implementation. It does not define methodological meaning.

## Gate discipline preserved

The standard stage chain remains:

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

The absence of a separate Work mode does not allow automatic movement between gates.

## Current authorization

Stage 1 Capability Spec `SP-TR-S1-CAP-001` remains approved.

Current gate remains:

**Gate B — Stage 1 Research Packet.**

Gate B is now executed directly in Chat using an executor-neutral specification.

Gate C remains closed until Gate B review and Owner approval.

## Preserved closed gates

This decision does not open:
- Foundation Stage 5;
- `SP-LAB-002`;
- external-user pilot;
- trainer implementation.

It does not create an efficacy claim, mastery threshold or Selection Capacity score.

## Historical record

Decision PSYS-002 and SP-OPS-001 remain part of Git history as the prior operating model, but they no longer have active authority.
