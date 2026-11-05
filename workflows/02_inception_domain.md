# WF-002: Inception & Domain Grounding Workflow
## Scope: Ontological Grounding, Problem/Solution Invariant Lock (DoF = 0)
*Classical AUP Discipline: Requirements*

---

## 1. TRIGGER CONTRACT
- **Pre-condition:** Verified `artifacts/triage_digest.md` with passing Merkle seal from WF-001 (`INV-SEQUENCE-PRECEDENCE`).
- **Input Types:** Triage digest, domain taxonomy definitions, system interface schemas.
- **Degrees of Freedom (DoF):** 0 (Ontological boundary; zero room for speculative divergence).
- **Resource Ceiling:** Token window $\le 3000$; formulation latency $\le 45\text{s}$.

---

## 2. INNER MICRO-LOOP & STATE MACHINE (TRIAGE -> DIAGNOSE -> SOLVE)

### State 0: Digest Integrity Verification
- [ ] Verify preceding digest seal: Does `triage_digest.md` contain an ungrounded claim?
  - YES: Backtrack immediately to WF-001.
  - NO: Proceed to State 1.

### State 1: Dual Domain Formalization (`problem.md` vs. `solution.md`)
- [ ] Inception of `domain/problem.md`:
  - Formalize ground-truth failure state.
  - Explicitly forbid referencing solution mechanisms inside `problem.md`.
- [ ] Inception of `domain/solution.md`:
  - Declare required system state transition.
  - Anchor transition to thermodynamic minimum action ($\delta S = 0$).

### State 2: Tacit-to-Metric Decompilation (5N1K Grid)
- [ ] Convert implicit operator adjectives into operational metric coordinates:
  - *"Scalable"* $\to$ Throughput $\ge X\text{ req/s}$ with $P_{99} \le Y\text{ms}$.
  - *"Secure"* $\to$ Zero unauthenticated endpoints; all parameters schema-validated.
  - *"Robust"* $\to$ Degraded fallback state reachable within $\le 200\text{ms}$.

### State 3: Living Specification Inception (`SPEC_INCEPTION.md`)
- [ ] Synthesize initial specification draft:
  - Pre-conditions, invariants, and Boolean acceptance gates.
  - Hard negative constraints (`[PROHIBITED]`, `DoF = 0`).

---

## 3. EVALUATION & ADVERSARIAL GATE

### A. Writers' Room Focus
- **Architect:** Ensures `solution.md` does not introduce accidental architectural complexity beyond minimal entropy.
- **Proceduralist:** Verifies strict separation between problem space and solution space (`INV-PLANE-SEPARATION`).
- **Scarred Senior:** Audits 5N1K metrics for realistic production boundary conditions.

### B. Murphy Stress Filter
- **Escape Vector 1 (Tautological Specification):** The specification defines the solution in terms of itself rather than verifiable ground truth.
- **Escape Vector 2 (Implicit Dependency Leak):** Hidden assumption of unverified third-party libraries or ambient runtime state.
- **Escape Vector 3 (Metric Gaming):** The metrics can be satisfied without actually solving the underlying domain pathology.

---

## 4. BACKPROPAGATION & PLOTTER LOGIC
- **Horizontal Oscillation (Δθ Plotter):**
  - If Metric Gaming detected: Plotter tightens acceptance criteria in State 2 with adversarial boundary assertions.
  - If Implicit Dependency Leak detected: Plotter enforces clean-room isolation; purge ambient assumptions.
  - If Tautological Specification detected: Plotter purges `solution.md` and backtracks to State 1.
- **Inter-Layer Escalation Protocol (Vertical Dynamics - ΔZ):**
  - **Local Tolerance (Δθ):** Maximum 3 micro-oscillations within Phase 02.
  - **Macro Fracture Trigger:** If Murphy evaluation proves that domain requirements cannot be satisfied without violating constitutional invariants (`INV-*`) or if the problem space contains unresolvable internal contradictions:
    - **Vertical Fallback Target (ΔZ):** Revert altitude to `workflows/01_triage_and_digest.md`.
    - **Pruning & Ballast Ejection:** Intermediate inception drafts are frozen, failure telemetry is logged to `stories/memories`, and raw operator intent is re-triaged.
- **Iteration Ceiling ($N_{\max} = 3$):** Escalates to Chief Architect if ontological invariants remain ungrounded.

---

## 5. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `domain_problem_file_sealed == True` (Zero solution leakage).
- [ ] `domain_solution_file_sealed == True` (Pure invariant transitions).
- [ ] `tacit_adjectives_count == 0` (All adjectives grounded in 5N1K metrics).
- [ ] Handoff Artifact: `artifacts/SPEC_INCEPTION.md` ratified.
- [ ] State Persistence: `.state.json` updated with Inception Merkle hash.

