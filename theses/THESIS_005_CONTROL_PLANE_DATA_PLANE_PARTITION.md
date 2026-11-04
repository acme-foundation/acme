# THESIS SPEC: CONTROL PLANE DATA PLANE PARTITION AND CLEAN-ROOM ISOLATION (GENESIS-005)
> **Candidate Node:** node-005  
> **Faculty:** faculty-systems  
> **Release Target:** ACME v3.0.0-Genesis  
> **Constitutional Anchor:** CONSTITUTION.md Article 5 (Control Plane / Data Plane Partition)  
> **Attribution:** 100% Core Foundation  

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Article 5 (Control Plane / Data Plane Partition) and Article 2 (Zero-Bin Distribution).
* **Problem Formulation:** When autonomous governance harnesses, internal thesis archives, and PMO control structures contaminate the public runtime distribution, the resulting deliverable becomes bloated, leaky, and vulnerable to intellectual property exposure and governance tampering. Conversely, completely severing public runtimes prevents upstream specifications from learning from real-world execution failures.
* **Negative Boundary Condition (Via Negativa):** Exporting PMO/governance artifacts into standalone production repos, or leaking user PII and credentials back into upstream control planes during telemetry feedback is strictly prohibited (`REJECT_PLANE_CONTAMINATION`, DoF = 0).

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt pipeline compilation immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific failure modes cataloged and strictly prohibited:*
* **FAILURE MODE 1 (Governance Artifact Leakage into Runtime):** Shipping internal curricula, candidate theses, and PMO files (`.norm`, `CONSTITUTION.md`) in production applications -> `[PROHIBITED]` Strict unidirectional clean-room filter allowing only pure `src/`, `tests/`, and public docs (`INV-CLEAN-ROOM-01`).
* **FAILURE MODE 2 (Telemetry PII Breach & Privacy Leak):** Transmitting raw user data or unscrubbed stack traces from client devices to headquarters -> `[PROHIBITED]` Zero-PII differential Scar Signatures hashed via SHA-256 (`INV-REVERSE-TELEMETRY-02`).
* **FAILURE MODE 3 (Amnesic Defect Recurrence):** Upstream control planes failing to assimilate confirmed downstream failures into negative constraints -> `[PROHIBITED]` Mandatory permanent search-space pruning via immutable Scar Tokens (`INV-SCAR-PRUNING-03`).

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Clean-Room Filter** | **$\text{DoF} = 0$** | *Lex Invariant* | Production projection must contain zero internal governance files. Unfiltered export is rejected. |
| **Reverse Telemetry Privacy** | **$\text{DoF} = 0$** | *Privacy Invariant* | Telemetry payloads must exclude absolute paths, tokens, and PII. Only mathematical error digests admitted. |
| **Runtime Packaging** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Runtime packaging format (Tauri binary, headless wheel, container) adapts to deployment targets. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INVARIANT 1 (Clean-Room Boundary):** The projection from PMO to standalone runtime allows only: `src/`, `tests/`, `README.md`, and `LICENSE`. Presence of `.norm`, `.acme`, `theses/`, or `curriculum/` in a public repository fails pre-flight verification (`REJECT_PMO_CONTAMINATION`).
* **INVARIANT 2 (Differential Scar Feedback):** Downstream runtime defects are serialized into anonymous error signatures ($E_{\text{class}} \parallel \text{NormalizedAST}$) and submitted upstream as candidate RFCs without human data exposure.
* **INVARIANT 3 (State Sibling Independence):** Runtime volatile state resides in `.acme.state.json` sibling files; under no circumstance is the root manifest mutated into a directory.

---

## 4. DEFINITION OF DONE (DoD)
- [x] Verified UTF-8 No-BOM pure NLP specification.
- [x] Pre-Mortem Anti-Pattern Gates (Section 1.4) codified with hard negative constraints (`[PROHIBITED]`).
- [x] Formally registered as Genesis Core Thesis 005.
