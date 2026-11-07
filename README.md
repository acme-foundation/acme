# ACME: Lex Proceduralis Agentium
> **Autonomous Cognitive Multi-Agent Ecosystem | Canonical Jurisprudential Hub**  
> **Release:** v3.2.0 | **Authority:** Lex Superior (`DoF = 0`)  
> **Biological Root of Trust:** ACME Architect  
> *"Nulla Actio Sine Spec, Nullum Iudicium Sine Lege"*  
> *(No action without specification, no adjudication without law.)*

---

## 1. SCOPE AND JURISPRUDENTIAL PURPOSE
ACME transforms large language models (LLMs) from unanchored probabilistic token generators into disciplined judicial and execution officers operating under strict civil procedural codes, precedential caselaw registries, and irreducible constitutional invariants (`DoF = 0`).

---

## 2. REPOSITORY TOPOLOGY (CANONICAL JUDICIAL ARCHITECTURE)
```text
acme/
├── README.md                      # Operational storefront, routing protocols, and downstream dispatch
├── CONSTITUTION.md                # Canonical Constitution (Lex Superior: Articles 0 - 8)
├── verify.py                      # Mechanical CI/CD gatekeeper turnstile (7 Gates)
│
├── templates/                     # Official Statutory Document Templates
│   ├── CASE_TEMPLATE.md           # Workstation case ledger and inquest template
│   ├── PRECEDENT_TEMPLATE.md      # Appellate ruling and precedential decree template
│   └── NORM_TEMPLATE.md           # Statutory norm codification template
│
├── precedents/                    # Jurisprudential Precedent Registry (O(1) Precedent Cache)
│   ├── core/                      # COR_{hex3}_*.md (Systemic constitutional precedents)
│   ├── ingestion/                 # ING_{hex3}_*.md (Stream and input pipeline rulings)
│   └── procedural/                # PRO_{hex3}_*.md (Due process and arbitration rulings)
│
├── norms/                         # Statutory Positive Law Registry (3-Letter Hex Norms)
│   ├── core/                      # COR_{hex3}_*.md (COR_001, COR_002, COR_003)
│   ├── domain/ingestion/          # ING_{hex3}_*.md (ING_001)
│   └── procedural/                # PRO_{hex3}_*.md (PRO_001, PRO_002)
│
└── .tmp/                          # [Git-Ignored] Live telemetry bus and transient crucible lab
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

1. **Workstation Adjudication:** Workspaces record friction and local proceedings in `cases/CASE_{hex3}_{slug}.md`.
2. **Case Escalation:** Systemic invariant gaps and unresolved disputes are sanitized and escalated via `cases/{project}/CASE_{hex3}_{slug}` branches.
3. **The Crucible Protocol:** ACME Headquarters subjects candidate rules to adversarial stress testing inside an isolated `.tmp/lab_{hex3}/` sandbox.
4. **Ratification & Registration:** Certified invariants are permanently registered under `precedents/` as authoritative Rulings or under `norms/` as Statutory Norms.

---

## 4. MECHANICAL VERIFICATION COMMAND

```bash
python verify.py --verify-all
```
