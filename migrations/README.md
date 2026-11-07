# ACME MIGRATION PROTOCOL (INV-PIPELINE-MIGRATION)
> **Authority:** CONSTITUTION.md (Article 13: Pipeline Topology & Automated Migration)  
> **Status:** CANONICAL MIGRATION SPECIFICATION (`DoF = 0`)  

---

## 1. TELEOLOGICAL PURPOSE
Execution pipelines and filesystem registers mutate deterministically across architectural epochs. To prevent breaking changes and ensure zero divergence across federated downstream workspaces, all structural mutations MUST provide automated, non-destructive migration adapters under `migrations/MIG_{hex3}_{slug}.py`.

---

## 2. ADAPTER CONVENTIONS & LIFECYCLE
1. **Naming Schema:**
   Every migration adapter script MUST follow the trigraph convention:
   `migrations/MIG_{hex3}_{slug}.py`
   Where `{hex3}` is a sequential 3-character hexadecimal counter (`001` to `FFF`).

2. **Non-Destructive Execution (Via Negativa):**
   - Migration scripts MUST NOT destroy, overwrite, or truncate existing artifacts without verification.
   - Any migrated artifact MUST preserve historical cryptographic provenance and byte parity.
   - State transformations MUST execute deterministically: `migrate(state_n) -> state_{n+1}`.

3. **Rollback Determinism:**
   - Every migration adapter script MUST implement an atomic rollback procedure: `rollback(state_{n+1}) -> state_n`.
   - If an unexpected error or integrity gate failure occurs during migration, the adapter MUST fail closed and revert all filesystem mutations to the pre-migration baseline.

---

## 3. DOWNSTREAM WORKSPACE PARITY ENFORCEMENT
Prior to executing cases against a newer ACME upstream release, downstream workspaces MUST execute all pending migration scripts sequentially. Attempting to execute cases against an unmigrated filesystem topography triggers immediate turnstile rejection (`REJECT_UNMIGRATED_TOPOLOGY`).
