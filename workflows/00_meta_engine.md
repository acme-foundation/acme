# WF-000: E-AUP Meta-Engine & Conical Vortex Specification
## Scope: Universal 3D Helical Lifecycle Governor & Dual-Scale Plotter Mechanics (DoF = 0)

---

## 1. TRIGGER CONTRACT
- **Pre-condition:** Invocation of any E-AUP operational phase or downstream task manifest (`.norm`).
- **Input Types:** Architectural directives, telemetry streams, defect reports, or change proposals.
- **Degrees of Freedom (DoF):** 0 (Inviolable governance constitution; cannot be relaxed).
- **Resource Ceiling:** Global iteration cap $N_{\max} = 3$ per discrete station; latency $\le 500\text{ms}$ per evaluation pass.

---

## 2. THE CONICAL VORTEX TOPOLOGY (3D HELICAL DYNAMICS)
Traditional unified processes suffer from the **Planar Fallacy**: modeling software synthesis as a flat 2D conveyor belt. In E-AUP, the operational space is structured as a **Conical Vortex** in cylindrical coordinates $(r, \theta, Z)$ structured into 3 Macro Phases:

```text
                  ▲ Z (Altitude: Abstract Intent -> Concrete Artifact)
                  │
        (Apex)    •  MACRO PHASE I: SENSE-MAKING (r=1..2)
                 / \   [Input] < 1 > [Triage] < 2 > [Diagnostics] -> problem_spec.md
                / S \
               /  P  \  MACRO PHASE II: DESIGN & DIALECTIC GATE (r=3)
              /   I   \   [Diagnostics] < 3 > [Solution] < 4 > [Evaluation] -> solution_contract.yaml
             /    R    \
            /     A     \  MACRO PHASE III: MATERIALIZATION & REALITY (r=4..5)
           /      L      \   [Execution] < 6 > [Test] < 7 > [Simulation] < 8 > [Output]
          /_______________ \
                  r ──► (Radius: Scope, Token Budget, Complexity & Attack Surface)
```

### Coordinate System:
1. **$\theta$ (Angular Micro-Loop - $0^\circ \to 360^\circ$):** Intra-phase circular traversal through the 4 internal stations: **Triage $\to$ Diagnose $\to$ Solve $\to$ Evaluate**.
2. **$r$ (Radial Coordinate - Scope & Kinetic Energy):** Expands monotonically from apex ($r_0$, minimal tokens, pure intent) toward the base ($r_{\max}$, full test surface, integration matrix).
3. **$Z$ (Vertical Altitude - Ontological Depth):** Governs vertical descent from sovereign abstract requirements down to concrete, executed, and ratified deliverables.

---

## 3. INNER MICRO-LOOP & STATE MACHINE (TRIAGE -> DIAGNOSE -> SOLVE)
Every operational altitude ($Z_k$) must recursively execute the 4-station micro-loop:

### State 0: Acute Hemostasis (Circuit Breaker)
- [ ] Is there an active system crash, infinite loop, or resource exhaustion?
  - YES: Trip Circuit Breaker immediately (`CIRCUIT_BREAKER_HALT`). Throttle I/O, apply temporary tourniquet. (Root cause analysis is strictly deferred).
  - NO: Proceed to State 1.

### State 1: Triage Protocol & Teleological Framing ($\theta = 0^\circ \to 90^\circ$)
- [ ] Identify Subject Entity: Formalize entity nature and teleological scope (Telos).
- [ ] Surface Symptom vs. Root Cause Demarcation: All initial user/operator inputs evaluate strictly as noisy symptoms (`INV-DIAGNOSTIC-TRIAGE`).
- [ ] Entropic Noise Purge: Discard unanchored subjective qualifiers (`REJECT_HIGH_FREQUENCY_FLUFF`).

### State 2: Diagnostics & Metric Invariant Matrix ($\theta = 90^\circ \to 180^\circ$)
- [ ] Ground Truth Quantification: What cannot be measured cannot be validated (`REJECT_UNMEASURED_DIAGNOSIS`).
- [ ] Invariant Boundary Extraction: Identify legal, statutory, type-level, and architectural constraints.
- [ ] Blast Radius Calculation: Bound maximum affected subsystem radius before code is touched.

### State 3: Solution Synthesis & Atomic Decomposition ($\theta = 180^\circ \to 270^\circ$)
- [ ] 3-Tier Structural Hierarchy: Decompose solution into Application Shell $\to$ Layouts $\to$ Components (`INV-3-TIER-DECOMPOSITION`).
- [ ] Anti-Monolithic Escalation: Spontaneous monoliths are rejected by default (`INV-PRIMITIVE-ATTRACTOR-REFUTATION`).
- [ ] Surgical Sizing: Ensure each atomic execution unit remains bounded ($\le 500$ tokens).

---

## 4. EVALUATION & ADVERSARIAL GATE ($\theta = 270^\circ \to 360^\circ$)
No artifact may pass to the next altitude without surviving the dual-adversarial crucible:

### A. The Writers' Room (Braintrust Dialectic)
- **Profile A (Architect / Pragmatist):** Enforces minimum viable complexity, zero redundant intermediate states, and thermodynamic efficiency ($\delta S = 0$).
- **Profile B (Proceduralist / Purist):** Enforces statutory compliance, interface typing, strict contract preconditions, and immutable boundary invariants.
- **Profile C (Scarred Senior / Stateful Worker):** Injects historical scar tissue: past deadlock patterns, memory leaks, compiler quirks, and downstream regression vectors.

### B. The Murphy Stress Filter & Escape Line Analysis
- **Cheapest Escape Vector Detection:** Identify the most superficial justification an adversary (compiler, judge, API gateway, end user) could exploit to reject the deliverable.
- **Gap Closure Economics:**
  - *Fatal Gap:* Flaws that compromise systemic invariants or induce catastrophic cascade $\to$ Inlined as hard negative constraints (`[PROHIBITED]`, `DoF = 0`).
  - *Marginal Gap:* Bureaucratic or aesthetic nitpicks whose remediation cost exceeds utility $\to$ Allocated to the conscious open-gap budget without over-engineering.

---

## 5. DUAL-SCALE PLOTTER LOGIC & VERTICAL ESCALATION

Progress is non-linear; the system acts as a 3D plotter head with two orthogonal oscillation vectors:

```text
                      [UPSTREAM PRECEDING MACRO PHASE]
                                     ▲
                                     │  VERTICAL CASCADING COLLAPSE (ΔZ)
                                     │  (Root Invariant Breach / False Keystone)
                                     │
     ┌───────────────────────────────┴───────────────────────────────┐
     │  ACTIVE ALTITUDE (Z_k) - INTRA-PHASE HELICAL LOOP             │
     │                                                               │
     │   [Triage] ──► [Diagnose] ──► [Solve] ──► [Evaluate]          │
     │         ▲            ▲            ▲           │               │
     │         └────────────┴────────────┴───────────┘               │
     │             HORIZONTAL OSCILLATION (Δθ Plotter)               │
     │             (Syntax Error, Weak Patch, Missing DoD)           │
     └───────────────────────────────────────────────────────────────┘
```

### A. Horizontal Oscillation (Angular Correction - $\Delta \theta$)
- **Condition:** Local test failure, syntax defect, or incomplete Definition of Done within current phase altitude $Z_k$.
- **Action:** System maintains current altitude $Z_k$ and retracts angular coordinate to State 3 (Solve) or State 2 (Diagnose).
- **Limit:** Capped at 3 micro-iterations ($N_{\max} = 3$).

### B. Vertical Cascading Collapse (Altitude Regress - $\Delta Z$)
- **Condition:** When an evaluation gate reveals that an underlying architectural assumption, core invariant (`INV-*`), or keystone foundation is defective.
- **Action:** Patching local code is prohibited as entropy dissipation. The system loses altitude and collapses vertically:
  - $\Delta Z = -1$ from Phase III $\to$ `workflows/02_design_and_dialectic.md`: When tests reveal structural, keystone, or concurrency model defects.
  - $\Delta Z = -1$ from Phase II $\to$ `workflows/01_sense_making.md`: When domain invariants or scope boundaries were miscalculated.
  - $\Delta Z = -2$ from Phase III $\to$ `workflows/01_sense_making.md`: When ground-truth metrics or teleological assumptions were fundamentally false.
- **Thermodynamic Pruning & Ballast Ejection:** Upon vertical collapse, all downstream atomic code and speculative text artifacts generated under the false keystone are discarded immediately to preserve minimal action ($\delta S = 0$).

---

## 6. COMPARATIVE MATRIX OF THE 3 MACRO PHASES

| Macro Phase | Vector Topology | Radius ($r$) & Budget | Primary Deliverable | Vertical Fallback Target ($\Delta Z$) |
| :--- | :--- | :--- | :--- | :--- |
| **I. Sense-Making** (`01_sense_making.md`) | `[Input] <1> [Triage] <2> [Diagnostics]` | $r_1..r_2$: Narrow (Minimal tokens / Intent) | `artifacts/problem_spec.md` | Reject input / Escalate to Human (`ABORT`). |
| **II. Design & Dialectic** (`02_design_and_dialectic.md`) | `[Diagnostics] <3> [Solution] <4> [Evaluation]` | $r_3$: Medium (Architecture & Pre-Mortem) | `artifacts/solution_contract.yaml` | $\Delta Z = -1 \to$ Phase I (`01_sense_making.md`). |
| **III. Materialization & Reality** (`03_materialization_and_reality.md`) | `[Execution] <6> [Test] <7> [Simulation] <8> [Output]` | $r_4..r_5$: Maximum (Execution & Chaos Harness) | Ratified Commit, Merkle Seal, Scar Tissue | $\Delta Z = -1 \to$ Phase II; $\Delta Z = -2 \to$ Phase I. |

---

## 7. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `macro_phase_contracts_ratified == True` (`01_sense_making.md`, `02_design_and_dialectic.md`, `03_materialization_and_reality.md`).
- [ ] `inter_layer_escalation_protocol_active == True` ($\Delta Z$ boundaries mapped).
- [ ] `braintrust_unanimous_pass == True` (Architect, Proceduralist, Stateful Senior sign-off).
- [ ] `murphy_fatal_gaps_sealed == True` (Zero unmodeled fatal escape vectors).
- [ ] `pruning_clean_room_verified == True` (Zero residual ballast on vertical regress).
- [ ] Handoff payload persists as a typed formal intermediate specification.
- [ ] Telemetry state updated and Merkle commit SHA validated.
