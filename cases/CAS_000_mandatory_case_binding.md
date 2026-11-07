# CASE: CAS_000_MANDATORY_CASE_BINDING
- **Case ID:** CAS_000_mandatory_case_binding
- **File Path:** cases/CAS_000_mandatory_case_binding.md
- **Type:** FEAT
- **Commit Pattern:** [CAS-000] feat(core): ratify flat case topology, local counter scoping, and PRE template (DoF=0)
- **Target Scope (Whitelisted Files):**
  - CONSTITUTION.md
  - README.md
  - templates/CAS_TEMPLATE.md
  - templates/PRECEDENT_TEMPLATE.md
  - templates/PRE_TEMPLATE.md
  - precedents/ingestion/ING_001_STREAM_QUARANTINE_RULING.md
  - precedents/PRE_001_stream_quarantine.md
  - verify.py
  - cases/CAS_000_mandatory_case_binding.md
- **Execution State:** ACTIVE
- **Bound Invariant:** INV-PRECEDENT-PROMOTION
- **Timestamp:** 2026-11-07T23:20:00+03:00
- **Target Module:** core/governance
- **Station / Node:** Construction / Node-3
- **Normative Anchor Commit:** 0920640
- **Parity Status:** ACTIVE_CANONICAL
- **Divergence / Root Cause:** Hierarchical case subdirectories risk counter collision; precedent promotion lacks standardized schema and automated verification.
- **Bound Invariants & Constraints:** INV-FLAT-REGISTRY-01, INV-LOCAL-COUNTER-SCOPE-02, INV-PRECEDENT-PROMOTION-03

## 1. SPECIFICATION CONFLICT ANALYSIS (PROPOSED SPEC VS. COUNTER-CONSTRAINT)
- **Proposed Spec (Action):** Codify flat case registry and precedent promotion protocol as Article 14, standardize templates/PRE_TEMPLATE.md, migrate precedents to flat PRE schema, and enforce Gate 11 and Gate 12 in verify.py.
- **Counter-Constraint Audit (Reaction / Discriminator):** Zero executable artifacts in core, No-BOM UTF-8 interlingua compliance, and adjective density <= 0.02.

## 2. MECHANICAL VERIFICATION & RESOLUTION
- **Verification Command & Mechanical Log:**
  - `Command:` python verify.py --verify-all
  - `Telemetry:` All 12 gates PASS with exit code 0.
- **Resolution State:** RESOLVED_LOCAL
- **Grounding Ratio:** Strict enforcement of flat registry topology and canonical precedent lineage.

## 3. UPSTREAM SYNCHRONIZATION
- **Synchronization State:** RESOLVED_LOCAL
- **Escalation Branch:** NONE
