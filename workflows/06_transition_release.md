# WF-006: Phase III — Transition & Release Decontamination Specification
## Pipeline Vector: `[Simulation] ───< 8 >───► [Output: Release Mühür]`
*Macro Phase III Output & Transition Gate (DoF = 0)*

---

## 1. TRIGGER CONTRACT & SCOPE BOUNDARY
- **Pre-condition:** Ingestion of certified test and simulation telemetry from `workflows/05_verification_sim.md`.
- **Primary Goal:** Execute full decontamination sweep (purge PII, eliminate scratch ballast, verify No-BOM UTF-8), enforce SemVer monotonic cadence lock, generate cryptographic Merkle release digest, and apply canonical Git release tag.
- **Degrees of Freedom (DoF):** 0 (Cryptographic release mühür; zero unanchored modifications).
- **Resource Ceiling:** Release execution $\le 30\text{s}$; zero uncommitted git ballast.

---

## 2. PIPELINE TOPOLOGY & NODE-SPRING MATRIX

```text
[SIMULATION] ────────< 8 >────────► [DECONTAMINATION] ────────► [OUTPUT: RELEASE MÜHÜR]
(Crucible Pass)    (Release Seal)    (Clean-Room Purge)           (Merkle Tag & State Delta)
```

### A. Discrete Nodes `[]`
* **Spring `< 8 >` (Release & Decontamination Seal):**
  - Asserts that all upstream verification and adversarial simulation gates are 100% green.
  - Verifies workspace status: zero untracked, corrupted, or unstaged artifacts.
* **Node 9: `[Çıkış / Output]` (Terminal Seal & Production Authority):**
  - Applies cryptographic Merkle commit hash to the repository.
  - Enforces SemVer monotonic version lock.
  - Publishes sealed release deliverable and triggers institutional memory update.

---

## 3. EXPLICIT STATE MACHINE (DoF = 0)

### State 0: Pre-Flight Cleanliness & Telemetry Ingestion
- [ ] Ingest certified simulation telemetry from Phase III.
- [ ] Verify that zero compilation warnings or suppressed tests exist.
- [ ] Check Git working tree: Confirm zero uncommitted or untracked operational files.

### State 1: Workspace Decontamination Sweep
- [ ] Purge Ephemeral Ballast: Cleanse `.tmp/`, `scratch/`, and intermediate test fixtures (`rm -rf .tmp/*`).
- [ ] Run No-BOM UTF-8 Sweep: Verify that all tracked files strictly conform to UTF-8 without byte order marks (`INV-NOBOM-UTF8`).
- [ ] PII & Credential Scrub: Verify zero hardcoded tokens, secret keys, or personally identifiable information leaked into diffs.
- [ ] Core Zero-Code Audit: Confirm core repository contains zero executable artifacts outside `verify.py`.

### State 2: SemVer Cadence & Version Lock Verification
- [ ] Inspect Git log for release tokens:
  - Patch Bumps (`v3.0.x-genesis`): Monotonically permitted for bugfixes and non-breaking contract updates.
  - Minor Bumps (`v3.x.0-genesis`): Clamped under monotonic lock; strictly requires explicit biological `[RELEASE]` token in the commit message.
- [ ] Update version strings in `README.md` and `verify.py` synchronously.

### State 3: Cryptographic Merkle Commit & Git Tag Mühür
- [ ] Stage all verified deliverables: `git add .`.
- [ ] Author standardized, zero-fluff Git commit message conforming to Conventional Commits:
  `feat(...)` / `fix(...)` / `chore(...)`.
- [ ] Apply canonical Git release tag: `git tag v3.0.x-genesis`.
- [ ] Compute repository Merkle root digest.

### State 4: Release Handshake to Backpropagation
- [ ] Record release metadata into `.acme/workspace_state.json`.
- [ ] Hand off release telemetry to `workflows/07_backpropagation.md` for institutional memory integration.

---

## 4. ADVERSARIAL EVALUATION & MURPHY STRESS FILTER

### A. Release Integrity Guardrails
- **Ghost Artifact Rejection:** If an agent leaves temporary scratch scripts in the repo, release aborts immediately (`ABORT_DIRTY_WORKSPACE`).
- **Encoding Drift Rejection:** Any file saved with UTF-16, Latin-1, or UTF-8 with BOM triggers instant rejection.
- **Unverified Tag Rejection:** Pushing a Git tag without a corresponding clean run of `verify.py --verify-all` is prohibited.

### B. Murphy Filter (Top Escape Vectors)
- **Escape Vector 1 (Leaky Credentials):** Test credentials or API tokens committed inside configuration stubs.
  - *Closure:* Automated pre-commit regex scanner sweeps for high-entropy secret patterns.
- **Escape Vector 2 (SemVer Violation):** Bumping minor version autonomously without biological sign-off.
  - *Closure:* `verify.py` SemVer Cadence Gate enforces monotonic clamping.
- **Escape Vector 3 (BOM Infiltration):** Windows PowerShell injecting UTF-8 BOM into modified text files.
  - *Closure:* Explicit binary BOM scanner inspects first 3 bytes of every file.

---

## 5. ANTI-RUMINATION GUARD & ESCALATION PROTOCOLS
- **Release Abort Rule:** Unlike upstream construction phases, Spring `< 8 >` does NOT loop indefinitely. Any decontamination failure aborts release immediately.
- If decontamination or encoding checks fail $\to$ Return to `workflows/04_construction_worker.md` for surgical cleanup ($\Delta \theta$).
- If release tag or SemVer is contested $\to$ `ESCALATE_TO_HUMAN`.

---

## 6. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `workspace_decontaminated == True` (`.tmp/` and scratch purged).
- [ ] `nobom_utf8_verified == True` (100% compliant).
- [ ] `zero_code_core_verified == True` (Only `verify.py` permitted).
- [ ] `semver_cadence_locked == True` (Monotonic version discipline preserved).
- [ ] `cryptographic_merkle_committed == True` (Git commit created).
- [ ] `canonical_git_tag_applied == True` (`git tag` ratified).
- [ ] Telemetry handed off to `workflows/07_backpropagation.md`.
