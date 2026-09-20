
# Recovery Checkpoint — Stage 1 Validation Design Owner Review

**ID:** SP-RCP-2026-09-20-S1-VAL-DESIGN-OWNER-REVIEW  
**Date:** 20 September 2026  
**Status:** active recovery checkpoint

## Current state

Stage 1 architecture remains:

~~~text
architecture_status:
  approved_closed

validation_status:
  efficacy_not_demonstrated
  empirically_open
~~~

A direct post-protocol validation design has now been drafted and Red Teamed.

Artifacts:

- docs/TRAINING/STAGE_1_POST_PROTOCOL_VALIDATION_DESIGN.md
- docs/TRAINING/STAGE_1_POST_PROTOCOL_VALIDATION_RED_TEAM.md

## Proposed V0

Initial test:

~~~text
P-A / Owner self-pilot
one lane
→ short Lane Card
→ supported acquisition
→ reduced-current-prompt observation
→ natural continuation / mismatch probe
~~~

Pragmatic feasibility coverage:

~~~text
target ≥ 6 evaluable live recurrences
including support-state variation where available
calendar cap = 21 days
~~~

These are not mastery or efficacy thresholds.

## Core capture

~~~text
NOTICE
→ OPEN
→ SELECT
→ REALIZE
→ CONSEQUENCE
→ UPDATE
~~~

with:

~~~text
support provenance
measurement reactivity
environment configuration
capture timing
unknown / not_observed
~~~

## Red Team boundaries

- Owner V0 cannot establish independent efficacy.
- Phase 1 → 2 cannot estimate a causal prompt-fading effect.
- Only in-event OPEN supports a live OPEN claim.
- Event capture itself is continuing measurement exposure.
- No running success score is shown.
- Safety/medical/protective support is never withdrawn to prove independence.
- Automaticity/reopenability are opportunistic observations in V0.
- SP-TR-HYP-002 Directed Question remains parked.
- External-user pilot remains unopened.

## Proposed V0 verdict space

~~~text
V0-A — no architecture contradiction requiring reopening observed
V0-B — reopen Gate E
V0-C — reopen Gate F
V0-D — reopen earlier Gate
V0-E — insufficient exposure
~~~

## Owner decision required

Approve, revise or reject SP-TR-S1-VAL-001 before V0 execution.

Until explicit approval:

~~~text
V0_execution: unopened
external_user_pilot: unopened
Stage_2: unopened
~~~
