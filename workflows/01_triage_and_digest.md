# WF-001: Triage & Digest Workflow
## Scope: Raw Intent Intake, Symptom Demarcation & Boundary Detection (DoF = 0)
*Classical AUP Discipline: Business Modeling*

---

## 1. TRIGGER CONTRACT
- **Pre-condition:** Operator prompt arrival, external incident webhook, or new ticket manifest intake.
- **Input Types:** Natural language text, stack traces, telemetry log dumps, or issue tickets.
- **Degrees of Freedom (DoF):** 0 (Hard intake gate; non-negotiable).
- **Resource Ceiling:** Token window $\le 2000$; triage completion latency $\le 30\text{s}$.

---

## 2. INNER MICRO-LOOP & STATE MACHINE (TRIAGE -> DIAGNOSE -> SOLVE)

### State 0: Acute Hemostasis (Circuit Breaker)
- [ ] Is the reported defect actively exhausting memory, token quota, or compute?
  - YES: Trip Circuit Breaker (`CIRCUIT_BREAKER_HALT`). Shunt traffic, apply emergency tourniquet, defer root intake.
  - NO: Proceed to State 1.

### State 1: Ontological Framing & Telos Identification
- [ ] Formalize Target Entity: What system, service, or repository is being addressed?
- [ ] Telos Extraction: What is the core existential purpose of the entity?
- [ ] Symptomatic Demarcation: Is the input an ungrounded preference or an objective operational failure?
  - Ungrounded / Subjective: REJECT at intake (`Exit Code 400`, `REJECT_UNANCHORED_INTENT`).
  - Grounded Operational Defect: Proceed to State 2.

### State 2: Spectral Noise Filtering (FFT Intake)
- [ ] High-Pass Filter Gate: Strip all subjective adjectives (*"fast"*, *"urgent"*, *"broken"*, *"terrible"*).
- [ ] Low-Pass Carrier Isolation: Extract quantifiable error signatures (status codes, memory offsets, latency deviations).
- [ ] Boundary Detection: Delineate external environment boundary vs. internal system responsibility.

### State 3: Digest Formulation & Triage Contract
- [ ] Draft `triage_digest.md` encapsulating:
  - Validated Telos
  - Quantified defect metric
  - Allowed blast radius bounds
- [ ] Ensure digest contains zero executable code and zero speculative inferences.

---

## 3. EVALUATION & ADVERSARIAL GATE

### A. Writers' Room Focus
- **Architect:** Verifies the defect is isolated to a clean problem statement rather than solution premature jumping.
- **Proceduralist:** Verifies input conforms to statutory 5N1K coordinates (Who, What, Where, When, Why, How).
- **Scarred Senior:** Checks if the symptom is a known recurring ghost of a prior architectural flaw.

### B. Murphy Stress Filter
- **Escape Vector 1 (Phantom Symptom):** The user reported a transient client-side glitch mistaken for a core defect.
- **Escape Vector 2 (Scope Creep):** The ticket bundles multiple unrelated complaints into a single monolithic defect.
- **Escape Vector 3 (Metric Evaporation):** The failure cannot be reproduced or verified through objective telemetry.

---

## 4. BACKPROPAGATION & PLOTTER LOGIC
- **Horizontal Oscillation (Δθ Plotter):**
  - If Metric Evaporation detected: Plotter backtracks to State 2; request instrumentation probe.
  - If Scope Creep detected: Plotter splits intake into atomic sub-digests; restart State 1 per sub-digest.
  - If Phantom Symptom confirmed: Plotter halts intake and drops ticket into cryptographic archive log (`QUARANTINE_AND_LOG`).
- **Inter-Layer Escalation Protocol (Vertical Dynamics - ΔZ):**
  - **Local Tolerance (Δθ):** Maximum 3 micro-oscillations within Phase 01.
  - **Apex Boundary Condition:** If input is fundamentally ungrounded, unmeasurable, or malicious (`INV-OPTIN-STRICT` breach), the system executes a terminal abort (`ABORT`), preventing downward descent into Phase 02.
- **Iteration Ceiling ($N_{\max} = 3$):** Unresolved ambiguity escalates to biological human anchor.

---

## 5. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `symptom_isolated == True`
- [ ] `adjective_density <= 0.02`
- [ ] `reproducible_metric_identified == True`
- [ ] Handoff Artifact: `artifacts/triage_digest.md` compiled and ready for Inception.
- [ ] State Persistence: Telemetry record updated and anchored.

