# WF-003: Elaboration & Architecture Workflow
## Scope: Architectural Skeleton, Keystone Isolation & Pre-Mortem Gates (DoF = 0)
*Classical AUP Discipline: Analysis & Design*

---

## 1. TRIGGER CONTRACT
- **Pre-condition:** Ratified `artifacts/SPEC_INCEPTION.md` from WF-002 with valid Merkle seal.
- **Input Types:** Living specification draft, system topology maps, API boundary schemas.
- **Degrees of Freedom (DoF):** 0 (Structural integrity; monolithic deviations prohibited).
- **Resource Ceiling:** Token window $\le 4000$; elaboration latency $\le 60\text{s}$.

---

## 2. INNER MICRO-LOOP & STATE MACHINE (TRIAGE -> DIAGNOSE -> SOLVE)

### State 0: Pre-Flight Requirement Verification
- [ ] Verify `SPEC_INCEPTION.md`: Are all requirements expressed in binary Boolean assertions?
  - NO: Backtrack immediately to WF-002 (Inception).
  - YES: Proceed to State 1.

### State 1: 3-Tier Structural Decomposition
- [ ] Decompose architecture into strictly bounded tiers (`INV-3-TIER-DECOMPOSITION`):
  1. **Application Shell (Orchestrator):** Global lifecycle, routing, and context providers.
  2. **Layouts (Skeleton Slots):** Wireframe frames, page layouts, and slot topologies.
  3. **Components (Composite & Atomic):** Stateless, reusable atomic units with phase-locked props.
- [ ] Reject any monolithic shortcut attempting to collapse tiers into single files (`REJECT_MONOLITHIC_COLLAPSE`).

### State 2: Keystone Component & Fracture Point Isolation
- [ ] Identify Keystone: Which single component carries the highest architectural stress and blast radius?
- [ ] Isolate Fracture Points: Map inter-component interfaces (events, props, APIs) to Bernstein kinematic synergy contracts.
- [ ] Enforce zero independent degrees of freedom across component joints (`REJECT_UNCONSTRAINED_JOINTS`).

### State 3: Pre-Mortem Anti-Pattern Formulation (Section 1.4 Gate)
- [ ] Catalog Top 3 Domain-Specific Failure Modes before code construction.
- [ ] Draft `### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)` prohibiting these modes via hard negative constraints (`[PROHIBITED]`).

---

## 3. EVALUATION & ADVERSARIAL GATE

### A. Writers' Room Focus
- **Architect:** Audits structural hierarchy for scale-invariant isomorphism ($\text{MSE} = 0$, macro-to-micro parity).
- **Proceduralist:** Verifies Section 1.4 Pre-Mortem Gate is syntactically present with explicit `[PROHIBITED]` clauses.
- **Scarred Senior:** Simulates cyclic deadlocks, state leakage between components, and Jenga-style cascade risks.

### B. Murphy Stress Filter
- **Escape Vector 1 (Jenga Cascade):** Failure of an atomic child component propagates upward and crashes the Application Shell.
- **Escape Vector 2 (Boundary Smuggling):** Business logic or database calls embedded within presentation layouts.
- **Escape Vector 3 (Unbounded Prop Sprawl):** Untyped dictionary payloads passed across component joints.

---

## 4. BACKPROPAGATION & PLOTTER LOGIC
- **Horizontal Oscillation (Δθ Plotter):**
  - If Jenga Cascade risk detected: Plotter inserts an isolation boundary / circuit-breaker fallback into State 2.
  - If Boundary Smuggling detected: Plotter refactors component contract in State 1 to enforce clean-room tier separation.
  - If Section 1.4 missing: Immediate mechanical rejection; return to State 3.
- **Inter-Layer Escalation Protocol (Vertical Dynamics - ΔZ):**
  - **Local Tolerance (Δθ):** Maximum 3 micro-oscillations within Phase 03.
  - **Macro Fracture Trigger:** If the Keystone component cannot be isolated or Section 1.4 Pre-Mortem analysis reveals an unresolvable systemic deadlock:
    - **Vertical Fallback Target (ΔZ):** Revert altitude to `workflows/02_inception_domain.md`.
    - **Pruning & Ballast Ejection:** Architectural models are discarded, and domain scope boundaries are contractually narrowed before re-attempting elaboration.
- **Iteration Ceiling ($N_{\max} = 3$):** Escalates to Biological Root of Trust upon persistent structural instability.

---

## 5. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `three_tier_decomposition_verified == True` (Shell, Layout, Component isolated).
- [ ] `section_1_4_pre_mortem_gate_present == True` (Top 3 failure modes prohibited with `[PROHIBITED]`).
- [ ] `bernstein_joint_dof == 0` (All props/events statically typed).
- [ ] Handoff Artifact: `artifacts/SPEC_ELABORATION.md` ratified.
- [ ] State Persistence: `.state.json` updated and Merkle commit SHA anchored.

