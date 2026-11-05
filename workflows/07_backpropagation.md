# WF-007: Backpropagation & Scar Tissue Ingestion Workflow
## Scope: Retrospective Analysis, Scar Tissue Logging & Autopoietic Evolution (DoF = 0)
*Classical AUP Discipline: Configuration & Change Management*

---

## 1. TRIGGER CONTRACT
- **Pre-condition:** Successful release publication from WF-006 or post-incident root-cause analysis (RCA).
- **Input Types:** Release logs, incident post-mortems, friction reports (RFCs), mutation telemetry.
- **Degrees of Freedom (DoF):** 0 (Systemic learning is strictly empirical; unanchored changes forbidden).
- **Resource Ceiling:** Retrospective analysis latency $\le 45\text{s}$; maximum 3 scar invariants per cycle.

---

## 2. INNER MICRO-LOOP & STATE MACHINE (TRIAGE -> DIAGNOSE -> SOLVE)

### State 0: Operational Friction Triage
- [ ] Ingest operational telemetry: Did the previous execution cycle experience oscillation, stalls, or workarounds?
  - NO: Proceed directly to State 3 (quiescent closure).
  - YES: Proceed to State 1.

### State 1: Forensic Root Cause Analysis (Incident RCA)
- [ ] Analyze friction across 4 telemetric axes:
  1. *Attention & Context Window:* Did token bloat or context loss induce hallucination?
  2. *Default Prior vs. Local Invariant:* Did general LLM priors override local constitutional rules?
  3. *Instruction Saliency:* Were negative constraints buried in prose rather than hard-gated?
  4. *Mechanical Turnstile Coverage:* Was the defect detectable via automated static gates?

### State 2: Scar Tissue Formulation & RFC Generation
- [ ] Translate painful runtime defects into permanent scar tissue:
  - Formulate an explicit, falsifiable RFC conforming to `templates/RFC_TEMPLATE.md`.
  - Inline the failure mode as a hard negative constraint (`[PROHIBITED]`, `DoF = 0`).
- [ ] Calculate Mean Squared Error ($\text{MSE}$) between intended specification and actual outcome.

### State 3: Autopoietic Doctrine & Gatekeeper Evolution
- [ ] If $\text{MSE} > 0$:
  - Submit candidate RFC to the ACME Review Board.
  - Patch upstream `verify.py` turnstiles to mechanically catch the defect in future runs.
- [ ] If $\text{MSE} == 0$: Seal systemic equilibrium and record state to long-term memory.

---

## 3. EVALUATION & ADVERSARIAL GATE

### A. Writers' Room Focus
- **Architect:** Ensures that scar tissue additions do not inflate systemic complexity or bloat token overhead.
- **Proceduralist:** Verifies that every new RFC conforms strictly to Kelsen normative hierarchy standards.
- **Scarred Senior:** Verifies that the proposed invariant genuinely prevents the root pathology without creating brittle edge cases.

### B. Murphy Stress Filter
- **Escape Vector 1 (Overfitting):** Adding overly specific rules that break general capability while fixing a single bug.
- **Escape Vector 2 (Amnesia):** Logging friction in narrative text without upgrading mechanical turnstiles.
- **Escape Vector 3 (Doctrine Bloat):** Accumulating redundant rules that dissipate agent attention budgets.

---

## 4. BACKPROPAGATION & PLOTTER LOGIC
- **Horizontal Oscillation (Δθ Plotter):**
  - If Overfitting detected: Plotter elevates specific symptom to a generalized domain invariant in State 2.
  - If Doctrine Bloat detected: Plotter consolidates duplicate invariants through ontological subsumption.
- **Inter-Layer Escalation Protocol (Vertical Dynamics - ΔZ):**
  - **Global Memory Loop:** Analyzes all vertical collapses (ΔZ) and horizontal oscillations (Δθ) recorded across the vortex descent.
  - **Autopoietic Scar Ingestion:** If a vertical collapse occurred during the execution cycle, an explicit RFC and a mechanical turnstile check must be committed to `verify.py` before the system achieves quiescent equilibrium (MSE -> 0).
- **Iteration Ceiling ($N_{\max} = 3$):** Quench Gate halt and biological arbitration.

---

## 5. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `operational_friction_analyzed == True`
- [ ] `scar_tissue_rfc_formulated == True` (if friction observed).
- [ ] `mechanical_turnstile_patched == True` (automated gate added for new failure modes).
- [ ] `systemic_mse_minimized == True` ($\text{MSE} \to 0$).
- [ ] Handoff Artifact: `artifacts/RETROSPECTIVE_SCAR_REPORT.md` sealed.
- [ ] State Persistence: Long-term memory updated and Merkle release tree confirmed quiescent.

