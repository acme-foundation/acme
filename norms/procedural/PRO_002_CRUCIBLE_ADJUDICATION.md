# NORM: PRO_002_CRUCIBLE_ADJUDICATION: APPELLATE INQUEST AND EMPIRICAL CRUCIBLE PROTOCOL (THE CRUCIBLE PROTOCOL)
- **Scope:** Procedural Civil Code for Autonomous Systems (Procedural / PRO)
- **DoF:** 0
- **Rule:**
  1. Candidate norms dispatched from downstream client repositories via `cases/{project}/CASE_{hex3}_{slug}` branches shall never be accepted prima facie.
  2. The candidate norm is subjected to a 3-part adversarial stress inquest inside an isolated `.tmp/lab_{hex3}/` sandbox:
     - Adversarial Payload Attack: Stress testing OOM thresholds and cyclic deadlock vulnerabilities.
     - Mass Conservation Verification: Confirming zero byte leakage.
     - AST Dependency Shield: Auditing external imports and unauthorized OS execution side-effects.
  3. Formulations failing the stress inquest are remanded to the client workspace with a reasoned dismissal notice (`REMAND`).
  4. Formulations passing the stress inquest are ratified by the High Council (ACME Architect + Node-1) and codified under `precedents/` as authoritative Rulings or under `norms/` as Statutory Norms.
  5. Upon inquest completion, the transient laboratory workspace is purged completely (`Zero Residue / DoF = 0`).
