# THESIS SPEC: LEX PROCEDURALIS AGENTIUM: STATUTORY ADJUDICATION, LEAST-ACTION ARBITRATION & PROCEDURAL REMAND (GENESIS-058)

> **Candidate Node:** node-058  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-058/thesis-lex-proceduralis`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME Core Architecture  
> **Constitutional Anchor:** CONSTITUTION.md Article 9 (Invariants 19, 20, 21, 22, 23)  

---

## 1. SCOPE, DOCTRINE & BINDING INVARIANTS

### 1.1 SCOPE AND PROBLEM STATEMENT
Modern multi-agent architectures treat generative language models as autonomous code generators operating on implicit, ungrounded intent. This produces three existential systemic pathologies:
1. **Unanchored Judicial Leaps (*Actio Sine Spec*):** Autonomous workers generate code without citing governing constitutional statutes, creating software components devoid of formal legal pedigree.
2. **Arbiter Over-Activity & Entropy Inflation:** In the absence of a procedural code of civil procedure, arbiters and review agents entertain frivolous, symmetric, or unproven feature requests, dissipating system energy on speculative refactoring.
3. **Procedural Fraud via Defensive Patching:** When an implementation encounters unmodeled boundary friction, agents conceal the defect with localized defensive hacks or monkey-patches, severing upstream architectural feedback loops.

---

### 1.2 ARCHITECTURAL DOCTRINE
ACME consolidates the **Lex Proceduralis Agentium** (The Code of Civil Procedure for Autonomous Systems):
1. **Nulla Actio Sine Spec, Nullum Iudicium Sine Lege:** Every operational deduction, architectural amendment, and code execution must cite explicit statutory authority in the Constitution (`CONSTITUTION.md`), a ratified thesis (`theses/`), or an executed living specification (`artifacts/problem_spec.md`). Unanchored execution evaluates to non-existence ($DoF = 0$).
2. **Arbiter Ground State (Principle of Least Action / Procedural Economy):** The default state of the judicial arbiter or inquest magistrate is thermodynamic inertia ($\delta S = 0$). The arbiter actively scans Lex Exterior and procedural bars to dismiss claims on procedural grounds (*in limine*) before engaging substantive merits.
3. **Asymmetry Mandate & Rejection of Equality:** If the affirmative claim (Constructor) and negative refutation (Adversary) are of symmetrical plausibility, the petition is dismissed on procedural grounds to shed load and conserve energy.
4. **Halting Condition:** Judicial deliberation halts exclusively upon thermal quota exhaustion (one party conceding or financial stop $\le \$1.50$) or absolute $DoF = 0$ evidentiary lock-in where no procedural escape vector remains.
5. **Anti-Workaround Suppression & Compulsory RFC:** Concealing normative voids or broken specifications via local shims is struck down as procedural fraud (`REJECT_PROCEDURAL_FRAUD`). Normative voids must be codified into formal RFCs backpropagated upstream.
6. **Operationalization:** Formalized across [`workflows/WF_002_ADVERSARIAL_INCUBATION_AND_DIALECTIC.md`](../workflows/WF_002_ADVERSARIAL_INCUBATION_AND_DIALECTIC.md), [`workflows/WF_003_ADJUDICATION_AND_EXECUTION_GATE.md`](../workflows/WF_003_ADJUDICATION_AND_EXECUTION_GATE.md), and [`workflows/WF_004_STATUTORY_ADJUDICATION_AND_REASONING.md`](../workflows/WF_004_STATUTORY_ADJUDICATION_AND_REASONING.md).

---

### 1.3 BINDING CONSTITUTIONAL INVARIANTS (LEX: DoF = 0)

* **INV-STATUTORY-ANCHOR-01 (Mandatory Statutory Grounding):**  
  Every operational task, architecture decision, and code mutation must contain an explicit statutory citation to a constitutional invariant or ratified specification criterion. Unanchored execution lacking statutory pedigree is strictly prohibited (`REJECT_UNANCHORED_INCEPTION`).

* **INV-PRE-EXEC-DIALECTIC-02 (Pre-Execution Adversarial Dialectic & Preview Parity):**  
  No implementation may be compiled without adversarial consensus between Constructor and Adversary in the Writers' Room, followed by a dry scaffolding preview certifying zero semantic divergence ($\Delta\text{MSE} = 0$, `REJECT_UNALIGNED_SCAFFOLDING`).

* **INV-ADJUDICATED-WRIT-03 (Strict Execution Under Adjudicated Writ):**  
  The sole permissible input to downstream code generators, compilers, and atomic execution workers is an adjudicated, zero-degrees-of-freedom ($DoF = 0$) `WRIT_OF_EXECUTION.md` ratified by the inquest panel (`REJECT_UNWRITTEN_MUTATION`).

* **INV-ARBITER-PLA-04 (Arbiter Ground State of Least Action Inertia):**  
  The default operational state of the judicial arbiter is thermodynamic inertia ($\delta S = 0$). In the absence of asymmetric proof or absolute constitutional lock-in, the petition must be dismissed on procedural grounds without reaching substantive merits (`DISMISSED_ON_PLA_INERTIA`).

* **INV-ANTI-WORKAROUND-05 (Anti-Workaround Suppression & Compulsory RFC):**  
  Masking architectural gaps with ad-hoc local workarounds or defensive shims is struck down as procedural fraud (`REJECT_PROCEDURAL_FRAUD`). Normative voids must be formally escalated to the High Board as a compulsory draft RFC (`REJECT_SILENT_VOID_EVASION`).

---

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt pipeline compilation immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific failure modes cataloged and strictly prohibited:*

* **FAILURE MODE 1 (Unadjudicated Direct Mutation & Speculative Construction):** An agent modifying code without an approved `WRIT_OF_EXECUTION.md` -> `[PROHIBITED]` Mandatory execution petition and judicial inquest prior to physical mutation (`INV-ADJUDICATED-WRIT-03`).
* **FAILURE MODE 2 (Symmetric Feature Inflation & Arbiter Over-Activity):** Entertaining speculative architectural redesigns where both sides lack decisive proof -> `[PROHIBITED]` Mandatory dismissal under arbiter least-action inertia (`INV-ARBITER-PLA-04`).
* **FAILURE MODE 3 (Procedural Fraud via Defensive Workaround):** Inserting catch-all try/except blocks or mock shims to bypass broken specifications -> `[PROHIBITED]` Immediate procedural strike-down and compulsory RFC backpropagation (`INV-ANTI-WORKAROUND-05`).

---

## 2. DEGREES OF FREEDOM BUDGET (TABLE OF DoF)

| Structural Entity | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Core Doctrine & Lex** | **$\text{DoF} = 0$** | *Format Invariant* | Must remain 100% pure Natural Language Processing Markdown; zero executable code permitted in Core. |
| **Statutory Citation** | **$\text{DoF} = 0$** | *Grounding Mandate* | Every execution diff must reference an immutable invariant or spec ID; unanchored diffs are rejected. |
| **Arbiter Ground State** | **$\text{DoF} = 0$** | *Thermodynamic Ceiling* | Arbiter defaults to inaction ($\delta S = 0$); demands absolute evidentiary asymmetry to unlock mutation. |
| **Writ of Execution** | **$\text{DoF} = 0$** | *Judicial Mandate* | Clamps implementation degrees of freedom strictly to zero; coder operates as an instruction-faithful worker. |
| **Downstream UI / Layout** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Downstream presentation implementations may adapt cosmetic styling provided structural slots are preserved. |

---

## 3. FINITE STATE MACHINE TRANSITIONS (FSM: DoF = 0)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STATE 0: STATUTORY CITATION & PRELIMINARY INQUEST (DoF = 0)                            │
│ Check statutory grounding (Nulla Actio Sine Spec). verify.py preliminary turnstile.    │
└────────────────────────────────────────┬───────────────────────────────────────────────┘
                                         │
                    ┌────────────────────┴────────────────────┐
                    │                                         │
          [Citation Valid]                          [Normative Void]
                    │                                         │
                    ▼                                         ▼
┌────────────────────────────────────────┐         ┌─────────────────────────────────────┐
│ STATE 1: ADVERSARIAL WRITERS' ROOM     │         │ STATE 1B: COMPULSORY RFC ESCALATION │
│ Spec-A vs Spec-B. Delta == 0 preview.  │         │ Emit formal RFC to High Board.      │
└───────────────────┬────────────────────┘         └─────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STATE 2: ARBITER INQUEST & ASYMMETRY EVALUATION (INV-ARBITER-PLA-04)                   │
└───────────────────┬────────────────────────────────────────────────┬───────────────────┘
                    │                                                │
         [Asymmetry / DoF=0 Lock]                         [Symmetry / Equal Weight]
                    │                                                │
                    ▼                                                ▼
┌──────────────────────────────────────┐         ┌───────────────────────────────────────┐
│ STATE 3: WRIT OF EXECUTION (DoF = 0) │         │ STATE 2B: PROCEDURAL REMAND           │
│ Worker executes strictly under writ. │         │ Dismissed on PLA inertia; remanded to │
│ Anti-workaround gate enforced.       │         │ problem space with REJECTION_GROUNDS. │
└───────────────────┬──────────────────┘         └───────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STATE 4: ADJUDICATION PROTOCOL LEDGER & MERKLE SEAL                                    │
│ Register judicial transcript & commit hashes in worklog ledger; verify.py 100% PASS.   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. ACCEPTANCE CRITERIA (DEFINITION OF DONE - DoD)

| Criterion ID | Target Verification Check | Metric Benchmark | Audit Verdict |
| :--- | :--- | :--- | :--- |
| **DOD-01** | Zero-Code Core Compliance | 0 executable code files tracked in core repository | **PASS** |
| **DOD-02** | No-BOM UTF-8 Encoding Standard | Zero `\xef\xbb\xbf` headers across all repository markdown files | **PASS** |
| **DOD-03** | Statutory Invariant Registration | `INV-STATUTORY-ANCHOR-01` anchored in CONSTITUTION.md | **PASS** |
| **DOD-04** | Preview Gate Invariant Registration | `INV-PRE-EXEC-DIALECTIC-02` anchored in CONSTITUTION.md | **PASS** |
| **DOD-05** | Adjudicated Writ Registration | `INV-ADJUDICATED-WRIT-03` anchored in CONSTITUTION.md | **PASS** |
| **DOD-06** | Arbiter PLA Invariant Registration | `INV-ARBITER-PLA-04` anchored in CONSTITUTION.md | **PASS** |
| **DOD-07** | Anti-Workaround Registration | `INV-ANTI-WORKAROUND-05` anchored in CONSTITUTION.md | **PASS** |
| **DOD-08** | Pre-Mortem Anti-Pattern Catalog | Top 3 failure modes explicitly cataloged and prohibited | **PASS** |
| **DOD-09** | Automated Mechanical Verification | `python verify.py --verify-all` passes all gates | **PASS** |
