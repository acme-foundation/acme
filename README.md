# ACME: Lex Proceduralis Agentium
### Release v3.2.0 | Statutory Adjudication, Jurisprudential Caching & Pure Procedural Engine
> *"Nulla Actio Sine Spec, Nullum Iudicium Sine Lege"*  
> *(No execution without specification, no judgment without statutory law.)*

**Version:** `v3.2.0`  
**Standard:** Deterministic Specification, Jurisprudential Precedent Caching & Procedural Adjudication (`DoF = 0`)  
**Gatekeeper:** `verify.py` (Zero-dependency stdlib)

---

## The Genesis Manifesto: From Stochastic Generation to Statutory Due Process
ACME elevates large language models (LLMs) from unanchored, hallucinating coding interns into disciplined judicial actors governed by the thousand-year-old rigor of procedural civil law (*Lex Proceduralis Agentium*).

The existential crisis of modern software ecosystems is not that generative models cannot write code; rather, it is the total absence of a procedural code that governs **why** code is written, **what** statutory boundaries it must obey, and **how** architectural dependencies must be settled before touching the physical disk. Under ACME, code is not an act of spontaneous statistical generation; it is an irrevocable execution of a reasoned, cross-examined judicial verdict.

---

## Core Adjudication Doctrines & Jurisprudential Pillars
1. **Statutory Anchoring (Lex Superior & Grounding):** Every deduction, architectural mutation, or code execution must cite explicit statutory authority in the Constitution (`CONSTITUTION.md`), a ratified thesis (`theses/`), or an executed living specification (`artifacts/problem_spec.md`). Unanchored execution evaluates to non-existence ($DoF = 0$, `INV-STATUTORY-ANCHOR-01`).
2. **Arbiter Ground State & PLA (Procedural Economy):** The default operational state of the judicial arbiter or decision-maker is thermodynamic inertia ($\delta S = 0$). Absent demonstrated evidentiary asymmetry or absolute constitutional lock-in, the arbiter actively scans procedural bars to dismiss petitions *in limine* and issue procedural remands, shedding cognitive load and conserving system energy (`INV-ARBITER-PLA-02`).
3. **Jurisprudential Precedent Cache ($O(1)$ Hit vs. Cache Miss):** Ratified specifications, accredited theses, and judicial writs serve as an immutable L2/L3 jurisprudential cache ($O(1)$ lookup). Normative gaps lacking precedent trigger an immediate Cache Miss, strictly prohibiting ad-hoc improvisation and mandating adversarial deliberation from first principles and compulsory upstream RFC escalation (`INV-PRECEDENT-CACHE-03`).
4. **Anti-Extrapolation & Fail-Closed Sovereign Human Gate:** In emergent boundary states unanchored to external reality, models are strictly prohibited from arbitrary extrapolation or inventing axioms ("could not find, so I inferred"). The system transitions immediately into `FAIL_CLOSED` mode; deductions are quarantined as advisory `HYPOTHESIS_REPORT.md` artifacts, and final ratification authority resides exclusively with the sovereign biological human architect (Human-in-the-Loop, `INV-FAIL-CLOSED-EXTRAPOLATION-04`).
5. **Anti-Workaround Suppression & Compulsory RFC (The Anti-Patch Doctrine):** Concealing an architectural defect or missing constraint via local defensive hacks, catch-all exceptions, or mock overrides is struck down as procedural fraud (`REJECT_PROCEDURAL_FRAUD`). Normative voids mandate compulsory upstream Request for Comments (RFC) backpropagation (`INV-ANTI-WORKAROUND-05`).

---

## The Lex Normative Hierarchy
1. **Lex Superior (The Cognitive Constitution):** `CONSTITUTION.md` — Irreducible constitutional invariants, thermodynamic limits, and biological primacy ($DoF = 0$).
2. **Lex Proceduralis (Procedural Protocols):** `workflows/WF_*.md` — Statutory workflows governing spectral triage, adversarial dialectic, execution petitions, and legal reasoning.
3. **Lex Specialis (Workspace Invariants):** `PROJECT_INVARIANTS.md` / `.acme.template` — Local sub-office containment, blast radius constraints, and commercial token circuit breakers.
4. **Lex Executiva (Living Specifications & Writs):** `artifacts/problem_spec.md`, `WRIT_OF_EXECUTION.md`, `specs/` — Deterministic implementation contracts with zero degrees of freedom.

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
6. **Deterministic Reasoning & Adjudicated SDLC:** Every deduction and code execution mandates explicit statutory citation (`INV-STATUTORY-ANCHOR-01`). Local defensive workarounds are struck down as procedural fraud, converting normative voids into compulsory upstream RFCs.

---

## Specification Lifecycle (Core Engine)
ACME operates as an upstream invariant compiler:

1. **Ingestion & Spectral Triage:** Ingest defect logs or raw intent via `workflows/WF_001_SPECTRAL_TRIAGE.md`. Filter subjective adjectives and isolate root-cause frequency.
2. **Pre-Execution Dialectic & Incubation:** Exhaust structural friction in pure NLP via `workflows/WF_002_ADVERSARIAL_INCUBATION_AND_DIALECTIC.md` before any code compilation.
3. **3-Tier Formulation:** Lock architecture strictly across Shell, Layout, and Component contracts ($DoF = 0$).
4. **Adjudication & Execution Gate:** Issue formal execution petitions and judicial writs under `workflows/WF_003_ADJUDICATION_AND_EXECUTION_GATE.md` before physical file mutations.
5. **Statutory Adjudication & Reasoning:** Ground every deduction in constitutional statute and route normative voids via `workflows/WF_004_STATUTORY_ADJUDICATION_AND_REASONING.md`.
6. **Mechanical Verification:** Validate invariant parity, SemVer cadence, and zero-code core purity:
   ```bash
   python verify.py --verify-all
   ```
7. **Downstream Dispatch:** Hand off compiled markdown specification contracts to downstream coding agents (Cursor, Claude Code, AntiGravity).

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
  "extends": "https://github.com/acme-foundation/acme.git#v3.1.0",
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
  "extends": "https://github.com/acme-foundation/acme.git#v3.1.0",
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
  "extends": "https://github.com/acme-foundation/acme.git#v3.1.0",
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
* `CONSTITUTION.md`: The 21 immutable invariants governing zero-drift specification.
* `faculty/`: Foundational theory curriculum (`SYS`, `PHI`, `LAW`).
* `workflows/`: Evolutionary Agent-Based Unified Process (E-AUP) suite (`00_meta_workflow.md`, `WF_001_INCEPTION_TO_SPEC.md` / `WF_001_SPECTRAL_TRIAGE.md`, `WF_002_ADVERSARIAL_INCUBATION_AND_DIALECTIC.md`, `WF_003_ADJUDICATION_AND_EXECUTION_GATE.md`, `WF_004_STATUTORY_ADJUDICATION_AND_REASONING.md`).
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
