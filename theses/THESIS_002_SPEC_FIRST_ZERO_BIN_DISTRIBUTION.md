# THESIS SPEC: SPEC-FIRST ZERO-BINARY DISTRIBUTION AND PORTABLE CONTRACTS (GENESIS-002)
> **Candidate Node:** node-002  
> **Faculty:** faculty-systems  
> **Release Target:** ACME v3.0.0-Genesis  
> **Constitutional Anchor:** CONSTITUTION.md Article 2 (Spec-First & Zero-Bin Distribution)  
> **Attribution:** 100% Core Foundation  

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Article 2 (Spec-First & Zero-Bin Distribution) and Article 5 (Control Plane / Data Plane Partition).
* **Problem Formulation:** Classical software engineering couples software distribution to brittle compiled binaries, platform-dependent packages, and centralized proprietary cloud hosts. This introduces vendor lock-in, cloud hostage dynamics, massive network bandwidth exhaustion for large data workloads, and dependency rot.
* **Negative Boundary Condition (Via Negativa):** Distributing closed compiled binaries across repository boundaries, requiring mandatory centralized cloud compute for contract interpretation, or scattering configuration into fragmented dotfile sprawl is strictly prohibited (`REJECT_BINARY_DISTRIBUTION`, DoF = 0).

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt pipeline compilation immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific failure modes cataloged and strictly prohibited:*
* **FAILURE MODE 1 (Binary Hostage & Cloud Lock-in):** Binding software execution to proprietary compiled binaries that cannot be inspected, verified, or reproduced locally -> `[PROHIBITED]` Mandatory living specification compilation at the local execution edge (`INV-ZERO-BIN-01`).
* **FAILURE MODE 2 (Configuration Sprawl & Fragmented Root):** Polluting project roots with fragmented dotfiles (`.org`, `.persona`, `.tool`) -> `[PROHIBITED]` Strict single manifest architecture under `.norm` with immutable fallback to `.acme` (`INV-SINGLE-MANIFEST-02`).
* **FAILURE MODE 3 (Unchecked Network Data Exfiltration):** Automatically uploading raw user assets to remote cloud providers without explicit consent -> `[PROHIBITED]` Default-local data sovereignty; zero outbound data egress without biological authorization (`INV-LOCAL-FIRST-03`).

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Living Spec Portability** | **$\text{DoF} = 0$** | *Lex Invariant* | Specifications must form complete, self-contained, portable engineering contracts. |
| **Manifest Precedence** | **$\text{DoF} = 0$** | *State Invariant* | Manifest resolution strictly follows `[".norm", ".acme"]`. Co-existence is prohibited. |
| **Local Synthesis Runtime** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Workspaces select local execution runtimes (Python stdlib, Rust, Tauri) according to performance targets. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INVARIANT 1 (Zero-Binary Core):** The ACME Core repository shall never track executable binary artifacts (`.exe`, `.dll`, `.bin`, `.pyc`). Distribution consists strictly of verifiable text contracts.
* **INVARIANT 2 (Universal Cascading Manifest):** Workspaces inherit normative governance via 4-tier Kelsen resolution (`Lex Superior` $\leftarrow$ `Lex Corporata` $\leftarrow$ `Portfolio` $\leftarrow$ `Lex Specialis`).
* **INVARIANT 3 (Independent Verifier Primacy):** Correctness is evaluated by deterministic local unit assertions and cryptographic receipts, never by subjective model self-assessment.

---

## 4. DEFINITION OF DONE (DoD)
- [x] Verified UTF-8 No-BOM pure NLP specification.
- [x] Pre-Mortem Anti-Pattern Gates (Section 1.4) codified with hard negative constraints (`[PROHIBITED]`).
- [x] Formally registered as Genesis Core Thesis 002.
