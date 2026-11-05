# ACME: Deterministic Specification Architecture
> A formal framework that compiles natural language intent into zero-drift execution contracts for agentic systems.

**Version:** `v3.0.2-genesis`  
**Standard:** Deterministic Specification (`DoF = 0`)  
**Gatekeeper:** `verify.py` (Zero-dependency stdlib)

---

## Core Pillars
1. **Decoupled Planes:** Absolute boundary between the Cognitive Specification Plane (`acme`) and downstream Execution Planes.
2. **3-Tier Decomposition:** Strict structural hierarchy across all systems:
   - Application Shell (Lifecycle & Service Orchestration)
   - Layouts (Spatial Isolation & Slot Contracts)
   - Components (Independent Composite & Atomic Units)
3. **Spectral Triage:** Fourier-inspired noise attenuation separating high-frequency symptom chatter from fundamental structural defects.
4. **Anti-Monolithic Escalation:** Rejection of default primitive attractors and unmodularized monolithic outputs.
5. **Scale-Invariant Isomorphism:** Macro-architectural invariants mathematically mirrored across micro-level implementations (MSE = 0).

---

## Repository Topology
- `CONSTITUTION.md`: The 9 immutable invariants governing zero-drift specification.
- `faculty/`: Domain faculties codifying foundational theory (`SYS`, `PHI`).
- `workflows/`: Deterministic state-machine decision workflows (e.g., `WF_001_SPECTRAL_TRIAGE.md`).
- `theses/`: Accredited, immutable architectural contracts.
- `verify.py`: Mechanical, zero-dependency CI gatekeeper enforcing zero-code purity and SemVer monotonic discipline.

---

## Verification
To mechanically verify repository integrity and zero-code invariants:

```bash
python verify.py --verify-all
```

---

## Execution Constraints
* Minor version bumps strictly require the `[RELEASE]` token in the commit message.
* Arbitrary code execution or secondary tooling scripts inside core are prohibited.
* Specifications must evaluate to binary PASS/FAIL criteria (DoF = 0).

---

## Downstream Adoption & The Universal `.norm` Manifest
Downstream client projects adopt ACME as an external normative authority (*Lex Superior*), never as application boilerplate.

### 1. Downstream Non-Pollution Invariant
* **Never Clone ACME into Active Projects:** ACME internal governance faculties (`theses/`, `faculty/`, `workflows/`, `CONSTITUTION.md`) must **never** be cloned, unpacked, or committed into downstream client repositories.
* **Separation of Concerns:** ACME is the normative doctrine plane (Lex Superior); the client workspace is the empirical execution plane (`INV-PLANE-SEPARATION`).

### 2. Anchoring via Root `.norm` Manifest
A downstream repository establishes constitutional compliance exclusively through a single root manifest (`.norm`, with backward compatibility for `.acme`):

```json
{
  "$schema": "https://acme-standard.org/schemas/v3/norm.json",
  "repo": "https://github.com/acme-foundation/acme.git",
  "version": "v3.0.2-genesis",
  "mode": "normative_reference",
  "extends": "https://github.com/acme-foundation/acme.git#v3.0.2-genesis",
  "feed": {
    "persona": false,
    "org": false
  }
}
```

### 3. How to Use ACME Downstream
1. **Drop the Manifest:** Place a `.norm` file in the root of your downstream project.
2. **Sidecar Context:** Configure your autonomous AI agent (e.g., Antigravity, Claude Code, Cursor) to reference ACME as an external read-only sidecar specification.
3. **Deterministic Execution:** Direct the agent to follow ACME's canonical state machines before writing code:
   - **Triage & Stabilization:** Ingest input signals and isolate noise (`workflows/WF_001_SPECTRAL_TRIAGE.md`).
   - **3-Tier Decomposition:** Structure code strictly across Shell $\to$ Layouts $\to$ Components.
   - **Specification Lock:** Compile a formal specification (`SPEC.md`) containing hard negative constraints (`[PROHIBITED]`, `DoF = 0`) prior to synthesis.
