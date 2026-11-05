# WF-005: Phase III — Verification & Adversarial Simulation Specification
## Pipeline Vector: `[Test] ───< 7 >───► [Simulation] ───< 8 >──► [Transition]`
*Macro Phase III: Materialization & Reality Gate (DoF = 0)*

---

## 1. TRIGGER CONTRACT & SCOPE BOUNDARY
- **Pre-condition:** Ingestion of staged atomic code diffs from `workflows/04_construction_worker.md`.
- **Primary Goal:** Execute mechanical deterministic test suites (`python verify.py --verify-all`), enforce Goodhart's law defenses, and subject deliverables to adversarial chaos and concurrency simulation (`INV-CRUCIBLE-CERTIFICATION`).
- **Degrees of Freedom (DoF):** 0 (Binary PASS/FAIL; zero subjective or heuristic leniency).
- **Resource Ceiling:** Test timeout $\le 60\text{s}$; simulation passes $k \ge 3$.

---

## 2. PIPELINE TOPOLOGY & NODE-SPRING MATRIX

```text
[EXECUTION] ────────< 6 >────────► [TEST] ────────< 7 >────────► [SIMULATION]
(Atomic Code)     (Regression Gate) (Deterministic) (Crucible Gate)  (Chaos / Race)
```

### A. Discrete Nodes `[]`
* **Node 7: `[Test / Test]` (Deterministic Empirical Verifier):**
  - Executes static analysis linters, type checkers, and mechanical gatekeeper scripts (`verify.py`).
  - Evaluates outputs against deterministic, binary Boolean assertions.
  - Strictly prohibits test skipping, conditional waivers, or heuristic passes.
* **Node 8: `[Simülasyon / Simulation]` (Adversarial Stress Harness):**
  - Injects parallel thread/process concurrency to detect race conditions and deadlocks.
  - Injects mutation testing suites and fuzzing payloads across boundary interfaces.
  - Empirically verifies that the Pre-Mortem failure modes (THESIS-036) cannot be triggered.

### B. Dialectic Springs `< >`
* **Spring `< 6 >` (Empirical Verification Gate):**
  - **Feed-Forward:** Do all unit tests, static analysis linters, and architectural invariant checks pass deterministically?
  - **Backpropagation:** On compilation or test failure, emit targeted compiler diagnostics and bounce back to `[Execution]` ($\Delta \theta$).
* **Spring `< 7 >` (Adversarial Simulation Crucible Gate):**
  - **Feed-Forward:** Does the deliverable maintain scale invariance and pre-mortem guarantees under chaotic multi-process stress?
  - **Backpropagation:** If race conditions, memory leaks, or unhandled exceptions emerge, return failure telemetry to `[Execution]`.
  - **Vertical Collapse Vector ($\Delta Z$):** If the failure exposes an unviable architecture, cascade vertically to Phase II (`CASCADE_COLLAPSE_TO_PHASE_2`).

---

## 3. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Baseline Integrity & Environment Lock
- [ ] Ingest staged code diff from `[Execution]`.
- [ ] Verify test harness environment integrity: Ensure test runners and linters are executing against clean, unpolluted sandbox.
- [ ] Confirm `verify.py` standard library independence.

### State 1: Deterministic Mechanical Test Suite (`< 6 >` / `[Test]`)
- [ ] Run full mechanical test suite: `python verify.py --verify-all`.
- [ ] Run unit and regression test matrices.
- [ ] Verify 100% binary PASS with 0 warnings and 0 skipped assertions.
- [ ] If any failure occurs: Bounce back to `[Execution]` with targeted diagnostic trace ($\Delta \theta$).

### State 2: Goodhart's Law Defense & Mock Demarcation
- [ ] Scan test suite for superficial mock gaming:
  - Mocking across core constitutional invariant boundaries is strictly prohibited (`[PROHIBITED]`).
  - Tests that pass without asserting concrete state delta are rejected (`REJECT_SUPERFICIAL_MOCKS`).
- [ ] Validate Ground-Truth Telemetry: Tests must assert against empirical ground truth defined in `problem_spec.md`.

### State 3: Adversarial Crucible & Chaos Simulation (`< 7 >` / `[Simulation]`)
- [ ] Concurrency Race Verification: Execute parallel threads/processes across shared state boundaries.
- [ ] Boundary & Fuzzing Stress: Ingest extreme payloads, null inputs, and pathological token sequences.
- [ ] Pre-Mortem Anti-Pattern Validation: Verify that none of the cataloged failure modes can be triggered under adversarial simulation.
- [ ] Repetition Invariant: Deliverable must survive $k \ge 3$ consecutive randomized stress passes without anomaly.

### State 4: Adversarial Crucible Certification
- [ ] Ratify adversarial crucible pass conforming to `INV-CRUCIBLE-CERTIFICATION`.
- [ ] Generate empirical test telemetry record.
- [ ] Hand off certified deliverable to `workflows/06_transition_release.md` through Spring `< 8 >`.

---

## 4. ADVERSARIAL EVALUATION & MURPHY STRESS FILTER

### A. Operational Invariants
- **Zero-Tolerance Regressions:** Even a single broken legacy test halts the entire pipeline immediately.
- **Flaky Test Elimination:** Intermittent passes are treated as deterministic failures.
- **Goodhart Shield:** If an agent modifies a test to make it pass without solving the underlying defect, the action is flagged as specification gaming (`REJECT_SPEC_GAMING`).

### B. Murphy Filter (Top Escape Vectors)
- **Escape Vector 1 (Mock Gaming):** Replacing external interfaces with empty stubs to claim 100% test coverage.
  - *Closure:* Prohibit mocks across core invariant boundaries; require end-to-end deterministic verification.
- **Escape Vector 2 (Flaky Release Pass):** Intermittent race condition passing test suite on lucky run.
  - *Closure:* Require $k \ge 3$ consecutive successful simulation passes before ratifying release.
- **Escape Vector 3 (Compiler Warning Suppression):** Suppressing linter warnings using directive comments.
  - *Closure:* Disallow warning suppression pragmas in new code diffs.

---

## 5. ANTI-RUMINATION GUARD & MULTI-LAYER VERTICAL COLLAPSE
- **Horizontal Micro-Oscillation Ceiling:**
  - `MAX_LOCAL_CYCLES = 3` ($N_{\max} = 3$) for local syntax, compiler, or unit test remediation.
- **Vertical Cascading Collapse Vectors ($\Delta Z$):**
  - **$\Delta Z = -1$ (Architectural Collapse):** If stress simulation exposes an unresolvable race condition, deadlocked state machine, or throughput cliff:
    - Trigger `CASCADE_COLLAPSE_TO_PHASE_2`.
    - Eject concrete code ballast; return to `workflows/03_elaboration_arch.md`.
  - **$\Delta Z = -2$ (Foundational Collapse):** If failure reveals that the target problem or metric baseline was fundamentally invalid:
    - Trigger `CASCADE_COLLAPSE_TO_PHASE_1`.
    - Purge all design and code artifacts; return to `workflows/01_triage_and_digest.md`.
- **Biological Primacy Escalation:** If total vertical cascade depth exceeds allowable energy budget $\to$ `ESCALATE_TO_HUMAN`.

---

## 6. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `mechanical_verify_py_passed == True` (10/10 gates green).
- [ ] `unit_test_matrix_passed == True` (100% pass, 0 skipped).
- [ ] `goodhart_mock_defense_verified == True` (Zero mocks across invariant boundaries).
- [ ] `adversarial_simulation_passed == True` (Survived $k \ge 3$ chaos passes).
- [ ] `pre_mortem_failure_modes_refuted == True` (Empirical immunity confirmed).
- [ ] Test telemetry sealed for transition release.
