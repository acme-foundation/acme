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
