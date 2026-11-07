# CASE: CAS_{HEX3}_{SLUG}
- **Case ID:** CAS_{hex3}_{slug}
- **File Path:** cases/CAS_{hex3}_{slug}.md
- **Type:** [BUG | FEAT | REFACTOR | INQUEST | ASSET | SPIKE]
- **Depends On:** [CAS-XXX | NONE]
- **Commit Pattern:** [CAS-{HEX3}] <action>: <description>
- **Target Scope (Whitelisted Files):**
  - [Mandatory: Explicit list of relative file paths permitted for modification]
- **Execution State:** [ACTIVE | BLOCKED | RESOLVED]
- **Bound Invariant:** [INV-* reference, e.g., INV-PRECEDENT-PROMOTION]
- **Timestamp:** YYYY-MM-DDTHH:MM:SS+03:00
- **Target Module:** [Module path or bounded subsystem]
- **Station / Node:** [Inception | Elaboration | Construction | Transition]
- **Normative Anchor Commit:** [HEAD Commit SHA of upstream ACME at case creation]
- **Parity Status:** [ACTIVE_CANONICAL | REJECTED_STALE_DRIFT]
- **Divergence / Root Cause:** [Operational friction, constraint breach, or failure trace]
- **Bound Invariants & Constraints:** [Deterministic assertions / DoF = 0]

## 1. SPECIFICATION CONFLICT ANALYSIS (PROPOSED SPEC VS. COUNTER-CONSTRAINT)
<!-- NOTE: For Type: SPIKE or INCEPTION cases, heading 1 MUST be: '## 1. BLOCKING DECISION MATRIX' -->
- **Proposed Spec (Action):** [...]
- **Counter-Constraint Audit (Reaction / Discriminator):** [...]

## 2. MECHANICAL VERIFICATION & RESOLUTION
<!-- NOTE: For Type: SPIKE or INCEPTION cases, heading 2 MUST be: '## 2. STRUCTURAL SKELETON' -->
- **Verification Command & Mechanical Log:**
  - `Command:` [Command executed]
  - `Telemetry:` [Exit code, memory metrics, test output]
- **Resolution State:** [RESOLVED_LOCAL | ESCALATED_UPSTREAM]
- **Grounding Ratio:** [Deterministic rationale and eliminated alternatives]

## 3. UPSTREAM SYNCHRONIZATION
- **Synchronization State:** [RESOLVED_LOCAL | ESCALATED_UPSTREAM]
- **Escalation Branch:** [cases/{project}/CAS_{hex3}_{slug} | NONE]
