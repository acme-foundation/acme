# ACME PIPELINE SPECIFICATION REGISTRY (INV-PIPELINE-EXPANSION)
> **Authority:** CONSTITUTION.md (Article 15: Dynamic Pipeline Expansion & Keystone Precedence)  
> **Status:** CANONICAL PIPELINE SPECIFICATION (`DoF = 0`)  

---

## 1. TELEOLOGICAL PURPOSE
Execution pipelines define strict deterministic input/output trays for discrete domain assets. Direct ad-hoc implementation of new modalities or asset types without a ratified pipeline definition is prohibited (`INV-PIPELINE-EXPANSION-01`).

---

## 2. PIPELINE DEFINITION SCHEMA (`pipelines/{TYPE}_{slug}.yaml`)
Each modal pipeline MUST be registered as an isolated declarative specification:
```yaml
pipeline_id: "{TYPE}_{slug}"
domain: "[audio | graphics | binary | protocol]"
ingress:
  directory: "assets/raw/{slug}/"
  allowed_extensions: [".raw", ".source"]
egress:
  directory: "assets/processed/{slug}/"
  allowed_extensions: [".bin", ".target"]
keystone_dependency: "CAS-XXX"
verification_command: "python verify.py --verify-all"
```

---

## 3. KEYSTONE PRECEDENCE PROTOCOL (INV-KEYSTONE-PRECEDENCE-02)
Secondary asset production, aesthetic pipelines, and auxiliary integrations SHALL NOT execute until the foundational Finite State Machine (Keystone / FSM) is closed and mechanically verified.
