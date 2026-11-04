# THESIS SPEC: AUTONOMOUS OVERSIGHT AND THE FOUR-STAGE GOVERNANCE LOOP (GENESIS-004)
> **Candidate Node:** node-004  
> **Faculty:** faculty-systems  
> **Release Target:** ACME v3.0.0-Genesis  
> **Constitutional Anchor:** CONSTITUTION.md Article 4 (Autonomous Oversight & Writer's Room Closed Loop)  
> **Attribution:** 100% Core Foundation  

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Article 4 (Autonomous Oversight) and Article 7 (Cadence Discipline).
* **Problem Formulation:** Single-pass code generation by autonomous models is inherently brittle, hiding blind spots, hallucinated APIs, and subtle security flaws. Conversely, unbounded iterative multi-agent debate introduces cognitive inflation, burning excessive compute tokens and overwhelming human review capacity ($v_{\text{production}} \gg v_{\text{human}}$).
* **Negative Boundary Condition (Via Negativa):** Releasing code without red-team adversarial examination, permitting unconstrained circular review loops beyond 3 iterations, or flooding biological operators with un-summarized model chatter is strictly prohibited (`REJECT_UNCONSTRAINED_OVERSIGHT`, DoF = 0).

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt pipeline compilation immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific failure modes cataloged and strictly prohibited:*
* **FAILURE MODE 1 (Single-Pass Blind Release):** Shipping generated code straight to production without adversarial challenge -> `[PROHIBITED]` Mandatory Critic examination prior to code construction (`INV-CRITIC-PREFLIGHT-01`).
* **FAILURE MODE 2 (Infinite Review Thrashing & Inflation):** Review loop oscillating indefinitely between critic and executor -> `[PROHIBITED]` Hard ceiling clamped at exactly three (3) iterations, triggering Quench Gate upon non-convergence (`INV-QUENCH-GATE-02`).
* **FAILURE MODE 3 (Cognitive Exhaustion of Human Principal):** Spawning multi-agent committee transcripts that exceed biological assimilation bandwidth -> `[PROHIBITED]` Mandatory two-paragraph epistemic distillation for human review (`INV-COGNITIVE-BUDGET-03`).

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Governance Loop Stages** | **$\text{DoF} = 0$** | *Lex Invariant* | Execution must sequence through: Critic $\to$ Spec Patch $\to$ Execution $\to$ Delivery Referee. |
| **Iteration Ceiling** | **$\text{DoF} = 0$** | *State Invariant* | Loop count strictly bounded to $\le 3$ iterations. Iteration 4 raises `QUENCH_HALT`. |
| **Critic Heuristics** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Red-team perturbation strategies adapt dynamically to target domain vulnerability profiles. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INVARIANT 1 (The Four-Stage Circuit):** No capability may transition from intent to production without passing: (1) Critic adversarial formulation $\to$ (2) Spec patch insertion $\to$ (3) Atomic execution $\to$ (4) Referee verification.
* **INVARIANT 2 (The Quench Gate):** If referee verification fails after iteration 3, the entire task is quarantined, memory state is dumped as a State Delta, and control yields to biological arbitration.
* **INVARIANT 3 (Tag Discipline):** Intermediate iterations and mid-day sprint milestones do not mint SemVer release tags; tagging is reserved exclusively for consolidated daily retreat.

---

## 4. DEFINITION OF DONE (DoD)
- [x] Verified UTF-8 No-BOM pure NLP specification.
- [x] Pre-Mortem Anti-Pattern Gates (Section 1.4) codified with hard negative constraints (`[PROHIBITED]`).
- [x] Formally registered as Genesis Core Thesis 004.
