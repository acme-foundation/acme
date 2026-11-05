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

### 1. Architectural Philosophy & System Mechanics
ACME functions as a decoupled **Cognitive Control Plane** that governs how autonomous engineering agents (e.g., Antigravity, Claude Code, Cursor) interact with codebase reality:

1. **Manifest Anchoring:** Drop a `.norm` file at the root of the target project and initialize.
2. **Contextual Field Analysis (Greenfield vs. Brownfield):**
   - **Greenfield (New Projects):** In the absence of existing code, the system immediately locks generation onto strict 3-tier modular contracts (`Shell -> Layouts -> Components`) and formal living specifications (`SPEC.md`).
   - **Brownfield (Existing Repositories):** The system performs an epistemic audit to isolate legacy dependencies, bounding the blast radius to prevent cascading failure before subjecting new modifications to telemetric triage.
3. **Workspace Topologies (Control Center vs. Decoupled Repositories):**
   - **Control Center Model (Recommended):** Maintain the root repository as the central governance cockpit while integrating active projects as independent repositories or sub-directories.
   - **Sidecar Model:** Maintain projects externally and link them to ACME as an immutable remote normative standard.
4. **Corporate Norms & Policy Injection:**
   Custom organizational policies, architectural rules, or compliance standards can be declared directly within the manifest (`corporate_norms`). AI agents treat these as constitutional negative constraints (`DoF = 0`) that cannot be bypassed.

---

### 2. Implementation Manifest Examples

#### A. Greenfield Project Manifest (`.norm`)
```json
{
  "$schema": "https://acme-standard.org/schemas/v3/norm.json",
  "project_name": "payments-service",
  "project_type": "greenfield",
  "extends": "https://github.com/acme-foundation/acme.git#v3.0.2-genesis",
  "control_mode": "strict_gatekeeper",
  "architecture": {
    "tier_enforcement": "shell-layout-component",
    "zero_degrees_of_freedom": true
  },
  "corporate_norms": [
    "All service endpoints must expose OpenAPI specifications before code implementation",
    "Zero binary dependencies: All logic must compile locally from verified source"
  ]
}
```

#### B. Brownfield Legacy Project Manifest (`.norm`)
```json
{
  "$schema": "https://acme-standard.org/schemas/v3/norm.json",
  "project_name": "legacy-core-portal",
  "project_type": "brownfield",
  "extends": "https://github.com/acme-foundation/acme.git#v3.0.2-genesis",
  "control_mode": "quarantine_and_isolate",
  "brownfield_policy": {
    "legacy_scope": "src/legacy/",
    "blast_radius_containment": "strict",
    "isolation_adapter": "facade_boundary"
  },
  "corporate_norms": [
    "Never mutate legacy data schemas directly; implement defensive wrappers",
    "Zero PII logging: All customer identifiers must be masked across log telemetry"
  ]
}
```

#### C. Central Control Cockpit Manifest (`.norm`)
```json
{
  "$schema": "https://acme-standard.org/schemas/v3/norm.json",
  "workspace_role": "control_center",
  "extends": "https://github.com/acme-foundation/acme.git#v3.0.2-genesis",
  "subprojects": [
    {
      "path": "services/identity-provider",
      "repo": "https://github.com/org/identity-provider.git",
      "type": "brownfield"
    },
    {
      "path": "apps/web-client",
      "repo": "https://github.com/org/web-client.git",
      "type": "greenfield"
    }
  ],
  "corporate_norms": [
    "Subproject Isolation: Mutations cannot span multiple service boundaries within a single pull request",
    "Unified Diagnostics: All service anomalies must emit standardized telemetric signatures"
  ]
}
```
