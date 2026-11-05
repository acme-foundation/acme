# WF-003: Phase II — Elaboration & Keystone Architecture Specification
## Pipeline Vector: `[Diagnostics] < 3 > [Solution] < 4 > [Evaluation] -> solution_contract.yaml`
*Macro Phase II: Synthesis & Adversarial Filter (DoF = 0)*

---

## 1. TRIGGER CONTRACT & SCOPE BOUNDARY
- **Pre-condition:** Ingestion of sealed `artifacts/problem_spec.md` from Macro Phase I.
- **Primary Goal:** Synthesize minimal keystone architecture, submit design to tripartite Writers' Room dialectic, catalog pre-mortem failure modes (THESIS-036), and seal `artifacts/solution_contract.yaml` with typed `.fir.json`.
- **Degrees of Freedom (DoF):** 0 (Finite structural contract; zero unanchored flexibility).
- **Resource Ceiling:** Token consumption $\le 2000$ tokens; review latency $\le 500\text{ms}$.

---

## 2. PIPELINE TOPOLOGY & NODE-SPRING MATRIX

```text
[DIAGNOSTICS] ────────< 3 >────────► [SOLUTION] ────────< 4 >────────► [EVALUATION]
(problem_spec.md)   (Occam's Razor)  (Keystone Arch)   (Rice & Murphy)  (solution_contract.yaml)
```

### A. Discrete Nodes `[]`
* **Node 3: `[Diagnostics]` (Ground Truth Spec Holder):**
  - Serves as the immutable boundary condition holding metric invariants and negative scope.
  - Does not invent architectural solutions or speculative features.
* **Node 4: `[Solution]` (Keystone Architect & Synthesizer):**
  - Decomposes systems according to the 3-Tier Structural Hierarchy (`INV-3-TIER-DECOMPOSITION`: Application Shell $\to$ Layouts $\to$ Components).
  - Isolates the Keystone Component (the single structural pivot whose failure compromises the system).
  - Enforces atomic unit sizing ($\le 500$ tokens per execution unit).
* **Node 5: `[Değerleme / Evaluation]` (Adversarial Crucible & Rice Gate):**
  - Submits architecture to the tripartite Writers' Room dialectic.
  - Compiles Formal Intermediate Representation (`.fir.json`) conforming to `INV-FORMAL-IR-GATE`.
  - Defines AST runtime intercept whitelist (`INV-RUNTIME-INTERCEPT`).

### B. Dialectic Springs `< >`
* **Spring `< 3 >` (Parsimony & Occam's Razor Gate):**
  - **Feed-Forward:** Does the synthesized architecture resolve *only* the invariants isolated in `problem_spec.md` with least action ($\delta S = 0$)?
  - **Backpropagation:** Rejects speculative utility functions, golden-hammer abstractions, or unanchored dependencies back to `[Solution]` (`REJECT_SPECULATIVE_STATE`).
  - **Homeostasis Check:** Protects downstream nodes from architectural bloat and cognitive overloading.
* **Spring `< 4 >` (Adversarial Crucible & Pre-Mortem Gate):**
  - **Feed-Forward:** Has the design achieved unanimous consensus across the tripartite Writers' Room and compiled into a type-checked Formal IR?
  - **Backpropagation:** If a scale-invariant failure mode, deadlocked state transition, or unmitigated Murphy vector is detected, reject back to `[Solution]` with an explicit prohibited constraint (`[PROHIBITED]`).
  - **Vertical Collapse Vector ($\Delta Z$):** If evaluation determines that the problem statement contains mathematically contradictory invariants, halt horizontal iteration and cascade vertically to Phase I (`CASCADE_COLLAPSE_TO_PHASE_1`).

---

## 3. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Problem Contract Ingestion & Integrity Lock
- [ ] Ingest `artifacts/problem_spec.md` from Phase I.
- [ ] Verify cryptographic Merkle signature and baseline metric anchors.
- [ ] Validate invariant bounds: Confirm $DoF = 0$ criteria and Negative Scope are explicitly defined.
- [ ] If input is corrupted or unsealed: Reject and return to Phase I (`EXIT_CODE_400`).

### State 1: 3-Tier Keystone Decomposition (`[Solution]`)
- [ ] Identify Keystone Component: The single structural pivot point whose failure causes systemic collapse.
- [ ] Enforce 3-Tier Structural Hierarchy:
  - Tier 1: Application Shell (Boundary routing, lifecycle context, security context).
  - Tier 2: Layouts / Workspaces (Subsystem containers, transactional boundaries).
  - Tier 3: Atomic Components (Leaf units $\le 500$ tokens).
- [ ] Apply Anti-Monolithic Constraint: Ban catch-all managers, god classes, and universal handlers (`INV-PRIMITIVE-ATTRACTOR-REFUTATION`).

### State 2: Parsimony & Invariant Gate (`< 3 >`)
- [ ] Zero Speculation Check: Confirm zero unrequested endpoints, helper methods, or speculative abstractions.
- [ ] Zero Adjective Density: Confirm design contains no subjective fluff ($Density \le 0.02$).
- [ ] Blast Radius Verification: Ensure the architecture does not penetrate boundaries beyond `problem_spec.md`.

### State 3: Dialectic Braintrust & Writers' Room Session (`[Evaluation]`)
- [ ] Convene Tripartite Writers' Room:
  - **Architect (Pragmatist):** Validates thermodynamic efficiency ($\delta S = 0$) and minimal dependency graph.
  - **Proceduralist (Kuralcı):** Validates type completeness, schema invariants, and statutory alignment.
  - **Stateful Senior (Yaralı Kıdemli):** Validates concurrency safety, state idempotence, and historical failure vectors.
- [ ] Unanimous Ratification: All three roles must issue binary PASS.

### State 4: Pre-Mortem Anti-Pattern Catalog (THESIS-036 / DoF = 0)
- [ ] Catalog Top 3 Scale-Invariant Failure Modes:
  - Failure Mode 1: Resource / buffer exhaustion under saturation.
  - Failure Mode 2: Concurrent race condition or cyclic state machine deadlock.
  - Failure Mode 3: Semantic schema drift or partial write split-brain.
- [ ] Formulate Hard Negative Constraints (`[PROHIBITED]`): Enforce explicit architectural guards eliminating each failure mode.

### State 5: Formal IR Derivation & Contract Seal (`solution_contract.yaml`)
- [ ] Derivation of Formal Intermediate Representation: Compile architecture into typed `.fir.json` schema (`INV-FORMAL-IR-GATE`).
- [ ] Specify Pre-conditions and Post-conditions for all execution units.
- [ ] Define AST Whitelist Shield: Map allowed system calls, file boundaries, and subprocess tokens (`INV-RUNTIME-INTERCEPT`).
- [ ] Seal `artifacts/solution_contract.yaml` with Merkle digest and pass to Macro Phase III.

---

## 4. ADVERSARIAL EVALUATION & MURPHY STRESS FILTER

### A. Writers' Room Operational Roles
- **Architect (Pragmatist):** "Does this design introduce any layer that cannot be justified by an explicit metric constraint in `problem_spec.md`?"
- **Proceduralist (Kuralcı):** "Are state transitions deterministically finite, fully typed, and verifiable via mathematical schema?"
- **Stateful Senior (Yaralı Kıdemli):** "Where does this lock up when the network drops 50% of packets, or when downstream disk fills to 100%?"

### B. Murphy Filter (Top Escape Vectors & Open Gap Budget)
- **Escape Vector 1 (Abstraction Laundering):** Hiding complexity behind deep inheritance or generic interfaces to fake simplicity.
  - *Closure:* Ban dynamic dispatch for core invariants; enforce static typed call paths.
- **Escape Vector 2 (Rice Undecidability Trap):** Formulating contracts that depend on semantic runtime behavior that cannot be statically determined.
  - *Closure:* Enforce syntax-level AST whitelists and finite-state transition tables.
- **Open Gap Budget Allocation:** Fatal architectural gaps are strictly banned; cosmetic or marginal bureaucratic nitpicks are assigned to open gap budget without over-engineering.

---

## 5. ANTI-RUMINATION GUARD & OSCILLATION LIMITS
- **Maximum Horizontal Cycles:** Clamped strictly to `MAX_LOCAL_CYCLES = 3` ($N_{\max} = 3$).
- **Vertical Cascading Collapse ($\Delta Z$):**
  - If `< 3 >` or `< 4 >` fails to converge within 3 cycles due to flawed problem framing:
    - Trigger `CASCADE_COLLAPSE_TO_PHASE_1`.
    - Eject speculative design ballast ($\delta S = 0$).
    - Revert altitude coordinate to `workflows/01_triage_and_digest.md`.
- **Base-Case Circuit Breaker:** If vertical collapses recur $\ge 2$ times across the same vector $\to$ `ESCALATE_TO_HUMAN`.

---

## 6. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `keystone_architecture_isolated == True`
- [ ] `3_tier_hierarchy_enforced == True` (Shell $\to$ Layout $\to$ Components).
- [ ] `pre_mortem_gates_ratified == True` (Top 3 failure modes banned under $DoF = 0$).
- [ ] `formal_ir_compiled == True` (`.fir.json` typed schema valid).
- [ ] `ast_shield_whitelist_defined == True` (`INV-RUNTIME-INTERCEPT`).
- [ ] `braintrust_unanimous_pass == True` (Architect, Proceduralist, Senior sign-off).
- [ ] `solution_contract_sealed == True` (`artifacts/solution_contract.yaml` committed).
