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
Traditional unified processes suffer from the **Planar Fallacy**: modeling software synthesis as a flat 2D conveyor belt. In E-AUP, the operational space is a **Conical Vortex** in cylindrical coordinates $(r, \theta, Z)$:

```text
                  ▲ Z (Altitude: Abstract Intent -> Concrete Artifact)
                  │
        (Apex)    •  PHASE 01: TRIAGE & INTENT (r=1, Minimal Budget / Pure Core)
                 / \
                / S \  PHASE 02: INCEPTION & CONTRACT (r=2, Specification Bounds)
               /  P  \
              /   I   \  PHASE 03: ARCHITECTURE & KEYSTONE (r=3, Pre-Mortem Skeleton)
             /    R    \
            /     A     \  PHASE 04: CONSTRUCTION (r=4, Atomic Code / Module Synthesis)
           /      L      \
          /_______________ \  PHASE 05-06: VERIFICATION & RELEASE (r=5, verify.py / Seal)
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
                      [UPSTREAM PRECEDING PHASE]
                                ▲
                                │  VERTICAL CASCADING COLLAPSE (ΔZ)
                                │  (Root Invariant Breach / False Keystone)
                                │
    ┌───────────────────────────┴───────────────────────────┐
    │  ACTIVE ALTITUDE (Z_k) - INTRA-PHASE HELICAL LOOP     │
    │                                                       │
    │   [Triage] ──► [Diagnose] ──► [Solve] ──► [Evaluate]  │
    │         ▲            ▲            ▲           │       │
    │         └────────────┴────────────┴───────────┘       │
    │             HORIZONTAL OSCILLATION (Δθ Plotter)       │
    │             (Syntax Error, Weak Patch, Missing DoD)   │
    └───────────────────────────────────────────────────────┘
```

### A. Horizontal Oscillation (Angular Correction - $\Delta \theta$)
- **Condition:** Local test failure, syntax defect, or incomplete Definition of Done within current phase altitude $Z_k$.
- **Action:** System maintains current altitude $Z_k$ and retracts angular coordinate to State 3 (Solve) or State 2 (Diagnose).
- **Limit:** Capped at 3 micro-iterations ($N_{\max} = 3$).

### B. Vertical Cascading Collapse (Altitude Regress - $\Delta Z$)
- **Condition:** When an evaluation gate reveals that an underlying architectural assumption, core invariant (`INV-*`), or keystone foundation is defective.
- **Action:** Patching local code is prohibited as entropy dissipation. The system loses altitude and collapses vertically to:
  - $\Delta Z \to \text{Phase 03 (Architecture / Keystone)}$: If inter-tier joints or keystone models fail.
  - $\Delta Z \to \text{Phase 02 (Inception / Contract)}$: If domain invariants or scope boundaries were miscalculated.
  - $\Delta Z \to \text{Phase 01 (Triage & Digest)}$: If the problem itself was fundamentally misdiagnosed.
- **Thermodynamic Pruning & Ballast Ejection:** Upon vertical collapse, all downstream atomic code and speculative text artifacts generated under the false keystone are discarded immediately to preserve minimal action ($\delta S = 0$).

---

## 6. COMPARATIVE MATRIX OF HELICAL LAYERS

| Phase / Altitude ($Z$) | Radius ($r$) & Budget | Micro-Loop Focus ($\theta$) | Vertical Fallback Target ($\Delta Z$) |
| :--- | :--- | :--- | :--- |
| **01. Ingestion / Triage** | $r_1$: Minimal (Single intent / ticket) | Symptom vs. Root Cause demarcation | Terminate & reject input (`ABORT`). |
| **02. Inception / Contract** | $r_2$: Narrow (Pure $DoF=0$ invariants) | `problem.md` & `solution.md` bounds | Fall back to Phase 01 (Re-triage operator intent). |
| **03. Elaboration / Keystone** | $r_3$: Medium (Architect & Scar Desk) | Keystone isolation & Pre-mortem gate | Fall back to Phase 02 (Contractually narrow scope). |
| **04. Construction / Worker** | $r_4$: Wide ($\le 500$ token atomic units) | Surgical implementation, zero fluff | Local $\to \Delta \theta$; Structural $\to$ Fall back to Phase 03. |
| **05. Verification / Adversarial** | $r_5$: Maximum (Full attack surface) | `verify.py`, 100 mutation crucible | Fatal fracture $\to$ Vertical collapse to Phase 02/03. |
| **06. Transition / Release** | $r_0$: Singularity (Release hash) | Decontamination, PII purge, Git tag | Validation breach $\to$ Fall back to Phase 05. |
| **07. Backpropagation** | Global Memory Loop | Scar tissue logging, MSE minimization | Upstream `verify.py` & constitutional patches. |

---

## 7. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `micro_loop_completed == True` across all 4 stations ($\Delta \theta$).
- [ ] `inter_layer_escalation_protocol_active == True` ($\Delta Z$ boundaries mapped).
- [ ] `braintrust_unanimous_pass == True` (Architect, Proceduralist, Stateful Senior sign-off).
- [ ] `murphy_fatal_gaps_sealed == True` (Zero unmodeled fatal escape vectors).
- [ ] `pruning_clean_room_verified == True` (Zero residual ballast on vertical regress).
- [ ] Handoff payload persists as a typed formal intermediate specification.
- [ ] Telemetry state updated and Merkle commit SHA validated.
