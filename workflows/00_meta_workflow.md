# WF-000: E-AUP Meta-Workflow Architecture & Conical Vortex Specification
## Scope: Universal 9-Node Pipeline Governance, Minimum Justified Dependency & Financial Circuit Breakers (DoF = 0)

---

## 1. TRIGGER CONTRACT & SCOPE BOUNDARY
- **Pre-condition:** Invocation of any Evolutionary Agent-Based Unified Process (E-AUP) phase or downstream project adoption manifest (`.norm`).
- **Input Types:** Architectural directives, telemetry streams, incident triage records, or formal change proposals.
- **Degrees of Freedom (DoF):** 0 (Normative Lex Superior; invariants cannot be relaxed or bypassed).
- **Resource Ceiling:** Global iteration cap $N_{\max} = 3$ per discrete station; latency $\le 500\text{ms}$ per verification evaluation pass.
- **Strict Invariant 1 (Decontamination & Signal Filtering):** All historical narrative, anecdotal noise, and conversational chatter evaluate as pure entropic noise (`ENTROPIC_NOISE`). The core specification compiles exclusively from empirical systems engineering signals, mathematical invariants, and reproducible telemetry.
- **Strict Invariant 2 (Minimum and Justified Dependency — `INV-MIN-DEPENDENCY`):** The dogma of "absolute zero external dependencies" is formally abandoned as a source of UI crudeness, wheel reinvention, and over-engineering. In its place, the **Zero-Unjustified Dependency** protocol is enforced:
  - **Permitted Leverage (Strict Whitelist):** Zero-setup friction standard CDN tools (e.g., Tailwind CSS CDN, Lucide Icons), native browser APIs (Canvas, Web Audio, localStorage), and Python standard libraries (`sqlite3`, `http.server`, etc.) are directly authorized. Wheels shall not be reinvented.
  - **Prohibited Parasitic Dependencies:** Uncontrolled npm packages introducing local installation overhead, external database servers, and bulky libraries imported for micro-functions are strictly prohibited (`REJECT_PARASITIC_DEPENDENCY`).

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
6. **Node 6: `[İcra / Execution]` (Atomic Materializer / Construction Worker):** Synthesizes concrete atomic diffs under the AST Runtime Intercept Shield (`INV-RUNTIME-INTERCEPT`) and `INV-MIN-DEPENDENCY`.
7. **Node 7: `[Test / Test]` (Deterministic Empirical Verifier):** Executes mechanical test suites (`verify.py --verify-all`), type checkers, and unit contracts to reach a binary PASS/FAIL verdict.
8. **Node 8: `[Simülasyon / Simulation]` (Adversarial Stress Harness):** Injects chaos, race conditions, edge fuzzing, and mutation suites (`INV-CRUCIBLE-CERTIFICATION`) to refute Goodhart's law evasion.
9. **Node 9: `[Çıkış / Output]` (Terminal Seal & Scar Tissue Integrator):** Cleanses workspace, validates No-BOM UTF-8, verifies SemVer monotonic lock, commits cryptographic Merkle digest, and updates institutional scar tissue.

---

## 3. THE 3 MACRO PHASE PACKAGING

To eliminate cognitive overload and prevent agentic thrashing, the 9-node pipeline is partitioned into 3 sequential, closed-loop Macro Phases:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MACRO PHASE I: SENSE-MAKING & DIAGNOSTICS (Anlama & Teşhis)                            │
│ Pipeline: [Input] ───< 1 >───► [Triage] ───< 2 >───► [Diagnostics]                    │
│ Target Deliverable: artifacts/problem_spec.md (DoF = 0, Zero Solution Leakage)        │
└────────────────────────────────────────┬───────────────────────────────────────────────┘
                                         ▼ (problem_spec.md Handoff)
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MACRO PHASE II: DESIGN & DIALECTIC GATE (Sentez & Süzgeç)                              │
│ Pipeline: [Diagnostics] ───< 3 >───► [Solution] ───< 4 >───► [Evaluation]              │
│ Target Deliverable: artifacts/solution_contract.yaml + .fir.json (Writers' Room Pass)  │
└────────────────────────────────────────┬───────────────────────────────────────────────┘
                                         ▼ (solution_contract.yaml Handoff)
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MACRO PHASE III: MATERIALIZATION & REALITY GATE (Maddileşme & Gerçeklik)               │
│ Pipeline: ──< 5 >──► [Execution] ───< 6 >───► [Test] ───< 7 >───► [Simulation] ──< 8 > │
│ Target Deliverable: Ratified Code Diff, verify.py PASS, Merkle Seal, Scar Tissue Log   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### A. Phase I: Sense-Making & Diagnostics (Düğümler 1-3)
- **Scope:** Ingests raw signal, filters entropic noise, extracts invariants, and formulates the ground-truth problem definition.
- **Contract Boundary:** Separates symptoms from root needs at intake; noise is rejected (`REJECT_UNANCHORED_INTENT`) before token consumption.
- **Handoff Artifact:** Sealed `artifacts/problem_spec.md`.

### B. Phase II: Design & Dialectic Gate (Düğümler 3-5)
- **Scope:** Produces surgical architecture; engages tripartite Writers' Room dialectic (Architect, Proceduralist, Stateful Senior) against Murphy Stress Filter.
- **Contract Boundary:** Pre-mortem gates (THESIS-036) must catalog the top 3 domain failure modes and establish hard negative constraints (`[PROHIBITED]`, $DoF = 0$).
- **Handoff Artifact:** Sealed `artifacts/solution_contract.yaml` (executable specification) and typed `.fir.json`.

### C. Phase III: Materialization & Reality Gate (Düğümler 5-9)
- **Scope:** Polymath worker executes atomic construction ($\le 500$ tokens); rapid MVP/POC scaffolding is stood up under the **Minimum Justified Dependency** (`INV-MIN-DEPENDENCY`) rule; runs local deterministic tests (`verify.py`, linters) and field stress simulations; seals release with cryptographic Merkle digest.
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
               /  P  \  MACRO PHASE II: DESIGN & DIALECTIC GATE (r=3)
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

## 5. DIALECTIC SPRING PROTOCOL (`< >`) & PLOTTER BACKPROPAGATION

Every dialectic spring membrane operates as an active, three-vector immunological filter:
1. **Feed-Forward:** Purity and schema compliance verification before downstream ingestion. The output of an upstream node must satisfy the explicit type and format contract of the downstream receiver.
2. **Feedback / Backpropagation (Plotter):** When a downstream constraint is breached, an atomic micro-correction instruction is dispatched upstream directly to the node that introduced the defect.
3. **Homeostasis & Telos Verification:** Continuous autonomous self-check: *"Does this transition serve the root constitutional purpose (Telos) with least action ($\delta S = 0$), or does it generate speculative entropy?"*

```text
  [NODE N] ──────(Feed-Forward: Purity & Schema Pass)──────► [NODE N+1]
     ▲                                                           │
     │◄──────(Feedback / Plotter: Pushback & Correction)─────────┤
     │                                                           │
     └────────(Homeostasis: Telos & Least Action Audit)──────────┘
```

---

## 6. MODEL EVAL-ROUTING MATRIX (PROCESSOR SELECTION)

Execution efficiency requires matching task complexity to processor capability, preventing cognitive waste and excessive token burn:

| Nodes / Stations | Operational Domain | Recommended Model Tier | Selection Rationale |
| :--- | :--- | :--- | :--- |
| **Node 1, 2, 6** | `[Input]`, `[Triage]`, `[Test]` / Linter | Lightweight / Deterministic (Local Python / Flash / Haiku) | Fast, zero/low-cost deterministic signal processing, schema parsing, and mechanical script execution. |
| **Node 4, 7** | `[Solution]`, Writers' Room, Murphy, `[Simulation]` | Deep Reasoning / Heavy Dialectic (Thinking / Opus / Pro) | High cognitive deliberation, edge-case simulation, game-theoretic stress testing, and architectural tradeoff analysis. |
| **Node 5** | `[Execution]` (Atomic Materializer) | Instruction-Faithful Worker (Coder / Synthesizer) | Bounded, surgical execution of exact specifications without speculative deviation or creative hallucination. |

---

## 7. ENERGY, OSCILLATION & FINANCIAL CIRCUIT BREAKERS

```text
                                [PHASE I: SENSE-MAKING]
                                           ▲
                                           │  ΔZ = -2 (Foundational Diagnostic Error)
                                           │
                              [PHASE II: DESIGN & DIALECTIC]
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
- Maximum permissible oscillation across any planar spring interface:
  $$\text{Cycle Count} \le N_{\max} = 3$$
- If consensus is not achieved within 3 iterations, autonomous rumination is terminated immediately.
- The system updates operational state in `.acme/workspace_state.json` to:
  $$\text{System State} = \texttt{PAUSED\_FOR\_HUMAN}$$
- Triggers immediate escalation to the biological system architect (`ESCALATE_TO_HUMAN`).

### B. Financial Budget Ceiling (`HARD_BUDGET_STOP`)
- Every autonomous task is constrained by a strict monetary expenditure ceiling:
  $$\text{Cost Ceiling} \le \$1.50\text{ USD per task}$$
- When cumulative API token expenditure exceeds \$1.50 or the designated token threshold, autonomous processing is forcibly aborted:
  $$\text{Trigger} \to \texttt{HARD\_BUDGET\_STOP}$$
- Prevents runaway recursive loops, background token hemorrhaging, and unbounded context window reprocessing.

### C. Vertical Cascading Collapse (Altitude Regress - $\Delta Z$)
- **Strict Invariant:** On root invariant breach or architectural column (`keystone`) failure, local patching of intermediate layers is prohibited as entropy dissipation (`PROHIBIT_LOCAL_PATCHING_ON_ROOT_BREACH`).
- The system must lose altitude and regress vertically along the spiral slope:
  - $\Delta Z = -1$ from Phase III $\to$ Phase II: When test/simulation reveals a concurrency race condition, deadlock, or throughput collapse rooted in architecture.
  - $\Delta Z = -1$ from Phase II $\to$ Phase I: When target invariants prove mathematically contradictory.
  - $\Delta Z = -2$ from Phase III $\to$ Phase I: When empirical execution demonstrates that foundational problem telemetry was false.
- **Thermodynamic Ballast Ejection:** All downstream speculative code diffs, temporary configurations, and synthetic artifacts generated under the false keystone are permanently deleted immediately ($\delta S = 0$).

### D. Open Gap Budget & Anti-Overengineering (Açık Kapı Bütçesi)
- Systems and adversaries invariably possess an identifiable "cheapest bureaucratic escape hatch."
- **Fatal Gaps:** Vulnerabilities, deadlocks, or schema drifts that compromise constitutional invariants or cause systemic collapse are classified as fatal. They MUST be codified as hard negative constraints (`[PROHIBITED]`, $DoF = 0$).
- **Marginal / Aesthetic Gaps:** Secondary bureaucratic nitpicks or aesthetic concerns that do not alter operational outcomes must NOT be patched with complex abstractions. They are consciously allocated to an open-gap budget.
- Over-engineering is prohibited (`PROHIBIT_OVER_ENGINEERING`).

---

## 8. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Acute Hemostasis & Financial Circuit Breaker
- [ ] Is there an active crash, infinite loop, OOM fault, or financial budget breach ($> \$1.50$)?
  - YES: Trip Circuit Breaker immediately (`HARD_BUDGET_STOP` / `CIRCUIT_BREAKER_HALT`). Throttle I/O, apply temporary tourniquet.
  - NO: Proceed to State 1.

### State 1: Ingestion, Teleological Framing & Dependency Audit
- [ ] Ingest operational signal through Spring `< 1 >`.
- [ ] Filter subjective adjectives, emotional markers, and speculative scope.
- [ ] Formalize target entity Telos (purpose) and verify structural payload validity.
- [ ] Audit Dependency Policy: Confirm compliance with `INV-MIN-DEPENDENCY` (Zero parasitic packages; permitted CDN/stdlib whitelist).

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

## 9. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `pipeline_vector_ratified == True` (9 nodes, 8 dialectic springs mapped).
- [ ] `inv_min_dependency_enforced == True` (Zero-Unjustified Dependency / Permitted CDN & stdlib whitelist active).
- [ ] `macro_phase_boundaries_sealed == True` (Phase I, Phase II, Phase III decoupled).
- [ ] `model_eval_routing_active == True` (Processors assigned per operational node).
- [ ] `financial_circuit_breaker_armed == True` (\$1.50 hard cap enforced).
- [ ] `max_local_cycles_clamped == True` ($N_{\max} = 3 \to \texttt{PAUSED\_FOR\_HUMAN}$).
- [ ] `vertical_collapse_protocol_armed == True` ($\Delta Z$ regress and ballast ejection active).
- [ ] `open_gap_budget_codified == True` (Fatal gaps prohibited, over-engineering banned).
- [ ] `biological_primacy_escalation_active == True` (`ESCALATE_TO_HUMAN` trigger ready).
- [ ] `verify_py_invariants_pass == True` (10/10 mechanical verification gates PASS).
