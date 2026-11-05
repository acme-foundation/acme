# WF-000: E-AUP Meta-Workflow Architecture & Conical Vortex Specification
## Scope: Universal 9-Node Pipeline Governance, 3D Helical Vortex & Dual-Scale Plotter Protocol (DoF = 0)

---

## 1. TRIGGER CONTRACT & SCOPE BOUNDARY
- **Pre-condition:** Invocation of any Evolutionary Agent-Based Unified Process (E-AUP) phase or downstream project adoption manifest (`.norm`).
- **Input Types:** Architectural directives, telemetry streams, incident triage records, or formal change proposals.
- **Degrees of Freedom (DoF):** 0 (Normative Lex Superior; invariants cannot be relaxed or bypassed).
- **Resource Ceiling:** Global iteration cap $N_{\max} = 3$ per discrete station; latency $\le 500\text{ms}$ per verification evaluation pass.
- **Strict Invariant (Decontamination & Signal Filtering):** All historical narrative, anecdotal noise, and conversational chatter evaluate as pure entropic noise (`ENTROPIC_NOISE`). The core specification compiles exclusively from empirical systems engineering signals, mathematical invariants, and reproducible telemetry.

---

## 2. THE 9-NODE CANONICAL PIPELINE VECTOR

The universal execution pipeline consists of 9 discrete state-keeping nodes (`[]`) coupled via 8 bidirectional dialectic spring membranes (`<>`):

```text
[Girdi] < 1 > [Triyaj] < 2 > [Tahlil] < 3 > [Çözüm] < 4 > [Değerleme] < 5 > [İcra] < 6 > [Test] < 7 > [Simülasyon] < 8 > [Çıkış]
 [Input]       [Triage]      [Diagnostics]   [Solution]     [Evaluation]     [Execution]    [Test]       [Simulation]      [Output]
```

### A. Discrete Nodes `[]` (Local State Keepers)
Each discrete node is an insulated action cell with strictly bounded local responsibility. Nodes do NOT perform existential or global systemic philosophy; they execute local state transitions:
1. **Node 1: `[Girdi / Input]` (Intake Receiver):** Ingests raw telemetry, defect tickets, or operator commands with zero speculative modification.
2. **Node 2: `[Triyaj / Triage]` (Ontological Decompiler):** Identifies target entity Telos (core purpose) and demarcates surface symptoms from underlying structural pathology (`INV-DIAGNOSTIC-TRIAGE`).
3. **Node 3: `[Tahlil / Diagnostics]` (Boundary & Invariant Engine):** Quantifies observable defects against empirical baselines ($P_{99}$, error codes, memory offsets) and bounds maximum blast radius.
4. **Node 4: `[Çözüm / Solution]` (Keystone Architect & Synthesizer):** Generates candidate architectural topology adhering strictly to the 3-Tier Structural Hierarchy (`INV-3-TIER-DECOMPOSITION`: Application Shell $\to$ Layouts $\to$ Components) and atomic unit sizing ($\le 500$ tokens).
5. **Node 5: `[Değerleme / Evaluation]` (Adversarial Crucible & Rice Gate):** Submits candidate design to the tripartite Writers' Room dialectic and pre-mortem failure mode cataloging (THESIS-036).
6. **Node 6: `[İcra / Execution]` (Atomic Materializer / Construction Worker):** Synthesizes concrete atomic diffs under the AST Runtime Intercept Shield (`INV-RUNTIME-INTERCEPT`).
7. **Node 7: `[Test / Test]` (Deterministic Empirical Verifier):** Executes mechanical test suites (`verify.py --verify-all`), type checkers, and unit contracts to reach a binary PASS/FAIL verdict.
8. **Node 8: `[Simülasyon / Simulation]` (Adversarial Stress Harness):** Injects chaos, race conditions, edge fuzzing, and mutation suites (`INV-CRUCIBLE-CERTIFICATION`) to refute Goodhart's law evasion.
9. **Node 9: `[Çıkış / Output]` (Terminal Seal & Scar Tissue Integrator):** Cleanses workspace, validates No-BOM UTF-8, verifies SemVer monotonic lock, commits cryptographic Merkle digest, and updates institutional scar tissue.

---

## 3. THE 3 MACRO PHASE PACKAGING

To eliminate cognitive overload and prevent agentic thrashing, the 9-node pipeline is partitioned into 3 sequential, closed-loop Macro Phases. Downstream phases cannot initialize until upstream phase contracts are cryptographically sealed.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MACRO PHASE I: SENSE-MAKING & DIAGNOSTICS (Anlama & Teşhis)                            │
│ Pipeline: [Input] ───< 1 >───► [Triage] ───< 2 >───► [Diagnostics]                    │
│ Target Workflows: 01_triage_and_digest.md, 02_inception_domain.md                      │
│ Primary Deliverable: artifacts/problem_spec.md (Zero Solution Leakage)                │
└────────────────────────────────────────┬───────────────────────────────────────────────┘
                                         ▼ (problem_spec.md Handoff)
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MACRO PHASE II: SYNTHESIS & ADVERSARIAL FILTER (Sentez & Süzgeç)                       │
│ Pipeline: [Diagnostics] ───< 3 >───► [Solution] ───< 4 >───► [Evaluation]              │
│ Target Workflows: 03_elaboration_arch.md                                               │
│ Primary Deliverable: artifacts/solution_contract.yaml + .fir.json (Writers' Room Pass) │
└────────────────────────────────────────┬───────────────────────────────────────────────┘
                                         ▼ (solution_contract.yaml Handoff)
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MACRO PHASE III: MATERIALIZATION & REALITY GATE (Maddileşme & Gerçeklik)               │
│ Pipeline: ──< 5 >──► [Execution] ───< 6 >───► [Test] ───< 7 >───► [Simulation] ──< 8 > │
│ Target Workflows: 04_construction_worker.md, 05_verification_sim.md,                   │
│                   06_transition_release.md, 07_backpropagation.md                      │
│ Primary Deliverable: Ratified Code Diff, verify.py PASS, Merkle Seal, Scar Tissue Log  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### A. Phase I: Sense-Making & Diagnostics (Düğümler 1-3)
- **Scope:** Ingests raw signal, filters entropic noise, extracts invariants, and formulates the ground-truth problem definition.
- **Contract Boundary:** Strictly prohibits solution formulation, speculative code, or implementation bias.
- **Handoff Artifact:** Sealed `artifacts/problem_spec.md`.

### B. Phase II: Synthesis & Adversarial Filter (Düğümler 3-5)
- **Scope:** Synthesizes minimal keystone architecture, verifies parsimony, and subjects candidate design to the tripartite Writers' Room (Architect, Proceduralist, Stateful Senior) and Murphy stress vectors.
- **Contract Boundary:** Pre-mortem gates (THESIS-036) must catalog the top 3 domain failure modes and establish hard negative constraints (`[PROHIBITED]`, $DoF = 0$).
- **Handoff Artifact:** Sealed `artifacts/solution_contract.yaml` and typed `.fir.json`.

### C. Phase III: Materialization & Reality Gate (Düğümler 5-9)
- **Scope:** Arms AST whitelist shield, generates atomic code units ($\le 500$ tokens), executes deterministic verification, subjects outputs to adversarial chaos simulation, and seals the deliverable with cryptographic provenance.
- **Contract Boundary:** Mock tests across core invariant boundaries are prohibited; zero unhandled regressions permitted.
- **Handoff Artifact:** Merkle-signed Git commit, SemVer tag, and updated institutional memory (`scar_tissue`).

---

## 4. THE CONICAL VORTEX TOPOLOGY (3D HELICAL DYNAMICS)

The software synthesis space is a **Conical Vortex** parameterized in cylindrical coordinates $(r, \theta, Z)$:

```text
                  ▲ Z (Altitude: Sovereign Abstract Intent -> Concrete Physical Artifact)
                  │
        (Apex)    •  MACRO PHASE I: SENSE-MAKING (r=1..2)
                 / \   [Input] < 1 > [Triage] < 2 > [Diagnostics]
                / S \
               /  P  \  MACRO PHASE II: SYNTHESIS & ADVERSARIAL FILTER (r=3)
              /   I   \   [Diagnostics] < 3 > [Solution] < 4 > [Evaluation]
             /    R    \
            /     A     \  MACRO PHASE III: MATERIALIZATION & REALITY (r=4..5)
           /      L      \   [Execution] < 6 > [Test] < 7 > [Simulation] < 8 > [Output]
          /_______________ \
                  r ──► (Radius: Scope, Token Budget, Complexity & Attack Surface)
```

### Coordinate Governance:
1. **$\theta$ (Angular Micro-Loop - $0^\circ \to 360^\circ$):** Intra-node and intra-phase circular traversal through the 4 internal stations: **Triage $\to$ Diagnose $\to$ Solve $\to$ Evaluate**.
2. **$r$ (Radial Coordinate - Scope & Kinetic Energy):** Expands monotonically from the apex ($r_0$, minimal tokens, zero code, pure intent) toward the base ($r_{\max}$, full test surface, integration matrix, adversarial chaos injection).
3. **$Z$ (Vertical Altitude - Ontological Depth):** Governs descent from abstract natural language requirements at the apex down to concrete, machine-verified, and ratified deliverables at the base.

---

## 5. DIALECTIC SPRING PROTOCOL (`< >`)

Every dialectic spring membrane operates as an active, three-vector immunological filter:
1. **Feed-Forward:** Purity and schema compliance verification before downstream ingestion.
2. **Feedback / Backpropagation (Murphy):** Upstream pushback when invariants, assumptions, or bounds are breached.
3. **Homeostasis & Telos Verification:** Continuous autonomous self-check: *"Does this transition serve the root constitutional purpose (Telos) with least action ($\delta S = 0$), or does it generate speculative entropy?"*

```text
  [NODE N] ──────(Feed-Forward: Purity & Schema Pass)──────► [NODE N+1]
     ▲                                                           │
     │◄──────(Feedback / Murphy: Pushback & Constraint)──────────┤
     │                                                           │
     └────────(Homeostasis: Telos & Least Action Audit)──────────┘
```

### Discrete Spring Invariants:
* **Spring `< 1 >` (Toxin Shield & High-Pass Noise Attenuator):**
  - *Location:* Between `[Input]` and `[Triage]`.
  - *Action:* High-pass filters conversational fluff, panic chatter, and subjective qualifiers (*"urgent"*, *"broken"*, *"slow"*). Emits `REJECT_UNANCHORED_INTENT` on non-compliant payloads.
* **Spring `< 2 >` (Quantification & Metric Invariant Gate):**
  - *Location:* Between `[Triage]` and `[Diagnostics]`.
  - *Action:* Asserts that every diagnosed defect maps to reproducible, ground-truth telemetry ($P_{99}$, latency, error codes, memory offsets). Enforces `INV-DIAGNOSTIC-TRIAGE` ($DoF = 0$).
* **Spring `< 3 >` (Parsimony & Occam's Razor Gate):**
  - *Location:* Between `[Diagnostics]` and `[Solution]`.
  - *Action:* Rejects speculative utility functions, golden-hammer frameworks, and unrequested abstraction layers (`REJECT_SPECULATIVE_STATE`). Enforces minimal action ($\delta S = 0$).
* **Spring `< 4 >` (Adversarial Crucible & Pre-Mortem Gate):**
  - *Location:* Between `[Solution]` and `[Evaluation]`.
  - *Action:* Submits architecture to the tripartite Writers' Room. Validates Rice Theorem decidability and catalogs top 3 scale-invariant failure modes (THESIS-036).
* **Spring `< 5 >` (Phase Handoff & AST Boundary Shield):**
  - *Location:* Between `[Evaluation]` and `[Execution]`.
  - *Action:* Ingests `artifacts/solution_contract.yaml`, compiles typed `.fir.json` schema (`INV-FORMAL-IR-GATE`), and arms AST execution whitelist shield (`INV-RUNTIME-INTERCEPT`).
* **Spring `< 6 >` (Deterministic Empirical Verification Gate):**
  - *Location:* Between `[Execution]` and `[Test]`.
  - *Action:* Runs mechanical verifier (`python verify.py --verify-all`), type checkers, and unit contracts. Compiler or syntax errors bounce back to `[Execution]` ($\Delta \theta$).
* **Spring `< 7 >` (Adversarial Simulation Crucible Gate):**
  - *Location:* Between `[Test]` and `[Simulation]`.
  - *Action:* Executes multi-threaded race simulation, chaos fault injection, and mutation testing (`INV-CRUCIBLE-CERTIFICATION`). Defends against Goodhart's law (tests passing through superficial mocks).
* **Spring `< 8 >` (Release Mühür & Decontamination Seal):**
  - *Location:* Between `[Simulation]` and `[Output]`.
  - *Action:* Purges ephemeral ballast, verifies UTF-8 No-BOM standard, confirms zero-code status in core repository, enforces SemVer monotonic lock, and records institutional scar tissue.

---

## 6. BRAKES, CONSTRAINTS & ESCALATION PROTOCOLS

```text
                                [PHASE I: SENSE-MAKING]
                                           ▲
                                           │  ΔZ = -2 (Foundational Diagnostic Error)
                                           │
                              [PHASE II: SYNTHESIS & FILTER]
                                           ▲
                                           │  ΔZ = -1 (Architectural / Structural Failure)
                                           │
  [Execution] ◄──(Compiler / verify.py)──► [Test] ◄──(Chaos / Race)──► [Simulation]
       │                                     │                             │
       ▼                                     ▼                             ▼
 (Local Cycle)                         (Local Cycle)                 (Local Cycle)
  Δθ <= 3                               Δθ <= 3                       Δθ <= 3
```

### A. Intra-Phase Horizontal Oscillation Ceiling (`MAX_LOCAL_CYCLES = 3`)
- The maximum permissible oscillation count across any planar spring interface is strictly clamped:
  $$\text{Cycle Count} \le N_{\max} = 3$$
- If a spring fails to converge within 3 iterations, horizontal looping terminates unconditionally.
- Autonomous thrashing or rumination is strictly prohibited (`REJECT_INFINITE_RUMINATION`).

### B. Vertical Cascading Collapse (Altitude Regress - $\Delta Z$)
- **Strict Invariant:** On root invariant breach or false keystone identification, local patching of leaf code is prohibited as entropy dissipation (`PROHIBIT_LOCAL_PATCHING_ON_ROOT_BREACH`).
- The system must lose altitude and regress vertically:
  - **$\Delta Z = -1$ (Architectural Collapse):** When Phase III testing or simulation reveals a concurrent race condition, deadlock, or throughput cliff rooted in architectural design $\to$ Collapse to Phase II (`03_elaboration_arch.md`).
  - **$\Delta Z = -1$ (Teleological Collapse):** When Phase II evaluation reveals that target invariants are mathematically contradictory $\to$ Collapse to Phase I (`01_triage_and_digest.md`).
  - **$\Delta Z = -2$ (Foundational Collapse):** When empirical execution in Phase III proves that baseline problem telemetry was invalid $\to$ Collapse directly to Phase I (`01_triage_and_digest.md`).
- **Thermodynamic Ballast Ejection:** Upon vertical collapse, all downstream speculative code diffs, temporary configurations, and synthetic artifacts generated under the false keystone are purged immediately to preserve least action ($\delta S = 0$).

### C. Open Gap Budget & Murphy Economics (Açık Kapı Bütçesi)
- **Fatal Gaps:** Vulnerabilities, deadlocks, or schema drifts that compromise constitutional invariants or cause systemic collapse are classified as fatal. They MUST be codified as hard negative constraints (`[PROHIBITED]`, $DoF = 0$).
- **Marginal / Aesthetic Gaps:** Bureaucratic nitpicks, speculative edge scenarios with zero empirical frequency, or stylistic preferences whose remediation cost exceeds operational utility are allocated to a conscious open-gap budget.
- Over-engineering is prohibited (`PROHIBIT_OVER_ENGINEERING`).

### D. Biological Primacy Escalation (`ESCALATE_TO_HUMAN`)
- If horizontal cycles exceed $N_{\max} = 3$ without convergence, or if vertical collapse recurs $\ge 2$ times across the same operational vector:
  - Autonomous loops halt immediately (`HALT_AND_FREEZE`).
  - System compiles verifiable forensic telemetry and escalates state to the Biological Root of Trust.

---

## 7. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Acute Hemostasis & Circuit Breaker
- [ ] Is there an active infinite loop, OOM condition, thermal quota breach, or unhandled crash?
  - YES: Trip Circuit Breaker immediately (`CIRCUIT_BREAKER_HALT`). Throttle I/O, apply temporary tourniquet. Defer root cause analysis.
  - NO: Proceed to State 1.

### State 1: Ingestion & Teleological Framing
- [ ] Ingest operational signal through Spring `< 1 >`.
- [ ] Filter subjective adjectives, emotional markers, and speculative scope.
- [ ] Formalize target entity Telos (purpose) and verify structural payload validity.

### State 2: Planar Micro-Loop Traversal ($\theta = 0^\circ \to 360^\circ$)
- [ ] Execute 4 internal stations (Triage $\to$ Diagnose $\to$ Solve $\to$ Evaluate).
- [ ] Bound execution within $N_{\max} \le 3$ horizontal iterations.
- [ ] Validate invariant bounds against 3-Tier Structural Hierarchy.

### State 3: Dual-Scale Plotter Gate ($\Delta \theta$ vs. $\Delta Z$)
- [ ] Check convergence: Local patch acceptable ($\Delta \theta$) or root assumption broken ($\Delta Z$)?
- [ ] If root assumption broken: Eject downstream ballast and trigger vertical collapse.
- [ ] If local patch acceptable: Advance to downstream station.

### State 4: Open Gap Budget & Negative Invariant Enforcement
- [ ] Catalog top 3 scale-invariant failure modes (THESIS-036).
- [ ] Enforce binary prohibited constraints (`[PROHIBITED]`).
- [ ] Confirm zero speculative abstractions introduced for marginal open gaps.

### State 5: Merkle Ratification & Terminal Seal
- [ ] Purge ephemeral test ballast and verify No-BOM UTF-8 compliance across all files.
- [ ] Verify core zero-code invariant: Zero unapproved executable artifacts.
- [ ] Enforce SemVer monotonic lock.
- [ ] Commit cryptographic Merkle digest and update institutional scar tissue.

---

## 8. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `pipeline_vector_ratified == True` (9 nodes, 8 dialectic springs mapped).
- [ ] `macro_phase_boundaries_sealed == True` (Phase I, Phase II, Phase III decoupled).
- [ ] `conical_vortex_governance_active == True` ($(r, \theta, Z)$ coordinate system operational).
- [ ] `dialectic_spring_matrix_verified == True` (Springs `< 1 >` through `< 8 >` active).
- [ ] `max_local_cycles_clamped == True` ($N_{\max} = 3$ strictly enforced).
- [ ] `vertical_collapse_protocol_armed == True` ($\Delta Z$ regress and ballast ejection active).
- [ ] `open_gap_budget_codified == True` (Fatal gaps prohibited, over-engineering banned).
- [ ] `biological_primacy_escalation_active == True` (`ESCALATE_TO_HUMAN` trigger ready).
- [ ] `verify_py_invariants_pass == True` (10/10 mechanical verification gates PASS).

