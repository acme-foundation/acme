# WF-004: Statutory Adjudication, Legal Reasoning & Anti-Workaround Workflow
## Scope: Citation Audit -> Arbiter PLA Inertia -> Anti-Workaround Sieve -> Compulsory RFC (DoF = 0)

### State 0: Statutory Citation & Grounding Audit (Nulla Actio Sine Spec)
- [ ] Universal Citation Injunction (*Nulla Actio Sine Spec, Nullum Iudicium Sine Lege*):
  - Every operational deduction, architectural design, or physical code mutation must provide an explicit statutory citation to:
    1. An article of `CONSTITUTION.md`,
    2. A ratified thesis under `theses/`, or
    3. A bilaterally signed Living Specification under `artifacts/` or `forms/`.
- [ ] Invariant Gate: `INV-STATUTORY-ANCHOR-01` (`REJECT_UNANCHORED_INCEPTION`).
- [ ] Grounding Verification:
  - If valid statutory citation is present: Proceed to State 1.
  - If no constitutional grounding exists: Declare a Normative Void (`NORMATIVE_VOID`). Improvisation, unanchored assumption, or speculative coding is strictly prohibited. Proceed to State 2.

### State 1: Arbiter Ground State (PLA Inertia) & Asymmetry Verification
- [ ] Arbiter Default Ground State (Principle of Least Action / Procedural Economy):
  - The default state of the judicial magistrate or arbiter is inertia ($\delta S = 0$).
  - The magistrate actively scans Lex Exterior and procedural bars to defeat the claim before engaging substantive merits (`INV-ARBITER-PLA-04`).
- [ ] Rejection in Absence of Asymmetry:
  - If affirmative and negative dialectic claims are of comparable plausibility or evidence is symmetrical, the arbiter dismisses the petition on procedural grounds to conserve system energy and shed load.
- [ ] Halting Condition:
  - Deliberation terminates exclusively through:
    1. Thermal Quota Exhaustion (one party conceding or budget cap reached $\le \$1.50$), or
    2. Absolute Evidentiary Lock-in ($DoF = 0$, leaving the arbiter zero leeway to dismiss).
- [ ] Proceed to State 2.

### State 2: Anti-Workaround Sieve & Procedural Fraud Gate
- [ ] Examine proposed implementation diffs, architectural schemas, and dependency links.
- [ ] Workaround Interrogation: Check for covert defensive hacks, empty catch blocks, mock bypasses, or ad-hoc overrides designed to mask architectural friction.
- [ ] Invariant Gate: `INV-ANTI-WORKAROUND-05` (`REJECT_PROCEDURAL_FRAUD`).
  - If a local workaround, shim, or unratified patch is detected:
    * Strike down proposal immediately as procedural fraud (`REJECT_PROCEDURAL_FRAUD`).
    * Issue procedural remand and transfer requirement to State 3 for formal upstream RFC formulation.
  - If proposal represents clean, grounded architecture: Proceed to State 4.

### State 3: Compulsory RFC Escalation & Normative Void Resolution
- [ ] Compulsory Escalation: Compile formal Request for Comments conforming to `templates/RFC_TEMPLATE.md` (`INV-COMPULSORY-RFC-03`).
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
- [ ] Register reasoning chain, statutory citations, and git commit hashes into the decision ledger (`workflows/worklogs/`).
- [ ] Execute mechanical gatekeeper audit: `python verify.py --verify-all`.
- [ ] Confirm 100% binary PASS across all verification gates ($DoF = 0$).
- [ ] Purge ephemeral deliberation ballast (`.tmp/`).
- [ ] Transition execution plane to quiescent `STANDBY`.
