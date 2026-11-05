# WF-001: Phase I — Sense-Making Workflow Contract
## Pipeline Vector: `[Input] < 1 > [Triage] < 2 > [Diagnostics] -> problem_spec.md`
*Macro Phase I: Sense-Making (DoF = 0)*

---

## 1. PIPELINE TOPOLOGY & NODE-SPRING MATRIX

```text
[INPUT] ───< 1 >───► [TRIAGE] ───< 2 >───► [DIAGNOSTICS] ───► [OUTPUT: problem_spec.md]
(Raw Signal)        (Telos & Root)        (Metric Invariants)
```

### A. Discrete Nodes `[]` (Local State Keepers)
* **Node 0: `[Input]` (Intake Receiver):**
  - **Scope:** Ingest raw telemetry, defect tickets, customer logs, or operator commands.
  - **Responsibility:** Ingestion fidelity without speculative modification. Does not perform systemic philosophy.
* **Node 1: `[Triage]` (Ontological Decompiler):**
  - **Scope:** Isolate target entity Telos (core purpose) and demarcate surface symptoms from underlying pathology.
  - **Responsibility:** Teleological framing and entropic noise filtration.
* **Node 2: `[Diagnostics]` (Tahlil & Boundary Engine):**
  - **Scope:** Quantify observable defects against empirical baselines, delineate statutory/architectural invariants, and calculate blast radius.
  - **Responsibility:** Produces the immutable `artifacts/problem_spec.md`.

### B. Dialectic Springs `< >` (Braintrust & Murphy Membranes)
* **Spring `< 1 >` (Toxin Shield & Noise Filter):**
  - **Feed-Forward:** Is the raw input genuine operational intent, or is it toxic conversational fluff / panic chatter?
  - **Backpropagation:** Subjective adjectives (*"slow"*, *"urgent"*, *"broken"*) are rejected back to input (`REJECT_UNANCHORED_INTENT`).
  - **Homeostasis Check:** Protects downstream nodes from compute and context window dissipation.
* **Spring `< 2 >` (Quantification & Metric Gate):**
  - **Feed-Forward:** Can the diagnosed symptom be mapped to reproducible, quantifiable telemetry metrics ($P_{99}$, latency, error codes, memory offsets)?
  - **Backpropagation:** If the anomaly is unmeasurable, halt progression and dispatch an active instrumentation probe request.
  - **Homeostasis Check:** Enforces `INV-DIAGNOSTIC-TRIAGE` ($DoF = 0$).

---

## 2. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Acute Hemostasis (Circuit Breaker)
- [ ] Is there an active infinite loop, OOM fault, thermal quota breach, or cascading deadlock?
  - YES: Trip Circuit Breaker immediately (`CIRCUIT_BREAKER_HALT`). Shunt traffic, apply degraded-state tourniquet. Defer root cause analysis.
  - NO: Proceed to State 1.

### State 1: Input Ingestion & Toxins Gate (`< 1 >`)
- [ ] Ingest raw time-domain payload into `[Input]`.
- [ ] High-Pass Filter: Strip subjective fluff and emotional qualifiers.
- [ ] Validate minimum structural payload length ($\ge 20$ bytes).

### State 2: Ontological Triage & Teleology
- [ ] Identify Target Entity: What system, interface, or service is being addressed?
- [ ] Formalize Telos: What is the normative operational purpose of the entity?
- [ ] Defect vs. Preference Demarcation:
  - Subjective preference: Reject at intake (`Exit Code 400`).
  - Functional impairment of Telos: Proceed to State 3.

### State 3: Diagnostic Tahlil & Metric Invariants (`< 2 >`)
- [ ] Deconstruct intent across 5N1K metric grid (Who, What, Where, When, Why, How).
- [ ] Identify statutory, architectural, and type invariants (`INV-*`).
- [ ] Calculate Blast Radius: Quantify maximum affected subsystem boundary.

### State 4: Specification Seal (`problem_spec.md`)
- [ ] Synthesize `artifacts/problem_spec.md`:
  - Defined Telos.
  - Falsifiable ground-truth failure state.
  - Measurable boundary invariants ($DoF = 0$).
  - Zero solution code or implementation speculation.

---

## 3. ADVERSARIAL EVALUATION & MURPHY STRESS FILTER

### A. Writers' Room Focus
- **Architect (Pragmatist):** Verifies that the problem is framed at the minimal viable complexity level without premature architecture.
- **Proceduralist (Kuralcı):** Verifies all 5N1K fields are populated and zero subjective adjectives leaked into `problem_spec.md`.
- **Scarred Senior (Stateful Worker):** Cross-checks failure signature against historical incident scar tissue.

### B. Murphy Filter (Top Escape Vectors)
- **Escape Vector 1 (Phantom Symptom):** Transient network glitch reported as a core architectural failure.
  - *Closure:* Require 3 consecutive reproducible trace logs before ratifying defect.
- **Escape Vector 2 (Scope Smuggling):** Operator bundling multiple distinct problems into a single ticket.
  - *Closure:* Enforce single-defect atomicity; split into discrete sub-problems.
- **Escape Vector 3 (Metric Gaming):** Defining success criteria so loosely that an empty implementation satisfies it.
  - *Closure:* Bind criteria to strict binary Boolean ground truth.

---

## 4. ANTI-RUMINATION GUARD & OSCILLATION LIMITS

```text
  [Input]  ◄──(Feed-Back / Murphy)──►  [Triage]  ◄──(Feed-Back / Murphy)──►  [Diagnostics]
     │                                    │                                      │
     ▼                                    ▼                                      ▼
(Local Cycle)                       (Local Cycle)                          (Local Cycle)
```

- **Maximum Local Oscillation Ceiling:** `MAX_LOCAL_CYCLES = 3` ($N_{\max} = 3$).
  - If Spring `< 1 >` or `< 2 >` fails to converge within 3 bidirectional iterations, internal processing terminates unconditionally.
  - Trigger: `ESCALATE_TO_HUMAN` (Escalation to Biological Root of Trust).
- **Local Responsibility Isolation:**
  - `[Input]` does not evaluate Telos.
  - `[Diagnostics]` does not synthesize solutions.
  - The question *"Am I aligned with the whole?"* is evaluated exclusively at dialectic membranes `< 1 >` and `< 2 >`.

---

## 5. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `symptom_isolated_from_root_cause == True`
- [ ] `adjective_density <= 0.02` (Zero subjective fluff).
- [ ] `reproducible_metric_identified == True`
- [ ] `blast_radius_quantified == True`
- [ ] `zero_solution_leakage == True` (`problem_spec.md` contains 0 solution code).
- [ ] Handoff Artifact: `artifacts/problem_spec.md` sealed.
- [ ] State Persistence: Local telemetry record committed and Merkle hash verified.
