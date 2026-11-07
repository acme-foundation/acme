# CASE: CASE_{HEX3}_{SLUG}
- **Case ID:** CASE_{HEX3}_{SLUG}
- **Timestamp:** YYYY-MM-DDTHH:MM:SS+03:00
- **Target Module:** [Module path or bounded subsystem]
- **Station / Node:** [Inception | Elaboration | Construction | Transition]
- **Normative Anchor Commit:** [HEAD Commit SHA of upstream ACME at case creation]
- **Parity Status:** [ACTIVE_CANONICAL | REJECTED_STALE_DRIFT]
- **Divergence / Root Cause:** [Operational friction, constraint breach, or failure trace]
- **Bound Invariants & Constraints:** [Deterministic assertions / DoF = 0]

## 1. SPECIFICATION CONFLICT ANALYSIS (PROPOSED SPEC VS. COUNTER-CONSTRAINT)
- **Proposed Spec (Action):** [...]
- **Counter-Constraint Audit (Reaction / Discriminator):** [...]

## 2. MECHANICAL VERIFICATION & RESOLUTION
- **Verification Command & Mechanical Log:**
  - `Command:` [Command executed]
  - `Telemetry:` [Exit code, memory metrics, test output]
- **Resolution State:** [RESOLVED_LOCAL | ESCALATED_UPSTREAM]
- **Grounding Ratio:** [Deterministic rationale and eliminated alternatives]

## 3. UPSTREAM SYNCHRONIZATION
- **Synchronization State:** [RESOLVED_LOCAL | ESCALATED_UPSTREAM]
- **Escalation Branch:** [cases/{project}/CASE_{hex3}_{slug} | NONE]
