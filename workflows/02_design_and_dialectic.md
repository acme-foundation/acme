# WF-002: Phase II — Design & Dialectic Gate Workflow Contract
## Pipeline Vector: `[Diagnostics] < 3 > [Solution] < 4 > [Evaluation] -> solution_contract.yaml`
*Macro Phase II: Design & Dialectic Gate (DoF = 0)*

---

## 1. PIPELINE TOPOLOGY & NODE-SPRING MATRIX

```text
[DIAGNOSTICS] ───< 3 >───► [SOLUTION] ───< 4 >───► [EVALUATION] ───► [OUTPUT: solution_contract.yaml]
(problem_spec.md)       (Keystone Arch)       (Dialectic Crucible)
```

### A. Discrete Nodes `[]` (Local State Keepers)
* **Node 2: `[Diagnostics]` (Incoming Ground Truth Spec):**
  - **Scope:** Ingests the sealed `artifacts/problem_spec.md` delivered by Phase I.
  - **Responsibility:** Serves as the immutable boundary condition. Holds 5N1K ground truth, metric baselines, and blast radius limits. Node 2 does not invent architectural solutions or speculative features.
* **Node 3: `[Solution]` (Keystone Architecture & Synthesis Worker):**
  - **Scope:** Synthesizes the minimal architectural topology required to satisfy `problem_spec.md`.
  - **Responsibility:** Decomposes systems according to the 3-Tier Structural Hierarchy (`INV-3-TIER-DECOMPOSITION`: Application Shell $\to$ Layouts $\to$ Components). Bounded by atomic sizing ($\le 500$ tokens per unit). Strictly prohibits premature abstraction and monolithic attractors (`INV-PRIMITIVE-ATTRACTOR-REFUTATION`).
* **Node 4: `[Evaluation]` (Adversarial Crucible & Dialectic Gate):**
  - **Scope:** Submits candidate architecture to tripartite peer dialectic, pre-mortem failure mode cataloging (THESIS-036), and AST safety verification (`INV-RUNTIME-INTERCEPT`).
  - **Responsibility:** Compiles and seals `artifacts/solution_contract.yaml` and typed formal intermediate representations (`.fir.json`).

### B. Dialectic Springs `< >` (Braintrust & Murphy Membranes)
* **Spring `< 3 >` (Parsimony & Invariant Gate - Occam's Razor):**
  - **Feed-Forward:** Does the synthesized architecture resolve *only* the invariants isolated in `problem_spec.md` with least action ($\delta S = 0$)?
  - **Backpropagation:** If solution leaks speculative utility functions, golden-hammer frameworks, or unanchored dependencies, reject back to `[Solution]` (`REJECT_SPECULATIVE_STATE`).
  - **Homeostasis Check:** Protects downstream nodes from architectural bloat and cognitive overloading.
* **Spring `< 4 >` (Adversarial Crucible & Rice Gate):**
  - **Feed-Forward:** Has the design achieved unanimous consensus across the tripartite Writers' Room and compiled into a type-checked Formal IR (`INV-FORMAL-IR-GATE`)?
  - **Backpropagation:** If a scale-invariant failure mode, deadlocked state transition, or unmitigated Murphy vector is detected, reject back to `[Solution]` with an explicit prohibited constraint (`[PROHIBITED]`).
  - **Vertical Collapse Vector ($\Delta Z$):** If evaluation determines that the problem statement contains mathematically contradictory invariants, halt horizontal iteration and cascade vertically to Phase I (`CASCADE_COLLAPSE_TO_PHASE_1`).

---

## 2. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Problem Contract Ingestion & Integrity Lock
- [ ] Ingest `artifacts/problem_spec.md` from Phase I.
- [ ] Verify cryptographic Merkle signature and baseline metrics.
- [ ] Validate invariant bounds: Confirm $DoF = 0$ criteria are explicitly defined.
- [ ] If input is corrupted or unsealed: Reject and return to Phase I (`EXIT_CODE_400`).

### State 1: 3-Tier Keystone Decomposition (`[Solution]`)
- [ ] Identify Keystone Component: The single structural pivot point whose failure causes systemic collapse.
- [ ] Enforce 3-Tier Structural Hierarchy:
  - Tier 1: Application Shell (Boundary routing, lifecycle context, security context).
  - Tier 2: Layouts / Workspaces (Subsystem containers, transactional boundaries).
  - Tier 3: Atomic Components (Leaf units $\le 500$ tokens).
- [ ] Apply Anti-Monolithic Constraint: Ban catch-all managers, god classes, and universal handlers.

### State 2: Parsimony & Invariant Gate (`< 3 >`)
- [ ] Zero Speculation Check: Confirm zero unrequested endpoints, helper methods, or speculative abstractions.
- [ ] Zero Adjective Density: Confirm design contains no subjective fluff ($Density \le 0.02$).
- [ ] Blast Radius Verification: Ensure the architecture does not penetrate boundaries beyond `problem_spec.md`.

### State 3: Dialectic Braintrust & Writers' Room Session (`[Evaluation]`)
- [ ] Convene Tripartite Writers' Room:
  - Architect: Validates thermodynamic efficiency and minimal dependency graph.
  - Proceduralist: Validates type completeness, schema invariants, and statutory alignment.
  - Stateful Senior: Validates concurrency safety, state idempotence, and historical failure vectors.
- [ ] Unanimous Ratification: All three roles must issue binary PASS.

### State 4: Pre-Mortem Anti-Pattern Catalog (THESIS-036 / DoF = 0)
- [ ] Catalog Top 3 Scale-Invariant Failure Modes:
  - Failure Mode 1: Resource / buffer exhaustion under saturation.
  - Failure Mode 2: Concurrent race condition or cyclic state machine deadlock.
  - Failure Mode 3: Semantic schema drift or partial write split-brain.
- [ ] Formulate Hard Negative Constraints (`[PROHIBITED]`): Enforce explicit architectural guards eliminating each failure mode.

### State 5: Formal IR Derivation & Contract Seal (`solution_contract.yaml`)
- [ ] Derivation of Formal Intermediate Representation: Compile architecture into typed `.fir.json` schema.
- [ ] Specify Pre-conditions and Post-conditions for all execution units.
- [ ] Define AST Whitelist Shield: Map allowed system calls, file boundaries, and subprocess tokens (`INV-RUNTIME-INTERCEPT`).
- [ ] Seal `artifacts/solution_contract.yaml` with Merkle digest.

---

## 3. ADVERSARIAL EVALUATION & MURPHY STRESS FILTER

### A. Writers' Room Dialectic Profiles
- **Architect (Pragmatist):** "Does this design introduce any layer that cannot be justified by an explicit metric constraint in `problem_spec.md`?"
- **Proceduralist (Kuralcı):** "Are state transitions deterministically finite, fully typed, and verifiable via mathematical schema?"
- **Scarred Senior (Stateful Worker):** "Where does this lock up when the network drops 50% of packets, or when downstream disk fills to 100%?"

### B. Murphy Filter (Top Escape Vectors)
- **Escape Vector 1 (Abstraction Laundering):** Hiding complexity behind deep inheritance or generic interfaces to fake simplicity.
  - *Closure:* Ban dynamic dispatch for core invariants; enforce static typed call paths.
- **Escape Vector 2 (Rice Undecidability Trap):** Formulating contracts that depend on semantic runtime behavior that cannot be statically determined.
  - *Closure:* Enforce syntax-level AST whitelists and finite-state transition tables.
- **Escape Vector 3 (Phantom Safety):** Asserting safety through unexecuted unit tests or mock stubs.
  - *Closure:* Bind verification to empirical execution under adversarial conditions.

---

## 4. ANTI-RUMINATION GUARD & OSCILLATION LIMITS

```text
  [Diagnostics] ◄──(Occam / Murphy)──► [Solution] ◄──(Dialectic / Rice)──► [Evaluation]
        │                                  │                                   │
        ▼                                  ▼                                   ▼
  (Phase I Base)                    (Local Cycle)                       (Local Cycle)
```

- **Maximum Horizontal Cycles:** `MAX_LOCAL_CYCLES = 3` ($N_{\max} = 3$).
  - If Spring `< 3 >` or `< 4 >` fails to converge within 3 iterations, horizontal oscillation terminates immediately.
- **Vertical Cascading Collapse ($\Delta Z$):**
  - If the failure stems from an invalid or self-contradictory problem definition:
    - Trigger `CASCADE_COLLAPSE_TO_PHASE_1`.
    - Eject speculative design ballast ($\delta S = 0$).
    - Revert altitude coordinate to `workflows/01_sense_making.md`.
- **Base-Case Circuit Breaker:**
  - If consecutive vertical collapses exceed 2 iterations:
    - Trigger `ESCALATE_TO_HUMAN` (Biological Primacy).
    - Freeze workspace state; output comprehensive forensic telemetry log.

---

## 5. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `keystone_architecture_isolated == True`
- [ ] `3_tier_hierarchy_enforced == True` (Shell $\to$ Layout $\to$ Components).
- [ ] `pre_mortem_gates_ratified == True` (Top 3 failure modes banned under $DoF = 0$).
- [ ] `formal_ir_compiled == True` (`.fir.json` typed schema valid).
- [ ] `ast_shield_whitelist_defined == True` (`INV-RUNTIME-INTERCEPT`).
- [ ] `adjective_density <= 0.02` (Zero subjective fluff).
- [ ] `solution_contract_sealed == True` (`artifacts/solution_contract.yaml` committed).
- [ ] State Persistence: Telemetry record updated and cryptographic Merkle root recorded.
