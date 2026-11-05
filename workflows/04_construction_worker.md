# WF-004: Phase III — Construction Worker & Atomic Materialization Specification
## Pipeline Vector: `──< 5 >──► [Execution] ───< 6 >──► [Test]`
*Macro Phase III: Materialization & Reality Gate (DoF = 0)*

---

## 1. TRIGGER CONTRACT & SCOPE BOUNDARY
- **Pre-condition:** Ingestion of sealed `artifacts/solution_contract.yaml` and typed `.fir.json` emitted by Macro Phase II.
- **Primary Goal:** Materialize surgical, atomic code diffs under the AST Runtime Intercept Shield (`INV-RUNTIME-INTERCEPT`) adhering strictly to the 3-Tier hierarchy with zero conversational fluff and bounded unit sizing ($\le 500$ tokens).
- **Degrees of Freedom (DoF):** 0 (Exact adherence to contract; zero unanchored refactoring).
- **Resource Ceiling:** Token consumption $\le 1500$ tokens per atomic unit; AST intercept check $\le 100\text{ms}$.

---

## 2. PIPELINE TOPOLOGY & NODE-SPRING MATRIX

```text
[EVALUATION] ────────< 5 >────────► [EXECUTION] ────────< 6 >────────► [TEST]
(solution_contract) (AST Shield)    (Atomic Worker)     (Compiler Gate)  (Empirical Test)
```

### A. Discrete Nodes `[]`
* **Spring `< 5 >` (Transition & AST Intercept Shield):**
  - Verifies cryptographic signature of `solution_contract.yaml`.
  - Arms system call and subprocess whitelist: blocks unapproved file access, network calls, or dangerous terminal commands (`INV-RUNTIME-INTERCEPT`).
* **Node 6: `[İcra / Execution]` (Atomic Materializer / Construction Worker):**
  - Decomposes solution contract into atomic, ordered implementation units.
  - Generates code diffs bounded strictly to $\le 500$ tokens per unit.
  - Enforces zero unanchored refactoring: untouched adjacent modules must NOT be formatted or restructured.
* **Spring `< 6 >` (Empirical Verification Gate):**
  - Connects materializer to deterministic test harness (`verify.py --verify-all` and downstream test runner).

---

## 3. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Contract Verification & AST Shield Activation (`< 5 >`)
- [ ] Ingest `artifacts/solution_contract.yaml` and verified `.fir.json`.
- [ ] Arm AST Shield Whitelist: Lock down permitted system calls, shell commands, and file paths (`INV-RUNTIME-INTERCEPT`).
- [ ] Working Directory Cleanliness Check: Ensure zero unstaged or contaminated files exist before editing.

### State 1: Atomic Unit Deconstruction
- [ ] Deconstruct contract into an ordered queue of atomic units ($U_1, U_2, \dots, U_k$).
- [ ] Validate Unit Size Ceiling: Confirm each execution unit is bounded:
  $$\text{Unit Size} \le 500\text{ tokens}$$
- [ ] If any unit exceeds 500 tokens: Reject and subdivide before authoring.

### State 2: Surgical Construction & Strict Whitelist Enforcement
- [ ] Materialize code diffs exclusively within the whitelisted file paths.
- [ ] Zero Adjective Invariant: Code comments and commit annotations must be zero-fluff and descriptive (Adjective density $\le 0.02$).
- [ ] Pure Architecture Invariant: Core repository retains pure NLP specification status; executable scripts are confined strictly to downstream projects or `verify.py`.

### State 3: Local Diff Integrity Seal
- [ ] Check for accidental formatting diffs, line-ending corruption, or BOM injection.
- [ ] Verify that diff modifies *only* the minimal lines required to satisfy the unit contract.
- [ ] Hand off materialized diff to `workflows/05_verification_sim.md` through Spring `< 6 >`.

---

## 4. ADVERSARIAL EVALUATION & MURPHY STRESS FILTER

### A. Construction Guardrails
- **Scope Creep Guard:** If the worker attempts to touch files outside `solution_contract.yaml`, AST Shield triggers immediate termination (`AST_SCOPE_BREACH_HALT`).
- **Formatting Pollution Guard:** Full-file reformatting or stylistic sweeps are prohibited; only targeted lines may be touched.
- **Speculative Helper Guard:** Writing utility functions "for future use" is prohibited (`REJECT_SPECULATIVE_STATE`).

### B. Murphy Filter (Top Escape Vectors)
- **Escape Vector 1 (Silent AST Bypass):** Invoking unmonitored sub-shells or dynamic `eval()` calls.
  - *Closure:* Static AST analysis flags and rejects dynamic execution calls at pre-flight.
- **Escape Vector 2 (Mega-Patch Smuggling):** Bundling multiple conceptual fixes into a single 2000-token blob.
  - *Closure:* Enforce strict hard stop at 500 tokens per patch.
- **Escape Vector 3 (Fluff Injection):** Filling commit messages or comments with conversational explanations.
  - *Closure:* Semantic fluff gatekeeper rejects adjectives.

---

## 5. ANTI-RUMINATION GUARD & OSCILLATION LIMITS
- **Local Micro-Oscillation ($\Delta \theta$):**
  - Syntax errors or minor patch rejections bounce across Spring `< 6 >`. Clamped at `MAX_LOCAL_CYCLES = 3`.
- **Vertical Cascading Collapse ($\Delta Z$):**
  - If atomic materialization cannot be completed without breaching contract constraints:
    - Trigger `CASCADE_COLLAPSE_TO_PHASE_2`.
    - Eject concrete code ballast ($\delta S = 0$).
    - Revert altitude coordinate to `workflows/03_elaboration_arch.md`.
- **Biological Primacy:** If worker deadlocks across multiple units $\to$ `ESCALATE_TO_HUMAN`.

---

## 6. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `ast_shield_armed == True` (`INV-RUNTIME-INTERCEPT` active).
- [ ] `atomic_unit_size_bounded == True` ($\le 500$ tokens per unit).
- [ ] `zero_unanchored_refactoring == True` (Untouched modules unpolluted).
- [ ] `adjective_density <= 0.02` (Zero subjective fluff in comments/code).
- [ ] `core_zero_code_preserved == True` (Core ACME repo retains pure NLP status).
- [ ] Diffs staged cleanly for empirical verification.
