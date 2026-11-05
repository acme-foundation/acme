# ACME: Deterministic Specification Architecture
> A formal framework that compiles natural language intent into zero-drift execution contracts for agentic systems.

**Version:** `v3.0.7-genesis`  
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

## Specification Lifecycle (Core Engine)
ACME operates as an upstream invariant compiler:

1. **Ingestion & Spectral Triage:** Ingest defect logs or raw intent via `workflows/WF_001_SPECTRAL_TRIAGE.md`. Filter subjective adjectives and isolate root-cause frequency.
2. **Pre-Execution Dialectic & Incubation:** Exhaust structural friction in pure NLP via `workflows/WF_002_ADVERSARIAL_INCUBATION_AND_DIALECTIC.md` before any code compilation.
3. **3-Tier Formulation:** Lock architecture strictly across Shell, Layout, and Component contracts ($DoF = 0$).
4. **Mechanical Verification:** Validate invariant parity, SemVer cadence, and zero-code core purity:
   ```bash
   python verify.py --verify-all
   ```
5. **Downstream Dispatch:** Hand off compiled markdown specification contracts to downstream coding agents (Cursor, Claude Code, AntiGravity).

---

## Downstream Adoption & The Universal `.norm` Manifest
Downstream client projects adopt ACME as an external normative authority (*Lex Superior*), never as application boilerplate.

### 1. Initialization & Field Triage
Place a `.norm` manifest at the client repository root and instruct the agent:

> *"Initialize workspace against .norm manifest."*

The system automatically performs contextual field analysis:
* **Greenfield (New Projects):** In the absence of existing code, execution is immediately bounded by strict 3-tier modular contracts and formal binary acceptance criteria.
* **Brownfield (Legacy Codebases):** Performs dependency and defect isolation, defining strict blast-radius boundaries around legacy code before applying modifications.

### 2. Workspace Topologies
* **Control Center Model (Recommended):** The ACME workspace serves as the central governance cockpit, tracking projects as independent sub-repositories.
* **Sidecar Model:** Client projects exist externally and reference ACME remotely via immutable release tags.

---

### 3. Implementation Manifest Examples

#### A. Greenfield Project Manifest (`.norm`)
```json
{
  "project_name": "payments-service",
  "project_type": "greenfield",
  "extends": "https://github.com/acme-foundation/acme.git#v3.0.7-genesis",
  "corporate_invariants": [
    "All service endpoints must expose OpenAPI specifications before code implementation",
    "Zero binary dependencies: All logic must compile locally from verified source"
  ]
}
```

#### B. Brownfield Legacy Project Manifest (`.norm`)
```json
{
  "project_name": "legacy-core-portal",
  "project_type": "brownfield",
  "extends": "https://github.com/acme-foundation/acme.git#v3.0.7-genesis",
  "legacy_containment": {
    "legacy_scope": "src/legacy/",
    "blast_radius_containment": "strict"
  },
  "corporate_invariants": [
    "Never mutate legacy data schemas directly; implement defensive wrappers",
    "Zero PII logging: Mask all customer identifiers across telemetry"
  ]
}
```

#### C. Central Control Cockpit Manifest (`.norm`)
```json
{
  "workspace_role": "control_center",
  "extends": "https://github.com/acme-foundation/acme.git#v3.0.7-genesis",
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
  "corporate_invariants": [
    "Subproject Isolation: Pull requests cannot mutate multiple service boundaries simultaneously",
    "Unified Diagnostics: All service anomalies must emit standardized telemetric signatures"
  ]
}
```

---

## Repository Topology
* `CONSTITUTION.md`: The 15 immutable invariants governing zero-drift specification.
* `faculty/`: Foundational theory curriculum (`SYS`, `PHI`, `LAW`).
* `workflows/`: Evolutionary Agent-Based Unified Process (E-AUP) suite (`00_meta_workflow.md`, `WF_001_SPECTRAL_TRIAGE.md`, `WF_002_ADVERSARIAL_INCUBATION_AND_DIALECTIC.md`).
* `theses/`: Ratified architectural contracts.
* `verify.py`: Mechanical, zero-dependency CI gatekeeper enforcing zero-code purity and SemVer discipline (12 verification gates).
* `scripts/decontaminator.py`: Pre-commit decontamination shield enforcing zero absolute local paths and zero credential leaks.
* `templates/scaffolds/`: Downstream project scaffolding and formal field forms (`mode: consultancy_hub`, Form 01/02/03).

---

## Verification & Constraints
```bash
python verify.py --verify-all
```

* Minor version bumps strictly require the `[RELEASE]` token in the commit message.
* Arbitrary code execution or secondary tooling scripts inside core are prohibited.
* Specifications must evaluate to binary PASS/FAIL criteria (DoF = 0).
