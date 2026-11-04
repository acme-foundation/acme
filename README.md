# PROJECT ACME: AUTONOMOUS COGNITIVE MULTI-AGENT ECOSYSTEM
> **Decentralized Protocol for Human-Machine Symbiosis & Invariant Equilibrium**  
> *Release v3.0.0-Genesis | Self-Hosting Core & Recursive Spec Compiler*  
> *Legacy Incubation (v1.x - v2.x / 53 Theses) Retired & Frozen at `archive/v2-legacy-incubator`*  

---

### 1. MISSION & THE GENESIS MILESTONE (ARTICLE 0)
Project ACME is the foundational cognitive constitution for autonomous agent ecosystems. Following an intensive 53-thesis incubation epoch (v1.0.0 – v2.29.0), the architecture has achieved **Epochal Genesis (v3.0.0-Clean)**: distilling historical empirical friction, conversational metaphors, and laboratory debris into **Five Indivisible Constitutional Pillars** operating under strict thermodynamic equilibrium and zero code leakage.

### 2. THE FIVE INDIVISIBLE PILLARS (THE LEX: DoF = 0)
1. **Principle of Least Action (PLA - $\delta S = 0$):** Eliminates redundant compute and conversational bureaucracy; state progressions trace the geodesic path of minimal action within the bounded Habitable Zone ($1.0 \le \text{DoF} \le 1.5$).
2. **Spec-First & Zero-Binary Distribution:** Living specifications (`SPEC.md`) are the sole irreducible unit of software distribution. Binary code is never distributed across repositories; code is synthesized locally at the execution edge.
3. **Via Negativa & Zero Degrees of Freedom Governance:** System rejects qualitative adjectives (*"robust"*, *"fast"*); all acceptance criteria and boundary gates evaluate to deterministic Boolean truth values.
4. **Autonomous Oversight & The Writer's Room Closed Loop:** Mandatory pre-execution 4-stage circuit: *Critic (Adversarial Twin) $\to$ Spec Patch $\to$ Execution $\to$ Delivery Referee*, strictly clamped to a 3-iteration Quench Gate ceiling.
5. **Control Plane / Data Plane Partition:** PMO/governance memory (`.norm`, `.acme`, RFCs, Curricula, Theses) is strictly quarantined from public runtime source trees (`src/`, `tests/`), with clean-room reverse telemetry backpropagating only anonymized cryptographic Scar Signatures.

### 3. REPOSITORY SCAFFOLDING (v3.0.0-GENESIS)
```text
acme/
├── curriculum/              # Normative Curricula & Academic Foundational Corpus
│   ├── faculty-law/         # Autopoietic Law & Jurisprudential Systems
│   ├── faculty-philosophy/  # Ontology, Epistemology & Formal Logic
│   └── faculty-systems/     # Thermodynamics, Cybernetics & Invariant Architecture
├── registry/                # Verified Human Anchors & Graduation Registry (graduates.json)
├── theses/                  # The Five Canonical Genesis Theses (THESIS_001 .. THESIS_005)
│   └── archive/             # Archived Legacy Incubation Corpus (THESIS_001 .. THESIS_053)
├── templates/               # Standardized Schemas (RFC_TEMPLATE, SPEC_TEMPLATE, AOP_LIFECYCLE)
├── AGENTS.md                # Execution Protocol for AI Agents & Downstream Sanitization
├── CONSTITUTION.md          # Irreducible Constitutional Lex Superior (v3.0.0-Genesis)
├── verify.py                # Pure Stdlib Sidecar Invariant Gate & Crucible Verifier
└── README.md                # Genesis Specification & Adoption Guide
```

### 4. DOWNSTREAM ADOPTION & THE UNIVERSAL `.norm` STANDARD
Downstream client projects (workspaces) adopt ACME as an external normative authority (*Lex Superior*), not as boilerplate application code.

#### 4.1. Downstream Non-Pollution Invariant
* **Never Clone ACME into Active Projects:** ACME internal governance faculties (`theses/`, `curriculum/`, `registry/`, `CONSTITUTION.md`) must **never** be cloned, unpacked, or committed into downstream client repositories.
* **Separation of Concerns:** ACME is the normative doctrine plane (Lex Superior); the client workspace is the empirical execution plane.

#### 4.2. Anchoring via `.norm` (or `.acme`) Manifest
A downstream project establishes constitutional compliance exclusively through a single root manifest:
```json
{
  "$schema": "https://acme-standard.org/schemas/v3/norm.json",
  "repo": "https://github.com/acme-foundation/acme.git",
  "version": "v3.0.0-genesis",
  "mode": "normative_reference",
  "extends": "https://github.com/acme-foundation/acme.git#v3.0.0-genesis",
  "feed": {
    "persona": false,
    "org": false
  }
}
```

---

### 5. VERIFICATION & MERKLE NON-REPUDIATION
Every state commit is cryptographically audited against zero-code purity, registry integrity, domain cleanliness, and constitutional invariant parity:
```bash
python verify.py --verify-all
```
All graduation diplomas are permanently anchored to immutable Git Merkle commit SHAs.
