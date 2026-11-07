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
├── CONSTITUTION.md                # Root Invariants & System Protocols (Articles 0 - 11)
├── verify.py                      # Mechanical CI/CD gatekeeper turnstile (8 Gates)
│
├── cases/                         # Active execution ledgers and arbitration tickets
│   └── CASE_{hex3}_{slug}.md      # Bounded mutation scope and invariant linkage
│
├── templates/                     # Official Document Templates
│   ├── CASE_TEMPLATE.md           # Anomaly triage and conflict analysis template
│   ├── PRECEDENT_TEMPLATE.md      # Ground truth precedent record template
│   └── NORM_TEMPLATE.md           # Statutory norm codification template
│
├── precedents/                    # Ratified Precedent Registry (O(1) Precedent Cache)
│   ├── core/                      # COR_{hex3}_*.md (Systemic constitutional precedents)
│   ├── ingestion/                 # ING_{hex3}_*.md (Stream and input pipeline rulings)
│   └── procedural/                # PRO_{hex3}_*.md (Due process and arbitration records)
│
├── norms/                         # Statutory Positive Law Registry (3-Letter Hex Norms)
│   ├── core/                      # COR_{hex3}_*.md (COR_001, COR_002, COR_003)
│   ├── domain/ingestion/          # ING_{hex3}_*.md (ING_001)
│   └── procedural/                # PRO_{hex3}_*.md (PRO_001, PRO_002)
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
    "branch_template": "cases/{project_name}/CASE_{hex3}_{slug}",
    "auto_dispatch": true
  }
}
```

### Downstream to Headquarter Adjudication Lifecycle

1. **Workstation Adjudication:** Workspaces record friction and local proceedings in `cases/CASE_{hex3}_{slug}.md`. Opening any case or initiating an escalation strictly mandates binding to the latest canonical upstream ACME HEAD commit (`INV-MERKLE-PARITY-01`) and registered execution bounds (`INV-MANDATORY-CASE-BINDING`).
2. **Case Escalation:** Systemic invariant gaps and unresolved disputes are sanitized and escalated via `cases/{project}/CASE_{hex3}_{slug}` branches.
3. **Isolated Sandbox Verification (Adversarial Rig):** ACME Headquarters subjects candidate rules to adversarial stress testing inside an isolated `.tmp/lab_{hex3}/` sandbox.
4. **Registration:** Certified invariants register as canonical ground truth under `precedents/` as authoritative records or under `norms/` as Statutory Norms.

---

## 4. MECHANICAL VERIFICATION COMMAND

```bash
python verify.py --verify-all
```
