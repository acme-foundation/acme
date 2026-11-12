# ACME: Autonomous Cognitive Multi-Agent Ecosystem
> **Deterministic Living Specification & Canonical Governance Hub**  
> **Release:** v3.2.0 | **Authority:** Hierarchical Governance: Root Invariants > Procedural Protocols > Local Invariants (`DoF = 0`)  
> **Biological Root of Trust:** ACME Architect  
> **Invariant:** Strict Specification Enforcement (Zero Unmeasured Execution).  

---

## 1. SCOPE AND SYSTEM ARCHITECTURE
ACME transforms large language models (LLMs) from unanchored probabilistic token generators into deterministic state-machine execution units operating under strict systems protocols, precedent caselaw registries, and irreducible constitutional invariants (`DoF = 0`).

---

## 2. REPOSITORY TOPOLOGY
```text
acme/
├── README.md                      # Operational storefront, routing protocols, and downstream dispatch
├── CONSTITUTION.md                # Root Invariants & System Protocols (Articles 0 - 20)
├── verify.py                      # Mechanical CI/CD gatekeeper turnstile (17 Gates)
│
├── cases/                         # Active execution ledgers and arbitration tickets
│   └── CAS_{hex3}_{slug}.md      # Bounded mutation scope and invariant linkage (Flat topology)
│
├── templates/                     # Official Document Templates
│   ├── CAS_TEMPLATE.md           # Anomaly triage and conflict analysis template
│   ├── PRE_TEMPLATE.md           # Ground truth precedent record template
│   ├── NORM_TEMPLATE.md           # Statutory norm codification template
│   ├── TENANT_NORM_TEMPLATE.json # Declarative tenant baseline contract template
│   └── specs/                    # Canonical 8-tier living-spec & AUP lifecycle templates (9 files)
│
├── precedents/                    # Ratified Precedent Registry (O(1) Precedent Cache)
│   └── PRE_{hex3}_{slug}.md      # Canonical ecosystem rulings and evidentiary anchors
│
├── norms/                         # Statutory Positive Law Registry (3-Letter Hex Norms)
│   ├── core/                      # COR_{hex3}_*.md (COR_001, COR_002, COR_003)
│   ├── domain/ingestion/          # ING_{hex3}_*.md (ING_001)
│   └── procedural/                # PRO_{hex3}_*.md (PRO_001, PRO_002, PRO_003, PRO_004)
│
├── pipelines/                     # Declarative modal pipeline contracts and I/O specifications
│   ├── README.md                  # Pipeline schema definition, ingress/egress boundaries, and keystone rules
│   └── PIP_001_aup_living_spec.yaml # Agentic Unified Process living-spec pipeline definition
│
├── migrations/                    # Deterministic pipeline and schema migration registry
│   └── README.md                  # Migration adapter protocol, execution lifecycle, and rollback rules
│
└── .tmp/                          # [Git-Ignored] Live telemetry bus and transient adversarial rig
```

---

## 3. DOWNSTREAM DISPATCH AND INTEGRATION PROTOCOL (.norm)

Downstream client workspaces bind ACME as their external supreme normative authority via a single root `.norm` manifest, routing statutory change proposals upstream:

```json
{
  "norm_version": "1.0",
  "project_name": "client-core",
  "extends": "https://github.com/acme-foundation/acme.git#v3.2.0",
  "active_norm_scopes": [
    "norms/core/*",
    "norms/domain/ingestion/*",
    "norms/procedural/*"
  ],
  "upstream_dispatch": {
    "remote": "origin",
    "branch_template": "cases/{project_name}/CAS_{hex3}_{slug}",
    "auto_dispatch": true
  }
}
```

### Downstream to Headquarter Adjudication Lifecycle

1. **Workstation Adjudication:** Workspaces record friction and local proceedings in `cases/CAS_{hex3}_{slug}.md`. Opening any case or initiating an escalation strictly mandates binding to the latest canonical upstream ACME HEAD commit (`INV-MERKLE-PARITY-01`) and registered execution bounds (`INV-MANDATORY-CASE-BINDING`).
2. **Case Escalation:** Systemic invariant gaps and unresolved disputes are sanitized and escalated via `cases/{project}/CAS_{hex3}_{slug}` branches.
3. **Isolated Sandbox Verification (Adversarial Rig):** ACME Headquarters subjects candidate rules to adversarial stress testing inside an isolated `.tmp/lab_{hex3}/` sandbox.
4. **Registration:** Certified invariants register as canonical ground truth under `precedents/` as authoritative records or under `norms/` as Statutory Norms.

---

## 4. CANONICAL EXECUTION INVARIANTS

### 4.1. Orthogonal Blind-Spot Gate (Adversarial Invariance)
During adversarial twin review (Spec A / Builder vs. Spec B / Discriminator), after verifying reciprocal defect coverage, both nodes MUST collaboratively answer the mandatory orthogonal question:
> *"What is the shared implicit premise that both parties accepted without verification (the unasked question)?"*

The identified systemic blind spot MUST immediately be codified into the project living specification (`specs/const.md`) as a non-negotiable negative constraint (**Hard Guardrail / DoF = 0**).

### 4.2. Non-LLM Critic Grounding (Anti-Consensus-Illusion)
Dual-LLM verification loops (Actor-Critic / Spec-A vs. Spec-B) risk producing an "illusion of consensus" through mutual linguistic plausibility. Sole reliance on LLM inference for dialectic sign-off is prohibited (`DoF = 0`). The Critic seat MUST anchor to at least one non-LLM deterministic source of ground truth:
- Empirical error traces and execution telemetry (`.tmp/*.log`).
- Mathematical limit proofs and boundary calculations.
- Compiler, linter, or automated gatekeeper test turnstile results (`verify.py`, exit code 0).
- Sovereign biological human architect sign-off (`DECISION_LOG`).

### 4.3. Industry Interlingua Mapping Standard
Internal doctrinal purity is preserved within the ACME Core; however, all outward outputs (including SPEC, README, API contracts, and technical reports) translate canonical terminology into standard industry equivalents:

| Canonical ACME Doctrine | Industry Interlingua Standard |
| :--- | :--- |
| **Constitution / Lex Superior** (`CONSTITUTION.md`) | Governance-as-Code & Agent Harness |
| **Immutable Invariant (`DoF = 0`)** | Hard Guardrail & Contract-First Schema |
| **Adversarial Twin / Red-Blue Dialectic** | Adversarial Evals & Actor-Critic Loop |
| **Scar Tissue Ingestion** | Episodic Trajectory & Regression Dataset |
| **Budget / Early Exit** | Inference Compute Budgeting & Circuit Breaker |
| **Dewdrop Boundary Isolation** | Blast Radius Containment & Least-Privilege Sandboxing |

---

## 5. MECHANICAL VERIFICATION COMMAND

```bash
python verify.py --verify-all
```
