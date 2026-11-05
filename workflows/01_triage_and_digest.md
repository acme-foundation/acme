# WF-001: Phase I — Triage & Operational Digest Specification
## Pipeline Vector: `[Input] < 1 > [Triage] < 2 > [Diagnostics]`
*Macro Phase I: Sense-Making & Diagnostics (DoF = 0)*

---

## 1. TRIGGER CONTRACT & SCOPE BOUNDARY
- **Pre-condition:** Ingestion of raw operational signal, incident ticket, telemetry spike, or operator command into Node 1 `[Input]`.
- **Primary Goal:** Filter high-frequency entropic noise, isolate entity Telos, and demarcate surface symptoms from underlying structural pathology (`INV-DIAGNOSTIC-TRIAGE`).
- **Degrees of Freedom (DoF):** 0 (Strict diagnostic classification; zero speculative implementation).
- **Resource Ceiling:** Token consumption $\le 1000$ tokens; execution latency $\le 500\text{ms}$.

---

## 2. PIPELINE TOPOLOGY & NODE-SPRING MATRIX

```text
[INPUT] ────────< 1 >────────► [TRIAGE] ────────< 2 >────────► [DIAGNOSTICS]
(Raw Telemetry)  (Toxin Filter) (Telos Demarcation) (Metric Gate)  (telemetry_digest.md)
```

### A. Discrete Nodes `[]`
* **Node 1: `[Input]` (Intake Receiver):**
  - Ingests raw payload with absolute fidelity.
  - Does not mutate, sanitize, or interpret signal at point of entry.
* **Node 2: `[Triage]` (Ontological Decompiler):**
  - Identifies target entity Telos (constitutional purpose).
  - Categorizes payload into: Functional Defect, Transient Glitch, Scope Smuggling, or Subjective Fluff.
* **Node 3: `[Diagnostics]` (Boundary & Metric Engine):**
  - Extracts 5N1K grid (Who, What, Where, When, Why, How).
  - Establishes ground-truth reproducible metric baselines ($P_{99}$, latency, error offsets).

### B. Dialectic Springs `< >`
* **Spring `< 1 >` (Toxin Shield & Noise Filter):**
  - **Feed-Forward:** Verifies payload possesses minimum substantive payload length ($\ge 20$ bytes) and technical signal.
  - **Backpropagation:** Strips conversational fluff and panic qualifiers (*"urgent"*, *"broken"*, *"slow"*). Non-reproducible subjective chatter is rejected back to input (`REJECT_UNANCHORED_INTENT`).
  - **Homeostasis Check:** Protects downstream nodes from compute and token dissipation.
* **Spring `< 2 >` (Quantification & Metric Gate):**
  - **Feed-Forward:** Asserts that diagnosed anomaly maps to verifiable, quantitative telemetry.
  - **Backpropagation:** If symptom is unmeasurable or non-deterministic, halts pipeline and dispatches an active instrumentation probe request.
  - **Homeostasis Check:** Enforces `INV-DIAGNOSTIC-TRIAGE` ($DoF = 0$).

---

## 3. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Acute Hemostasis (Circuit Breaker)
- [ ] Is there an active infinite loop, OOM fault, thermal quota breach, or cascading service crash?
  - YES: Trip Circuit Breaker immediately (`CIRCUIT_BREAKER_HALT`). Throttle I/O, apply temporary tourniquet. Defer root cause analysis.
  - NO: Proceed to State 1.

### State 1: Input Ingestion & Noise Attenuation (`< 1 >`)
- [ ] Ingest raw payload into `[Input]`.
- [ ] High-Pass Filter: Strip subjective qualifiers and emotional fluff.
- [ ] Calculate signal-to-noise ratio: If payload is 100% subjective chatter, terminate with `EXIT_CODE_400`.

### State 2: Ontological Triage & Symptom Demarcation
- [ ] Target Entity Isolation: Identify specific interface, subsystem, or boundary contract under review.
- [ ] Formalize Telos: What is the normative operational purpose of the entity?
- [ ] Demarcate Symptom vs. Pathology:
  - Isolate observable surface symptom $S(t)$.
  - Reject superficial operator diagnosis as unverified hypothesis (`INV-DIAGNOSTIC-TRIAGE`).

### State 3: Diagnostic Tahlil & Metric Invariants (`< 2 >`)
- [ ] Formulate 5N1K empirical diagnostic matrix.
- [ ] Identify ground-truth metric signatures ($P_{99}$ latency, memory leak rate, error code frequency).
- [ ] Calculate Blast Radius: Delineate maximum affected subsystem perimeter before any fix is contemplated.

### State 4: Telemetry Digest Handshake
- [ ] Synthesize intermediate `artifacts/telemetry_digest.md`.
- [ ] Verify zero solution leakage: Zero algorithms, zero patches, zero speculative code.
- [ ] Handoff payload to `workflows/02_inception_domain.md`.

---

## 4. ADVERSARIAL EVALUATION & MURPHY STRESS VECTORS
- **Escape Vector 1 (Phantom Anomaly):** Operator reporting transient external network glitch as core software failure.
  - *Closure:* Require 3 consecutive reproducible trace events before ratifying defect.
- **Escape Vector 2 (Scope Smuggling at Intake):** Operator bundling multiple unrelated tickets into a single prompt.
  - *Closure:* Enforce strict single-defect atomicity; split into discrete sub-problems.
- **Escape Vector 3 (Subjective Preference Masking):** User cosmetic preference disguised as architectural defect.
  - *Closure:* Binary check against constitutional Telos; reject non-functional preferences.

---

## 5. ANTI-RUMINATION GUARD & OSCILLATION LIMITS
- **Local Oscillation Ceiling:** Clamped strictly to `MAX_LOCAL_CYCLES = 3` ($N_{\max} = 3$).
- If Spring `< 1 >` or `< 2 >` fails to converge within 3 cycles:
  - Halt local execution immediately.
  - Trigger `ESCALATE_TO_HUMAN` (Biological Primacy).
- Local Responsibility Isolation: `[Input]` does not evaluate Telos; `[Triage]` does not calculate code diffs.

---

## 6. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `symptom_isolated_from_root_cause == True`
- [ ] `adjective_density <= 0.02` (Zero subjective fluff).
- [ ] `reproducible_metric_identified == True`
- [ ] `blast_radius_quantified == True`
- [ ] `zero_solution_leakage == True` (`telemetry_digest.md` contains 0 solution code).
- [ ] Handoff Artifact: `artifacts/telemetry_digest.md` sealed with cryptographic SHA-256 digest.
