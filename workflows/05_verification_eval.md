# WF-005: Verification & Quality Evaluation Workflow
## Scope: Mechanical Gatekeeper, Adversarial Stress Testing & DoD Audit (DoF = 0)
*Classical AUP Discipline: Test / Quality Assurance*

---

## 1. TRIGGER CONTRACT
- **Pre-condition:** Sealed `artifacts/CONSTRUCTION_DELIVERABLE.manifest` from WF-004.
- **Input Types:** Synthesized codebase diffs, test suites, FIR schemas, mutation matrices.
- **Degrees of Freedom (DoF):** 0 (Binary Boolean evaluation; PASS or FAIL exclusively).
- **Resource Ceiling:** 100 mutation iterations; max test execution latency $\le 500\text{ms}$ per test vector.

---

## 2. INNER MICRO-LOOP & STATE MACHINE (TRIAGE -> DIAGNOSE -> SOLVE)

### State 0: Mechanical Boundary Gatekeeper Turnstile
- [ ] Run `python verify.py --verify-all`.
  - Does any gate evaluate to FAIL?
  - YES: Halt immediately and log failure telemetry (`QUARANTINE_AND_LOG`).
  - NO: Proceed to State 1.

### State 1: Adversarial Twin Fuzzing & Mutation Attack
- [ ] Ingest deliverable into isolated Red-Team Adversarial Twin (`INV-CRUCIBLE-CERTIFICATION`).
- [ ] Dispatch Centennial Stress Suite:
  - 100 boundary mutation vectors (type poisoning, schema overflow, rapid concurrency, zero-values).
  - Verify that every unexpected anomaly trips safe-state degraded fallback (`CIRCUIT_BREAKER_HALT`).

### State 2: Latency & Thermodynamic Action Audit
- [ ] Measure execution latency across all critical paths:
  - Confirm every transaction completes within $\le 500\text{ms}$.
  - Confirm token dissipation conforms to the Principle of Least Action ($\delta S = 0$).

### State 3: Definition of Done (DoD) Forensic Cross-Examination
- [ ] Cross-examine deliverable against `domain/solution.md` acceptance criteria.
- [ ] Verify non-repudiation: Confirm zero untracked side-effects on disk.

---

## 3. EVALUATION & ADVERSARIAL GATE

### A. Writers' Room Focus
- **Architect:** Evaluates whether the test suite covers end-to-end integration without mock leakage.
- **Proceduralist:** Verifies 100/100 mutation survival score with zero flaky or indeterminate tests.
- **Scarred Senior:** Specifically targets race conditions, memory leaks under sustained load, and unhandled edge errors.

### B. Murphy Stress Filter
- **Escape Vector 1 (Mock Collusion):** Test assertions passing only because mock implementations bypass real business rules.
- **Escape Vector 2 (Flaky Concurrency):** Tests passing intermittently depending on CPU scheduling jitter.
- **Escape Vector 3 (Resource Leak under Pressure):** System crashing after sustained mutation cycles due to unclosed file handles.

---

## 4. BACKPROPAGATION & PLOTTER LOGIC
- **Horizontal Oscillation (Δθ Plotter):**
  - If isolated test flakiness or mock collusion detected: Plotter replaces mock with an empirical test fixture and re-executes State 1.
- **Inter-Layer Escalation Protocol (Vertical Dynamics - ΔZ):**
  - **Local Tolerance (Δθ):** Maximum 3 micro-oscillations within Phase 05.
  - **Macro Fracture Trigger:** If Murphy crucible fuzzing uncovers an unhandled race condition, memory leak under pressure, or structural deadlock:
    - *Local Code Regression:* Fall back to `workflows/04_construction_worker.md` with failing test vector.
    - *Keystone Architecture Fracture:* Revert altitude to `workflows/03_elaboration_arch.md`.
    - *Fundamental Specification Breach:* Deep vertical collapse to `workflows/02_inception_domain.md`.
  - **Pruning & Ballast Ejection:** Downstream artifacts built upon the broken keystone are discarded; failure telemetry is recorded in `stories/memories`.
- **Iteration Ceiling ($N_{\max} = 3$):** Quench Gate halt and developer escalation upon persistent verification failure.

---

## 5. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `verify_py_all_gates_pass == True` (Zero-code, No-BOM, parity verified).
- [ ] `adversarial_mutation_pass_rate == 1.0` (100/100 attacks survived).
- [ ] `p99_latency_within_bounds == True` ($\le 500\text{ms}$).
- [ ] Handoff Artifact: `artifacts/VERIFICATION_CERTIFICATE.json` cryptographically signed.
- [ ] State Persistence: `.state.json` updated with verification receipt.

