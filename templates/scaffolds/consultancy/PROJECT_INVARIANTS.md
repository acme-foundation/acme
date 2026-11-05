# PROJECT INVARIANTS: CONSULTANCY HUB PMO CONSTITUTION
## Standard: Program Management Office Operational Invariants (DoF = 0)

---

## 1. CLIENT ISOLATION INVARIANT (`INV-ISLAND-BOUNDARY`)
- Every client engagement must reside in a dedicated, isolated sub-office directory:
  `offices/{client_id}/`
- Shared root repositories must NEVER contain client-specific source code, secrets, or operational data.
- Cross-office file access, data sharing, or symbolic links across client boundaries are strictly prohibited (`ISLAND_CONTAINMENT_BREACH`).

---

## 2. SPECIFICATION-FIRST INVARIANT (`INV-SPEC-FIRST`)
- Billable execution or architectural refactoring without a signed Work Order (`forms/FORM_02_SPEC_SIGN_OFF.md`) is prohibited.
- Every client deliverable must trace directly to an explicit requirement anchored in `artifacts/problem_spec.md`.

---

## 3. ZERO-UNJUSTIFIED DEPENDENCY INVARIANT (`INV-MIN-DEPENDENCY`)
- Standalone proof-of-concept (POC) and minimum viable product (MVP) implementations must prioritize standard CDN assets (Tailwind CSS CDN, Lucide Icons) and native platform APIs.
- Adding unvetted third-party npm packages, heavy framework scaffolds, or standalone database services for trivial requirements is prohibited (`REJECT_PARASITIC_DEPENDENCY`).

---

## 4. FINANCIAL & TOKEN CIRCUIT BREAKER (`HARD_BUDGET_STOP`)
- Autonomous task execution for any single task unit is capped at a strict monetary ceiling:
  $$\text{Task Budget Limit} \le \$1.50\text{ USD}$$
- When cumulative token consumption reaches this threshold, the task terminates immediately (`PAUSED_FOR_HUMAN`) and escalates to the Principal Consultant.

---

## 5. SCOPE CREEP SHIELD & AMENDMENT INVARIANT
- Verbal or informal client feature requests are classified as entropic noise (`ENTROPIC_NOISE`).
- Any requirement outside the signed `FORM_02_SPEC_SIGN_OFF.md` triggers an immediate Scope Freeze. A supplementary Work Order must be signed prior to execution.

---

## 6. FORMAL ACCEPTANCE INVARIANT (`INV-FORMAL-ACCEPTANCE`)
- No engagement invoice or milestone release may be issued without an executed `forms/FORM_03_ACCEPTANCE_DELIVERY.md` certifying 100% binary PASS across all defined Definition of Done (DoD) criteria.
