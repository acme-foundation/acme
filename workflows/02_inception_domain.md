# WF-002: Phase I-II Transition — Inception & Domain Contract Specification
## Pipeline Vector: `[Diagnostics] ──► [Contract Seal] ──► artifacts/problem_spec.md`
*Macro Phase I to II Transition Gate (DoF = 0)*

---

## 1. TRIGGER CONTRACT & SCOPE BOUNDARY
- **Pre-condition:** Ingestion of sealed `artifacts/telemetry_digest.md` emitted by `workflows/01_triage_and_digest.md`.
- **Primary Goal:** Translate diagnostic findings into a falsifiable, mathematically bounded `artifacts/problem_spec.md` with explicit Negative Scope (Via Negativa) and zero solution bias.
- **Degrees of Freedom (DoF):** 0 (Hard statutory specification lock).
- **Resource Ceiling:** Token consumption $\le 1200$ tokens; review latency $\le 500\text{ms}$.

---

## 2. TRANSITION TOPOLOGY & ARTIFACT MATRIX

```text
[TELEMETRY DIGEST] ────► [ONTOLOGICAL GROUNDING] ────► [NEGATIVE SCOPE GATE] ────► [problem_spec.md]
(Diagnostic Input)       (Domain Invariants)           (Via Negativa / Banned)     (Sealed Contract)
```

### A. Core Architectural Responsibilities
1. **Ontological Grounding:** Anchors the diagnosed anomaly to the Lex Superior constitution (`CONSTITUTION.md`) and ratified theses (`theses/`).
2. **Domain Boundary Demarcation:** Defines exact interface coordinates, type schemas, and system layers affected.
3. **Via Negativa / Negative Scope:** Explicitly catalogs what the solution MUST NOT touch, mutate, or introduce.
4. **Falsifiable Ground-Truth Criterion:** Defines binary Boolean pass/fail conditions for the subsequent construction phase.

---

## 3. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Ingestion Integrity & Digest Verification
- [ ] Ingest `artifacts/telemetry_digest.md`.
- [ ] Verify cryptographic digest and check for unresolved symptom/root ambiguities.
- [ ] If digest contains subjective fluff or unmeasured claims: Reject and fall back to `workflows/01_triage_and_digest.md` (`Δθ = 1`).

### State 1: Ontological Grounding & Invariant Extraction
- [ ] Map defect to core constitutional invariants (`INV-*`).
- [ ] Identify applicable statutory contracts, schemas, and type definitions.
- [ ] Verify Principle of Least Action (PLA): Confirm that solving this problem requires minimum systemic entropy ($\delta S = 0$).

### State 2: Negative Scope Boundary Formulation (Via Negativa)
- [ ] Formulate Explicit Prohibitions:
  - List files, directories, and subsystems that must NOT be modified.
  - Ban prohibited dependencies, unapproved libraries, or runtime sidecars.
  - Ban speculative features, cosmetic refactoring, or adjacent module cleanups.
- [ ] Codify hard negative constraints as `[PROHIBITED]` ($DoF = 0$).

### State 3: Falsifiable Acceptance Criteria Definition
- [ ] Define ground-truth acceptance criteria:
  - Binary metric threshold (e.g., $P_{99} \le 120\text{ms}$, error rate $= 0.00\%$, memory leakage $= 0\text{ bytes/hr}$).
  - Exact command line verification probe (e.g., `python verify.py --verify-all`).
- [ ] Confirm zero implementation speculation: Spec must not dictate specific code algorithms or internal variable names.

### State 4: Specification Seal (`problem_spec.md`)
- [ ] Synthesize immutable `artifacts/problem_spec.md`.
- [ ] Affix cryptographic SHA-256 seal.
- [ ] Formal handoff to Macro Phase II (`workflows/03_elaboration_arch.md`).

---

## 4. ADVERSARIAL EVALUATION & MURPHY STRESS VECTORS
- **Escape Vector 1 (Solution Smuggling):** Operator or agent embedding subtle architectural prescriptions inside the problem statement.
  - *Closure:* Automated linter pass; any mention of implementation patterns (e.g., "use a Redis cache") triggers `REJECT_SOLUTION_LEAKAGE`.
- **Escape Vector 2 (Unbounded Blast Radius):** Ambiguous boundary definitions allowing downstream workers to refactor adjacent code.
  - *Closure:* Mandatory explicit whitelist of modifiable file paths.
- **Escape Vector 3 (Unfalsifiable Success Criteria):** Success defined through vague performance promises ("faster", "more robust").
  - *Closure:* Acceptance criteria must parse as binary Boolean expressions (`evaluates_to_boolean == True`).

---

## 5. DUAL-SCALE PLOTTER LOGIC & VERTICAL ESCALATION
- **Horizontal Micro-Oscillation ($\Delta \theta$):**
  - If Negative Scope contains ambiguities, loop back to State 2. Clamped at $N_{\max} = 3$.
- **Vertical Cascading Collapse ($\Delta Z$):**
  - If inception analysis proves that the problem statement is self-contradictory or violates constitutional invariants:
    - Trigger `CASCADE_COLLAPSE_TO_PHASE_1`.
    - Eject speculative draft artifacts.
    - Revert altitude coordinate to `workflows/01_triage_and_digest.md`.
- **Biological Primacy:** If contradiction cannot be resolved across 2 vertical regress passes $\to$ `ESCALATE_TO_HUMAN`.

---

## 6. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `digest_signature_verified == True`
- [ ] `ontological_anchors_mapped == True` (`CONSTITUTION.md` parity checked).
- [ ] `negative_scope_codified == True` (Explicit `[PROHIBITED]` boundaries established).
- [ ] `acceptance_criteria_strictly_boolean == True`
- [ ] `zero_solution_leakage == True` (100% pure problem specification).
- [ ] Handoff Artifact: `artifacts/problem_spec.md` sealed with Merkle digest.
