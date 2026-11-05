# WF-004: Construction & Worker Execution Workflow
## Scope: Surgical Implementation, Atomic Units (<=500 tokens) & Zero-Fluff Purity (DoF = 0)
*Classical AUP Discipline: Implementation*

---

## 1. TRIGGER CONTRACT
- **Pre-condition:** Ratified `artifacts/SPEC_ELABORATION.md` from WF-003 with passing Section 1.4 Pre-Mortem Gate.
- **Input Types:** Living specification, FIR state schemas, component interface contracts.
- **Degrees of Freedom (DoF):** 0 (Surgical implementation strictly bounded by specification).
- **Resource Ceiling:** Token window $\le 500$ per atomic compilation unit; generation temperature $T \to 0^+$.

---

## 2. INNER MICRO-LOOP & STATE MACHINE (TRIAGE -> DIAGNOSE -> SOLVE)

### State 0: Pre-Construction Clean-Room Verification
- [ ] Verify execution environment: Are there secondary tools (`tools/`), unanchored scripts, or ambient artifacts?
  - YES: Purge foreign runtimes immediately (`REJECT_TOOLING_LEAK`).
  - NO: Proceed to State 1.

### State 1: Work Package Decomposition into Atomic Modules
- [ ] Slice implementation tasks into discrete, isolated construction tickets.
- [ ] Enforce Atomic Module Constraint: Each synthesized module/file must remain $\le 500$ tokens in size.
- [ ] Reject any broad speculative refactoring beyond the explicit specification manifest (`REJECT_SCOPE_DRIFT`).

### State 2: Polymath Worker Code Synthesis
- [ ] Execute synthesis within strictly bounded DoF envelope:
  - Generate atomic component or module code.
  - Apply phase-locked typed interfaces.
  - Embed zero subjective comments (*"magic number"*, *"temporary fix"*, *"fast hack"*).
- [ ] Enforce Tree-sitter AST compliance: No component state inside Application Shell (`REJECT_TIER_CROSSING`).

### State 3: Local Verification & Lint Turnstile
- [ ] Compile module against local type checker and static analyzer.
- [ ] Confirm zero runtime side-effects outside designated component boundary.

---

## 3. EVALUATION & ADVERSARIAL GATE

### A. Writers' Room Focus
- **Architect:** Audits generated code for 1:1 fidelity with the 3-tier architectural specification.
- **Proceduralist:** Verifies zero unauthorized package installations or external system calls (`INV-RUNTIME-INTERCEPT`).
- **Scarred Senior:** Inspects memory allocation, variable scoping, error handling paths, and boundary conditions.

### B. Murphy Stress Filter
- **Escape Vector 1 (Silent Catch Blocks):** Swallowing exceptions to artificially pass test gates.
- **Escape Vector 2 (Scope Expansion):** Worker generating extra helper utilities unrequested by specification.
- **Escape Vector 3 (Fluff Injection):** Embedding subjective or speculative commentary into production files.

---

## 4. BACKPROPAGATION & PLOTTER LOGIC
- **Horizontal Oscillation (Δθ Plotter):**
  - If Silent Catch or Fluff detected: Plotter rejects the atomic patch immediately; return to State 2 for sanitization.
  - If Scope Expansion detected: Plotter trims extra code and clamps diff strictly to manifest.
- **Inter-Layer Escalation Protocol (Vertical Dynamics - ΔZ):**
  - **Local Tolerance (Δθ):** Maximum 3 micro-oscillations within Phase 04 for local syntax or unit test errors.
  - **Macro Fracture Trigger:** If code synthesis reveals that the 3-tier architecture cannot support the feature, or Tree-sitter AST tier crossings are unavoidable:
    - **Vertical Fallback Target (ΔZ):** Terminate code synthesis immediately (Exit Code 126). Revert altitude to `workflows/03_elaboration_arch.md` (or `workflows/02_inception_domain.md` if the underlying requirement is flawed).
    - **Pruning & Ballast Ejection:** All partially generated code files are immediately purged as unverified ballast to prevent entropy pollution ($\delta S = 0$).
- **Iteration Ceiling ($N_{\max} = 3$):** Quench Gate halt and developer escalation upon persistent compilation failure.

---

## 5. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `all_atomic_units_under_500_tokens == True`
- [ ] `tree_sitter_ast_shield_passed == True` (Zero tier crossings).
- [ ] `zero_subjective_fluff == True` (Zero ungrounded prose).
- [ ] Handoff Artifact: `artifacts/CONSTRUCTION_DELIVERABLE.manifest` sealed.
- [ ] State Persistence: Local commit prepared and Merkle hash calculated.

