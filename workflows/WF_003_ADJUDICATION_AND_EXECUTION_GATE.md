# WF-003: Adjudicated Execution Gate & Reversible Petition Workflow
## Scope: Execution Petition -> Adversarial Inquest -> Writ / Remand -> Ledger (DoF = 0)

### State 0: Epistemic Injunction & Execution Bar
- [ ] Universal Injunction: Even if living specifications, architecture blueprints, and component interfaces are fully compiled, **zero code or file mutations may be written to disk**.
- [ ] Direct execution or speculative coding without an adjudicated, reasoned writ of execution is strictly barred (`REJECT_UNPETITIONED_EXECUTION`).
- [ ] Procedural Mandate: The executing worker or agent must formally file an `EXECUTION_PETITION.md` declaring:
  1. Target component and physical file path.
  2. Grounding specification clauses and invariant citations.
  3. Strict Definition of Done (DoD) binary acceptance thresholds.
  4. Bounded blast radius and dependency declarations (`INV-MIN-DEPENDENCY`).
- [ ] Invariant Gate: `INV-PETITION-EXEC-01`. Proceed to State 1.

### State 1: Adversarial Inquest & Procedural Hearing
- [ ] Lodge `EXECUTION_PETITION.md` into the Judicial Writers' Room.
- [ ] Convene Adversarial Inquest Panel:
  - **Defender (Blue Team):** Advocates for the structural necessity and metric fidelity of the petition under the Principle of Least Action ($\delta S = 0$).
  - **Inquest Magistrate (Red Team Adversary):** Interrogates the petition for substantive overreach, covert degrees of freedom, unmodeled failure modes, and boundary leaks.
- [ ] Substantive & Procedural Verification:
  - Substantive Audit: Does the petition address verified root pathology without speculative extras?
  - Procedural Audit: Are token budgets ($\le \$1.50$), zero-code core purity, and No-BOM UTF-8 standards strictly honored?
- [ ] Inquest concludes within $N_{\max} \le 3$ deliberations. Proceed to State 2.

### State 2: Bilateral Verdict (Writ of Execution vs. Procedural Remand)
- [ ] Render Judicial Ruling based on inquest findings:
  - **VERDICT A: WRIT OF EXECUTION (Writ of Adjudication / DoF = 0):**
    * The petition is ratified in full. Issue binding `WRIT_OF_EXECUTION.md` locking all implementation parameters.
    * Proceed to State 3.
  - **VERDICT B: PROCEDURAL REMAND (Remand to Problem Space):**
    * Substantive defects, scope evasion, or missing constraints detected.
    * Issue formal `REJECTION_GROUNDS.md` detailing exact judicial refutations.
    * Invariant Gate: `INV-REMAND-PROPAGATION-03`.
    * Prohibit ad-hoc local patching or silencing of defects (`REJECT_LOCAL_PATCH_BYPASS`).
    * Remand the petition upstream back to `artifacts/problem_spec.md` and component design for fundamental re-specification.

### State 3: Deterministic Materialization Under Judicial Writ
- [ ] Construction Worker ingests the ratified `WRIT_OF_EXECUTION.md` as its sole execution input (`INV-ADJUDICATED-WRIT-02`).
- [ ] Worker materializes atomic code diffs strictly bounded by $\le 500$ tokens per surgical mutation.
- [ ] Any speculative variation, unanchored refactoring, or departure from the explicit writ triggers an immediate circuit breaker halt (`REJECT_UNWRITTEN_MUTATION`).
- [ ] Proceed to State 4.

### State 4: Adjudication Protocol Ledger & Quiescent Sealing
- [ ] Log complete judicial transcript, writ signatures, and resulting git commit hashes into the immutable decision ledger (`workflows/worklogs/`).
- [ ] Run full mechanical gatekeeper verification: `python verify.py --verify-all`.
- [ ] Confirm 100% binary PASS across all verification gates ($DoF = 0$).
- [ ] Purge ephemeral hearing ballast (`.tmp/`).
- [ ] Transition execution plane to quiescent `STANDBY`.

