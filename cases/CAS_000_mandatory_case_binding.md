# CASE: CAS_000_MANDATORY_CASE_BINDING
- **Case ID:** CAS_000_mandatory_case_binding
- **File Path:** cases/CAS_000_mandatory_case_binding.md
- **Type:** FEAT
- **Depends On:** NONE
- **Commit Pattern:** [CAS-000] feat(constitution): ratify brownfield retrofit and implicit spec mining invariant
- **Target Scope (Whitelisted Files):**
  - CONSTITUTION.md
  - verify.py
  - cases/CAS_000_mandatory_case_binding.md
- **Execution State:** ACTIVE
- **Bound Invariant:** INV-BROWNFIELD-RETROFIT
- **Timestamp:** 2026-11-08T19:33:00+03:00
- **Target Module:** core/governance
- **Station / Node:** Construction / Node-3
- **Normative Anchor Commit:** 08b8db4
- **Parity Status:** ACTIVE_CANONICAL
- **Divergence / Root Cause:** Agents entering legacy, unanchored, or partially abandoned projects writing ad-hoc code without reconstructing the canonical specification tree first.
- **Bound Invariants & Constraints:** INV-BROWNFIELD-RETROFIT, INV-BROWNFIELD-RETROFIT-07

## 1. SPECIFICATION CONFLICT ANALYSIS (PROPOSED SPEC VS. COUNTER-CONSTRAINT)
- **Proposed Spec (Action):** Codify INV-BROWNFIELD-RETROFIT as Clause 7 under Article 18 in CONSTITUTION.md and update Gate 16 in verify.py to assert mechanical compliance.
- **Counter-Constraint Audit (Reaction / Discriminator):** Zero code artifacts in core, No-BOM UTF-8 interlingua compliance, Gate 10 topology whitelist integrity, and adjective density <= 0.02.

## 2. MECHANICAL VERIFICATION & RESOLUTION
- **Verification Command & Mechanical Log:**
  - `Command:` python verify.py --verify-all
  - `Telemetry:` All 16 gates PASS with exit code 0.
- **Resolution State:** RESOLVED_LOCAL
- **Grounding Ratio:** Strict mechanical assertion of mandatory backward specification reconstruction before forward code mutation.

## 3. UPSTREAM SYNCHRONIZATION
- **Synchronization State:** RESOLVED_LOCAL
- **Escalation Branch:** NONE
