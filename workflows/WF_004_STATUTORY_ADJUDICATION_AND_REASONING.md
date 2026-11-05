# WF-004: Statutory Adjudication, Jurisprudential Caching & Legal Reasoning Workflow
## Scope: Precedent Cache Lookup -> Arbiter PLA Inertia -> Anti-Extrapolation & Fail-Closed Gate -> Adjudicated Materialization (DoF = 0)

### State 0: Statutory Anchoring & Jurisprudential Cache Lookup (Cache Hit vs. Cache Miss)
- [ ] Universal Citation Injunction (*Nulla Actio Sine Spec, Nullum Iudicium Sine Lege*):
  - Every operational deduction, architectural design, or physical code mutation must query the immutable L2/L3 Jurisprudential Precedent Cache:
    1. An article of `CONSTITUTION.md` (Lex Superior),
    2. A ratified thesis under `theses/` (Lex Precedent), or
    3. A bilaterally signed Living Specification under `artifacts/` or `forms/` (Lex Executiva).
- [ ] Invariant Gate: `INV-STATUTORY-ANCHOR-01` (`REJECT_UNANCHORED_INCEPTION`).
- [ ] Jurisprudential Precedent Cache Resolution (`INV-PRECEDENT-CACHE-03`):
  - **Cache Hit ($O(1)$ Fast Path):** If ratified constitutional invariant or thesis precedent matches the target state, retrieve precedent and proceed directly to State 1.
  - **Cache Miss (Normative Void):** If no statutory precedent exists in the cache, declare a Normative Void (`NORMATIVE_VOID`). Unanchored improvisation, statistical guessing, or speculative coding is strictly prohibited. Route immediately to State 3 for Compulsory RFC Escalation.

### State 1: Least-Action Arbitration & Evidentiary Asymmetry (Arbiter Ground State)
- [ ] Arbiter Default Ground State (Principle of Least Action / Procedural Economy):
  - The default state of the judicial magistrate or arbiter is thermodynamic inertia ($\delta S = 0$).
  - The magistrate actively scans Lex Exterior, statutory standing, and procedural bars to defeat the claim *in limine* before engaging substantive merits (`INV-ARBITER-PLA-02`, `INV-ARBITER-PLA-04`).
- [ ] Rejection in Absence of Asymmetry:
  - If affirmative (Constructor) and negative (Adversary) claims are of symmetrical plausibility or evidence is balanced, the arbiter dismisses the petition on procedural grounds and issues a procedural remand (`DISMISSED_ON_PLA_INERTIA`) to conserve cognitive bandwidth and shed system load.
- [ ] Halting Condition:
  - Deliberation terminates exclusively through:
    1. Thermal Quota Exhaustion (one party conceding or financial budget cap reached $\le \$1.50$), or
    2. Absolute Evidentiary Lock-in ($DoF = 0$, leaving the arbiter zero procedural grounds to dismiss).
- [ ] Proceed to State 2 upon issuance of ratified Writ of Execution.

### State 2: Anti-Extrapolation & Fail-Closed Sovereign Human Gate (Anti-Workaround Sieve)
- [ ] Prohibition of Ontological Fabrication (`INV-FAIL-CLOSED-EXTRAPOLATION-04`):
  - In emergent, unmodeled boundary states lacking empirical or statutory correspondence, language models are strictly prohibited from arbitrary extrapolation or inventing ad-hoc axioms ("could not find, so I inferred").
  - The system transitions immediately into `FAIL_CLOSED` mode.
  - Model outputs are quarantined strictly within an advisory hypothesis report: `HYPOTHESIS_REPORT.md`.
  - Sovereign Human Gate (Human-in-the-Loop): Seal and ratification authority resides exclusively with the sovereign biological human architect. Autonomous mutation of execution planes is blocked until explicit human sign-off.
- [ ] Anti-Workaround Sieve & Procedural Fraud Gate (`INV-ANTI-WORKAROUND-05`):
  - Interrogate proposed implementation diffs, architectural schemas, and dependency links for covert defensive hacks, empty try/except blocks, mock bypasses, or ad-hoc overrides designed to mask architectural friction.
  - If a local workaround, shim, or unratified patch is detected:
    * Strike down proposal immediately as procedural fraud (`REJECT_PROCEDURAL_FRAUD`).
    * Issue procedural remand to `artifacts/problem_spec.md` with written rejection grounds.
    * Route requirement to State 3 for formal upstream RFC formulation.
  - If proposal passes anti-extrapolation and anti-workaround verification: Proceed to State 4.

### State 3: Compulsory RFC Escalation & Normative Void Resolution
- [ ] Compulsory Escalation: Compile formal Request for Comments conforming to `templates/RFC_TEMPLATE.md` (`INV-COMPULSORY-RFC-03`, `INV-ANTI-WORKAROUND-05`).
- [ ] Two-Tier Adjudication Cascade:
  - **Tier A (Autonomous Dialectic Resolution):**
    * Red Team and Blue Team in the Writers' Room deliberate whether the gap can be resolved by deducing from existing Lex Superior doctrine under Principle of Least Action ($\delta S = 0$).
    * If consensus is reached: Emit specification amendment and return to State 0.
  - **Tier B (High Board Escalation):**
    * If the gap requires fundamental constitutional precedent or cross-faculty rule creation, pause task (`PAUSED_FOR_HUMAN`).
    * Escalate formal RFC to the High Board: Biological Chief Architect (Node-0) & Review Board President (Node-1).
    * Upon ratification: Inline approved invariant into core doctrine and return to State 0.

### State 4: Adjudicated Materialization & Merkle Sealing
- [ ] Execute atomic construction units ($\le 500$ tokens per diff) with inline statutory citation headers.
- [ ] Register reasoning chain, statutory citations, precedent cache hits, and git commit hashes into the decision ledger (`workflows/worklogs/`).
- [ ] Execute mechanical gatekeeper audit: `python verify.py --verify-all`.
- [ ] Confirm 100% binary PASS across all verification gates ($DoF = 0$).
- [ ] Purge ephemeral deliberation ballast (`.tmp/`).
- [ ] Transition execution plane to quiescent `STANDBY`.
