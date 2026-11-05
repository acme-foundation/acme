# Worklogs: Three-Tier Agent Logging Hierarchy & Decision Ledger
## Scope: Bounded Decision Logging & Dialectic Memory Protocol (DoF = 0)

---

## 1. THREE-TIER LOGGING HIERARCHY
To prevent autonomous agents from polluting repository history with discursive conversational chatter, all execution telemetry is partitioned into three strictly segregated tiers:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ TIER 1: TRACE / DEBUG (Ephemeral Operational Noise)                                    │
│ Target: .tmp/execution.log (Transient local memory; strictly excluded from Git)       │
│ Content: Raw shell outputs, AST dumps, compiler tracebacks, token usage metrics.       │
│ Lifecycle: Purged automatically at session teardown; never tracked in version control. │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼ (State Transitions & Dialectic Synthesis)
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ TIER 2: DECISION / DIALECTIC (Architectural Decision Records)                          │
│ Target: workflows/worklogs/WL_{YYYYMMDD}_{ID}_{SLUG}.md (Committed to Git)             │
│ Content: "Barely Sufficient" 20-line atomic records: Thesis vs. Murphy, Resolution.    │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼ (Finite State Machine Convergence)
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ TIER 3: STATE_DELTA (Ground-Truth Machine State)                                       │
│ Target: .acme/workspace_state.json (Committed machine-readable JSON)                   │
│ Content: Active phase coordinates (r, θ, Z), Merkle digests, invariant lock hashes.   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. DECISION LOGGING INVARIANTS (TIER 2)

1. **Barely Sufficient Discipline ($\le 20$ Lines):**
   - Worklogs must conform strictly to `templates/WL_TEMPLATE.md`.
   - Conversational filler, emotional reflections, and speculative thoughts are prohibited (`REJECT_UNANCHORED_INTENT`).
2. **Mandatory Dialectic Triad:**
   - Every recorded decision must document:
     - The defended thesis.
     - The Murphy antithesis (the cheapest structural or adversarial escape vector).
     - The resolution and rejected alternative justification.
3. **Doctrine / Scar Tissue Integration:**
   - Every worklog must state the resulting institutional learning or invariant update (`scar_tissue`).
4. **Cryptographic Anchoring:**
   - Every entry must bind to the affected file path, Git commit hash, and verification status (`PASS` / `REWORK` / `REJECT`).
5. **Dependency Classification (`INV-MIN-DEPENDENCY`):**
   - Every entry must declare its asset status: `Zero-Asset` vs. `CDN-Leverage: Tailwind / Native API` vs. `Stdlib`. Parasitic uncontrolled packages remain banned.

