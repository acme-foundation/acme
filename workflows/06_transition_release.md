# WF-006: Transition & Release Workflow
## Scope: Environment Decontamination, Merkle Non-Repudiation & Tag Sealing (DoF = 0)
*Classical AUP Discipline: Deployment*

---

## 1. TRIGGER CONTRACT
- **Pre-condition:** Certified `artifacts/VERIFICATION_CERTIFICATE.json` from WF-005 with 100/100 crucible pass rate.
- **Input Types:** Release candidate codebase, documentation suite, Git index, and tag manifest.
- **Degrees of Freedom (DoF):** 0 (Cryptographic release discipline; zero discretionary mutations).
- **Resource Ceiling:** Release packaging latency $\le 30\text{s}$; zero uncommitted working tree artifacts.

---

## 2. INNER MICRO-LOOP & STATE MACHINE (TRIAGE -> DIAGNOSE -> SOLVE)

### State 0: Release Candidate Quarantine & Audit
- [ ] Verify verification certificate: Does it possess an untampered cryptographic signature?
  - NO: Reject release candidate immediately (`REJECT_UNSEALED_BINARY`).
  - YES: Proceed to State 1.

### State 1: Forensic Decontamination
- [ ] Scan codebase for local environment leakage:
  - Zero hardcoded local file paths (e.g., `C:\Users\...`, `/home/...`).
  - Zero PII, developer credentials, or internal test keys.
  - Zero uncommitted runtime artifacts (`.tmp`, `.log`, `.swp`).
- [ ] Enforce clean-room isolation between PMO governance and public distribution tree (`INV-PLANE-SEPARATION`).

### State 2: SemVer Cadence & Quench Enforcement
- [ ] Verify SemVer target:
  - Major ($X$): Requires explicit Biological Architect token.
  - Minor ($Y$): Requires explicit `[RELEASE]` token in commit message (`INV-SEMVER-QUENCH-GATE`).
  - Patch ($Z$): Advances monotonically for iterative releases and retreat seals.
- [ ] Bar any unauthorized minor bump attempt (`REJECT_UNAUTHORIZED_SEMVER_MUTATION`).

### State 3: Merkle Commit & Git Tag Ratification
- [ ] Stage all ratified files into git index.
- [ ] Commit with semantic commit prefix (`docs(canon):`, `feat(core):`, `refactor(core):`).
- [ ] Generate and force-seal immutable Git release tag (`v3.0.x-genesis`).
- [ ] Push clean main branch and tag to remote origin.

---

## 3. EVALUATION & ADVERSARIAL GATE

### A. Writers' Room Focus
- **Architect:** Confirms release tree contains zero secondary scripts or tooling leaks.
- **Proceduralist:** Verifies Merkle tree SHA is permanently anchored to the graduation record.
- **Scarred Senior:** Checks that tag naming and commit messages conform strictly to upstream SemVer contracts.

### B. Murphy Stress Filter
- **Escape Vector 1 (Dirty Working Tree):** Unstaged or untracked temporary files left behind during release tagging.
- **Escape Vector 2 (Tag Detachment):** Tag pointing to a detached or unmerged commit SHA.
- **Escape Vector 3 (Remote Desync):** Local tag differing from the published remote repository tag.

---

## 4. BACKPROPAGATION & PLOTTER LOGIC
- **Horizontal Oscillation (Δθ Plotter):**
  - If Dirty Working Tree detected: Plotter halts tagging, executes clean-room purge, and returns to State 1.
  - If SemVer Quench Gate breached: Plotter clamps version strictly to authorized Patch digit.
- **Inter-Layer Escalation Protocol (Vertical Dynamics - ΔZ):**
  - **Local Tolerance (Δθ):** Maximum 3 micro-oscillations within Phase 06.
  - **Macro Fracture Trigger:** If post-release verification detects uncommitted runtime artifacts, PII leakage, or unverified binary blobs:
    - **Vertical Fallback Target (ΔZ):** Revert release packaging immediately; drop altitude to `workflows/05_verification_eval.md`.
    - **Pruning & Ballast Ejection:** Local release tags are rolled back, and contaminated artifacts are quarantined.
- **Iteration Ceiling ($N_{\max} = 3$):** Quench Gate halt and developer escalation upon persistent release failure.

---

## 5. DEFINITION OF DONE (DoD) & MERKLE SEAL
- [ ] `git_status_working_tree_clean == True` (0 unstaged / 0 untracked).
- [ ] `merkle_commit_sha_anchored == True`.
- [ ] `release_tag_synchronized_with_remote == True`.
- [ ] Handoff Artifact: Published release tag (`v3.0.x-genesis`) and updated `live_state.json`.
- [ ] State Persistence: Quiescent retreat state recorded.

