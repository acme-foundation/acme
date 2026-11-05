# WF-000: E-AUP Meta-Workflow Architecture & Conical Vortex Specification
## Scope: Universal 9-Node Pipeline Governance, Circadian Cadence & Invariant Synthesis (DoF = 0)

---

## 1. TRIGGER CONTRACT & CONSTITUTIONAL INVARIANTS
- **Pre-condition:** Invocation of any Evolutionary Agent-Based Unified Process (E-AUP) phase or downstream project adoption manifest (`.norm`).
- **Input Types:** Architectural directives, telemetry streams, incident triage records, or formal change proposals.
- **Degrees of Freedom (DoF):** 0 (Normative Lex Superior; invariants cannot be relaxed or bypassed).
- **Resource Ceiling:** Global iteration cap $N_{\max} = 3$ per discrete station; latency $\le 500\text{ms}$ per verification evaluation pass.
- **Strict Invariant 1 (Decontamination & Signal Filtering — `INV-DECONTAMINATION`):** All historical narrative, anecdotal noise, and conversational chatter evaluate as pure entropic noise (`ENTROPIC_NOISE`). The core specification compiles exclusively from empirical systems engineering signals, mathematical invariants, and reproducible telemetry. Local host paths and credentials are mechanically barred via `scripts/decontaminator.py`.
- **Strict Invariant 2 (Minimum and Justified Dependency — `INV-MIN-DEPENDENCY`):** The dogma of "absolute zero external dependencies" is formally abandoned as a source of UI crudeness, wheel reinvention, and over-engineering. In its place, the **Zero-Unjustified Dependency** protocol is enforced:
  - **Permitted Leverage (Strict Whitelist):** Zero-setup friction standard CDN tools (e.g., Tailwind CSS CDN, Lucide Icons), native browser APIs (Canvas, Web Audio, localStorage), and Python standard libraries (`sqlite3`, `http.server`, etc.) are directly authorized. Wheels shall not be reinvented.
  - **Prohibited Parasitic Dependencies:** Uncontrolled npm packages introducing local installation overhead, external database servers, and bulky libraries imported for micro-functions are strictly prohibited (`REJECT_PARASITIC_DEPENDENCY`).
- **Strict Invariant 3 (Island Boundary & Dewdrop Isolation — `INV-ISLAND-BOUNDARY`):** Every autonomous execution worker is sandboxed inside an isolated island workspace (`engine/island/` or `tasks/{task_id}/`). Every execution context carries an immutable `CONTEXT_HEADER` signed with SHA-256. Direct modifications outside the designated island boundary (specifically to `CONSTITUTION.md` and ratified `theses/`) trigger immediate compilation abort (`ISLAND_CONTAINMENT_BREACH`).
- **Strict Invariant 4 (Self-Evolving Immunity — `INV-AUTO-IMMUNITY`):** Execution and simulation failures recorded in `WL_TEMPLATE.md` do not remain passive text. Every verified incident pattern must be automatically synthesized into a formal Negative Test Case and promoted into the `verify.py` verification suite as an active assertion gate.

---

## 2. CIRCADIAN CADENCE & PIPELINE VECTOR INTEGRATION (`INV-CIRCADIAN-CADENCE`)

The 7-Stage Circadian Lifecycle (`theses/archive/SYS_123_CIRCADIAN_CADENCE_REVEILLE_RETREAT.md`) governs the temporal operation of the 9-Node Canonical Pipeline Vector:

```text
  [REVEILLE] ──► [DIRECTIVE & TRIAGE] ──► [MARCH] ──► [EXECUTE & TELEMETRY] ──► [RELEASE & RETREAT] ──► [STANDBY]
  (Ground Truth)   (Nodes 1-3: Spec)   (Roll-Call)  (Nodes 4-8: Construction)   (Node 9: Mühür/Clean)   (Idle / Guard)
```

```text
[Input] ──< 1 >──► [Triage] ──< 2 >──► [Diagnostics] ──< 3 >──► [Solution] ──< 4 >──► [Evaluation] ──< 5 >──► [Execution] ──< 6 >──► [Test] ──< 7 >──► [Simulation] ──< 8 >──► [Output]
```

### A. Lifecycle Stage Mapping
1. **REVEILLE (Ground Truth Roll-Call):**
   - At daybreak or session initiation, the workspace executes `git pull` and `python verify.py --verify-all`.
   - All 11 verification gates must yield binary `PASS`. If baseline verification fails, task ingestion is locked.
2. **DIRECTIVE & TRIAGE (Nodes 1–3):**
   - Ingests incoming directive; separates noise from signal.
   - Evaluates **Greenfield vs. Brownfield Entry Threshold**:
     - *Greenfield:* Direct engagement of Inception; `problem_spec.md` synthesized cleanly.
     - *Brownfield:* Direct coding is barred; static AST scan extracts implicit invariants and reports the weakest architectural link (`theses/archive/SYS_112_HOLOGRAPHIC_COHERENCE_FRACTAL_WEAKEST_LINK.md`) before proceeding.
3. **MARCH (Constitutional Assembly):**
   - Pre-execution check: Locks architectural invariants ($DoF = 0$), initializes island containment sandbox, and verifies token/cost quotas.
4. **EXECUTE & TELEMETRY (Nodes 4–8):**
   - Generates candidate architecture (`SPEC-A`), subjects it to adversarial refutation (`SPEC-B`), executes atomic units ($\le 500$ tokens), runs deterministic tests, and executes stress simulation.
5. **RELEASE & RETREAT (Node 9):**
   - Cleanses ephemeral `.tmp/` ballast, verifies No-BOM UTF-8, logs cryptographic Merkle commit digest, validates SemVer monotonic tag, and puts the execution environment into `STANDBY`.

---

## 3. DISCRETE NODES & ONTOLOGICAL CURRICULUM BINDING

Each discrete node is an insulated action cell anchored directly to faculty curriculum foundations and ratified theses:

1. **Node 1: `[Input]` (Intake Receiver):**
   - Ingests raw signal with zero speculative mutation.
2. **Node 2: `[Triage]` (Ontological Decompiler):**
   - *Curriculum Anchors:* `faculty/SYS_systems.md` (Fourier-inspired spectral noise filtration) and `faculty/PHI_philosophy.md` (Teleological framing / Telos extraction).
   - Demarcates surface symptoms from structural pathology (`INV-DIAGNOSTIC-TRIAGE`).
3. **Node 3: `[Diagnostics]` (Boundary & Invariant Engine):**
   - *Curriculum Anchors:* `theses/archive/PHI_102_TACIT_TO_METRIC_GROUNDING.md` and `theses/archive/SYS_144_DRIFT_GUARD_CIRCUIT_BREAKER.md`.
   - Formulates 5N1K empirical diagnostic matrix; bounds maximum blast radius. Produces `artifacts/problem_spec.md`.
4. **Node 4: `[Solution]` (Keystone Architect & Synthesizer):**
   - *Curriculum Anchors:* `theses/SYS_001_PRINCIPLE_OF_LEAST_ACTION.md` / `SYS_101_LEAST_ACTION.md` ($\delta S = 0$) and `theses/archive/SYS_117_TRI_TIER_CONTEXT_FABRIC.md` (`INV-3-TIER-DECOMPOSITION`: Shell $\to$ Layouts $\to$ Components).
   - Emits candidate implementation blueprint: `SPEC-A (The Constructor)`.
5. **Node 5: `[Evaluation]` (Adversarial Crucible & Procedural Gate):**
   - *Curriculum Anchors:* `faculty/LAW_law.md` and `theses/archive/LAW_106_NORMATIVE_HIERARCHY_LEX_EXTERNA.md` (Kelsen Normative Hierarchy / Lex Superior).
   - Engages `SPEC-B (The Adversary)` in the Twin Specification Crucible (`theses/archive/SYS_103_ADVERSARIAL_TWIN_CRUCIBLE.md`). Produces `artifacts/solution_contract.yaml`.
6. **Node 6: `[Execution]` (Atomic Materializer / Polymath Worker):**
   - *Curriculum Anchors:* `theses/archive/SYS_146_PURE_NLP_COGNITIVE_CORE.md` and `RFC_049_RUNTIME_INTERCEPT_AND_AST_SHIELD.md`.
   - Authors surgical diffs ($\le 500$ tokens per unit) under `INV-MIN-DEPENDENCY` and AST execution whitelist shield.
7. **Node 7: `[Test]` (Deterministic Empirical Verifier):**
   - *Curriculum Anchors:* `theses/SYS_002_SPEC_FIRST_ZERO_BIN_DISTRIBUTION.md` and `verify.py`.
   - Mechanical gatekeeper verification; strictly prohibits mocks across invariant boundaries.
8. **Node 8: `[Simulation]` (Adversarial Stress Harness):**
   - *Curriculum Anchors:* `theses/archive/SYS_139_CRUCIBLE_HARDENING.md` and `RFC_050_ADVERSARIAL_CRUCIBLE_CERTIFICATION.md`.
   - Multi-threaded concurrency race condition testing, fuzzing, and pre-mortem failure mode refutation ($k \ge 3$ passes).
9. **Node 9: `[Output]` (Terminal Seal & Scar Tissue Integrator):**
   - *Curriculum Anchors:* `theses/archive/SYS_130_PORTABLE_SPECIFICATION_AND_STATE_CONTINUITY.md` and `theses/archive/SYS_131_STATEFUL_SCAR_TISSUE_AND_FAILURE_INVARIANCE.md`.
   - Merkle commit seal, SemVer release tag, and worklog scar tissue backpropagation.

---

## 4. THE TWIN SPECIFICATION CRUCIBLE (`SPEC-A` vs. `SPEC-B`)

To prevent single-agent consensus bias, the dialectic spring between Node 4 and Node 5 is formalized into a competitive artifact tournament:

```text
    ┌───────────────────────────┐         ┌───────────────────────────┐
    │  SPEC-A (The Constructor) │         │   SPEC-B (The Adversary)  │
    │  - Minimal Architecture   │         │  - Rice Undecidability    │
    │  - PLA (Least Action)     │         │  - Fluff & Adjective Hunt │
    │  - Atomic Component Graph │         │  - Cheapest Escape Vector │
    └─────────────┬─────────────┘         └─────────────┬─────────────┘
                  │                                     │
                  └──────────────────►◄─────────────────┘
                                     │
                              [CRUCIBLE COLLISION]
                                     │
                                     ▼
                    [artifacts/solution_contract.yaml]
                    (Crystal Consensus - Open Gap Deducted)
```

1. **`SPEC-A (The Constructor)`:** Authors the deterministic structural blueprint resolving the exact metrics in `problem_spec.md`.
2. **`SPEC-B (The Adversary / Critic)`:** Formulates a systematic refutation report:
   - Probes for semantic runtime assumptions that cannot be statically verified (Rice's Theorem).
   - Hunts for covert subjective fluff, emotional qualifiers, and unanchored complexity.
   - Calculates the adversary's cheapest bureaucratic escape vector.
3. **Synthesis & Contracting:** Node 5 reconciles the collision. Fatal flaws identified by SPEC-B become hard negative constraints (`[PROHIBITED]`, $DoF = 0$). Marginal nitpicks are allocated to the Open Gap Budget. The surviving consensus is sealed as `artifacts/solution_contract.yaml` and typed `.fir.json`.

---

## 5. THE 3 MACRO PHASE PACKAGING

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MACRO PHASE I: SENSE-MAKING & DIAGNOSTICS (Nodes 1-3)                                  │
│ Ingestion Gate: Greenfield (Inception) vs. Brownfield (Implicit Invariant Extraction)  │
│ Target Deliverable: artifacts/problem_spec.md (DoF = 0, Zero Solution Leakage)        │
└────────────────────────────────────────┬───────────────────────────────────────────────┘
                                         ▼ (problem_spec.md Handoff)
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MACRO PHASE II: DESIGN & DIALECTIC GATE (Nodes 3-5)                                    │
│ Synthesis Gate: Twin Specification Crucible (SPEC-A Constructor vs. SPEC-B Adversary) │
│ Target Deliverable: artifacts/solution_contract.yaml + .fir.json (Writers' Room Pass)  │
└────────────────────────────────────────┬───────────────────────────────────────────────┘
                                         ▼ (solution_contract.yaml Handoff)
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ MACRO PHASE III: MATERIALIZATION & REALITY GATE (Nodes 5-9)                            │
│ Reality Gate: AST Shield + INV-MIN-DEPENDENCY + Chaos Simulation + Merkle Tag Mühür   │
│ Target Deliverable: Ratified Code Diff, verify.py PASS, Merkle Seal, Scar Tissue Log   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. MODEL EVAL-ROUTING MATRIX (PROCESSOR SELECTION)

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
  $$\text{Trigger} \to \texttt{HARD\_BUDGET_STOP}$$
- Prevents runaway recursive loops, background token hemorrhaging, and unbounded context window reprocessing.

### C. Vertical Cascading Collapse (Altitude Regress - $\Delta Z$)
- **Strict Invariant:** On root invariant breach or architectural column (`keystone`) failure, local patching of intermediate layers is prohibited as entropy dissipation (`PROHIBIT_LOCAL_PATCHING_ON_ROOT_BREACH`).
- The system must lose altitude and regress vertically along the spiral slope:
  - $\Delta Z = -1$ from Phase III $\to$ Phase II: When test/simulation reveals a concurrency race condition, deadlock, or throughput collapse rooted in architecture.
  - $\Delta Z = -1$ from Phase II $\to$ Phase I: When target invariants prove mathematically contradictory.
  - $\Delta Z = -2$ from Phase III $\to$ Phase I: When empirical execution demonstrates that foundational problem telemetry was false.
- **Thermodynamic Ballast Ejection:** All downstream speculative code diffs, temporary configurations, and synthetic artifacts generated under the false keystone are permanently deleted immediately ($\delta S = 0$).

### D. Open Gap Budget & Anti-Overengineering (Principle of Least Action)
- Systems and adversaries invariably possess an identifiable "cheapest bureaucratic escape hatch."
- **Fatal Gaps:** Vulnerabilities, deadlocks, or schema drifts that compromise constitutional invariants or cause systemic collapse are classified as fatal. They MUST be codified as hard negative constraints (`[PROHIBITED]`, $DoF = 0$).
- **Marginal / Aesthetic Gaps:** Secondary bureaucratic nitpicks or aesthetic concerns that do not alter operational outcomes must NOT be patched with complex abstractions. They are consciously allocated to an open-gap budget.
- Over-engineering is prohibited (`PROHIBIT_OVER_ENGINEERING`).

---

## 8. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Acute Hemostasis & Circadian Reveille
- [ ] Execute Reveille verification: `python verify.py --verify-all` (All 12 gates must be PASS).
- [ ] Is there an active crash, infinite loop, OOM fault, or financial budget breach ($> \$1.50$)?
  - YES: Trip Circuit Breaker immediately (`HARD_BUDGET_STOP` / `CIRCUIT_BREAKER_HALT`). Throttle I/O, apply temporary tourniquet.
  - NO: Proceed to State 1.

### State 1: Ingestion, Greenfield/Brownfield Detection & Dependency Audit
- [ ] Ingest operational signal through Spring `< 1 >`.
- [ ] Execute Greenfield vs. Brownfield Detection:
  - Clean repo: Initiate Inception.
  - Legacy codebase: Perform AST scan, extract implicit invariants, and isolate weakest link before code modification.
- [ ] Audit Dependency Policy: Confirm compliance with `INV-MIN-DEPENDENCY` (Zero parasitic packages; permitted CDN/stdlib whitelist).

### State 2: Planar Micro-Loop Traversal & Twin Specification Crucible
- [ ] Execute 4 internal stations (Triage $\to$ Diagnose $\to$ Solve $\to$ Evaluate).
- [ ] Engage Twin Specification Crucible: Synthesize `SPEC-A`, attack with `SPEC-B`, deduce crystal consensus.
- [ ] Bound execution within $N_{\max} \le 3$ horizontal iterations.

### State 3: Dual-Scale Plotter Gate ($\Delta \theta$ vs. $\Delta Z$)
- [ ] Check convergence: Local patch acceptable ($\Delta \theta$) or root keystone assumption broken ($\Delta Z$)?
- [ ] If root assumption broken: Eject downstream ballast and trigger vertical collapse.
- [ ] If local patch acceptable: Advance to downstream station.

### State 4: Open Gap Budget & Negative Invariant Enforcement
- [ ] Catalog top 3 scale-invariant failure modes (THESIS-036).
- [ ] Enforce binary prohibited constraints (`[PROHIBITED]`).
- [ ] Confirm zero speculative abstractions introduced for marginal open gaps.

### State 5: Release Retreat & Scar-to-Test Auto-Promotion
- [ ] Execute pre-commit decontamination scan via `scripts/decontaminator.py`.
- [ ] Purge ephemeral test ballast (`.tmp/`) and verify No-BOM UTF-8 across all tracked files.
- [ ] If task failed during execution: Synthesize Negative Test Case and promote into `verify.py` (`INV-AUTO-IMMUNITY`).
- [ ] Enforce SemVer monotonic lock.
- [ ] Commit cryptographic Merkle digest, update worklog scar tissue, and transition environment to `STANDBY`.

---

## 9. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `circadian_cadence_integrated == True` (Reveille-to-Retreat lifecycle active).
- [ ] `island_boundary_isolation_active == True` (`INV-ISLAND-BOUNDARY` enforced).
- [ ] `ontological_bindings_locked == True` (Nodes anchored to faculty curricula & theses).
- [ ] `twin_specification_crucible_active == True` (SPEC-A vs. SPEC-B tournament operational).
- [ ] `scar_to_test_promotion_armed == True` (`INV-AUTO-IMMUNITY` active).
- [ ] `greenfield_brownfield_threshold_active == True` (Legacy implicit invariant scan active).
- [ ] `decontamination_shield_active == True` (12/12 gates in `verify.py` PASS).
- [ ] `financial_circuit_breaker_armed == True` (\$1.50 hard cap enforced).
- [ ] `max_local_cycles_clamped == True` ($N_{\max} = 3 \to \texttt{PAUSED\_FOR\_HUMAN}$).
