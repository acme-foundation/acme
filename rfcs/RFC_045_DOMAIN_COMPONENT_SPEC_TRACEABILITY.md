# RFC REQUEST: DOMAIN-COMPONENT-SPECIFICATION TRACEABILITY & FQN IDENTITY (RFC-045 - REVISION 2)
> **Reporting Client / Node:** ACME Architect  
> **Status:** CANDIDATE_REQUEST (REVISED)  
> **Target Faculty:** faculty-systems (SYS-128 / AUP Evolutionary Triad)  
> **Target Release:** ACME v2.29.0  
> **Constitutional Anchor:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Section II, Article 4 (Dewdrop Boundary Invariant), Article 7 (Downstream Non-Pollution), Article 8 (Dual Normative Stratification), Article 9 (INV-SEQUENCE-PRECEDENCE), Article 11 (INV-ARCHETYPE-INHERITANCE), and Section III (Biological Primacy)

---

## 1. OBSERVED FRICTION (WHAT BROKE?)

- **Context:** In the Agentic Unified Process (E-AUP / `THESIS-039`), projects advance through four lifecycle gates: Inception, Elaboration, Construction, and Transition. In real-world downstream workspaces (such as Premier Studio), a major architectural impedance mismatch emerged between the high-level human problem space and atomic living specifications (`specs/SPEC_xxx.md`):
  1. *The Inception Gap:* Human-centered problem-to-solution narratives (e.g. user journeys, physical friction, business context) have no formal structural home in downstream archetypes. They are either forced into rigid DoF specification tables prematurely or dumped into gitignored `artifacts/` directories, where they risk loss during evening retreat garbage collection (`INV-RETREAT-02`).
  2. *The Component Gap:* There is no formal, standardized concept of a **Component** with a stable, machine-readable identity. Functional boundaries, responsibilities, and relationships are scattered across narrative text or tightly coupled 1:1 to single specification files, preventing clean many-to-many relationships.
  3. *The Traceability Void:* There is no standardized, bidirectional evidence chain connecting:
     $$\text{Domain Problem} \longleftrightarrow \text{Domain Solution} \longleftrightarrow \text{Component (FQN)} \longleftrightarrow \text{SPEC-xxx} \longleftrightarrow \text{Implementation} \longleftrightarrow \text{Verification Evidence}$$
  4. *False Readiness & Epistemological Confusion:* Specifications cite document references interchangeably with empirical proof, obscuring whether a capability is merely specified or actually verified. Often, agents falsely infer verification simply from the physical existence of a file on disk.

- **Root Tension:** Classical Agile Unified Process (AgUP) provides rich modeling disciplines (Vision, Business Case, Component Model), whereas ACME's Pure NLP Living Spec model collapsed all requirements directly into atomic `specs/SPEC_xxx.md` files. We require a formal **Domain-Component-Specification** triad that preserves the human-readable "Why" and "What" without diluting or fragmenting the centralized, machine-processable specification library.

---

## 2. THE THREE-TIER CONCEPTUAL SEPARATION

ACME establishes three distinct, decoupled conceptual layers. **Identity and location are strictly independent.**

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. DOMAIN (WHY) — Inception Gate                                                       │
│    Problem Space, Teleological Intent, Stakeholder Needs, Business Context             │
│    Format: Human-readable Markdown Narratives                                          │
│    Canonical Location: domain/ (e.g., domain/video_production/problem_vision.md)       │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ informs & bounds
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 2. COMPONENT (WHAT & HOW) — Elaboration Gate                                           │
│    Functional Responsibility, Behavior, Boundaries, Dependencies                      │
│    Identity: Stable Canonical ID (CID) + Hierarchical Semantic FQN                    │
│    Syntax: [Namespace].[Subdomain].[Component] (Many-to-Many Binding to SPECs)        │
│    Canonical Location: components/ (e.g., components/ingest.md + component.json)       │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ binds many-to-many (No ID Renumbering)
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 3. SPECIFICATION (EXECUTABLE CONTRACT) — Centralized Library                           │
│    Centralized living engineering specifications library (Preserving SPEC-xxx IDs)     │
│    DoF Budget Tables: Lex (DoF=0) vs. Norms (DoF>=1), Pre-Mortem Anti-Pattern Gates    │
│    Canonical Location: specs/ (e.g., specs/SPEC_002_CADENCE_HEADLESS_VIDEO_PIPELINE.md)│
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │ implemented by / verified by
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 4. IMPLEMENTATION & EVIDENCE — Construction / Transition Gate                          │
│    Pure stdlib Source Modules (src/) ──> Unit Tests & Cryptographic Artifacts (tests/) │
│    Strict Status Stratification: [SPECIFIED] vs [IMPLEMENTED] vs [VERIFIED]            │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.1. Layer 1: Domain (The "Why")
- **Purpose:** Durable Inception artifacts capturing the human experience, domain ethnography, business case, and stakeholder constraints.
- **Form:** Rich, expressive, human-readable documentation without the rigid syntactic constraints of living specifications.
- **Hierarchy:** Housed in a dedicated `domain/` directory tree (e.g., `domain/problem_statement.md`, `domain/solution_vision.md`).
- **Rule:** Domain narratives are durable assets committed to version control, never staged in transient `artifacts/` directories.

### 2.2. Layer 2: Component (The "What & How")
- **Purpose:** Defines the functional boundaries, behavioral contracts, interface requirements, and dependency graph of a cohesive architectural subsystem.
- **Identity Architecture:**
  1. *Canonical Identifier (CID):* An immutable, opaque structural symbol (e.g., `cid:comp-005-ingest`), guaranteeing permanent referential integrity regardless of future renamings.
  2. *Fully Qualified Name (FQN):* A human-readable, dot-separated hierarchical namespace (e.g., `PremierStudio.VideoProduction.Ingest`).
- **Namespace Migration & Refactoring Behavior:**
  - Renaming a component mutates its FQN but preserves its underlying CID.
  - When an FQN is renamed, the component manifest records a forwarding alias:
    ```yaml
    cid: "cid:comp-005-ingest"
    fqn: "PremierStudio.MediaPipeline.Ingest"
    aliases:
      - fqn: "PremierStudio.VideoProduction.Ingest"
        deprecated_in: "v0.2.0"
        sunset_epoch: "v0.5.0"
    ```
  - Verification engines support bidirectional alias resolution throughout the migration window.
- **Relationship:** Components have **many-to-many** relationships with living specifications. A component may implement parts of several specifications, and a single specification may govern multiple interacting components.

### 2.3. Layer 3: Specification (The "Executable Contract")
- **Purpose:** Machine-processable, unambiguous engineering contracts governing invariants, state transitions, and acceptance criteria.
- **Centrality Invariant:** All living specifications reside exclusively in the centralized `specs/` directory, retaining their canonical, permanent identifiers (`SPEC-001`, `SPEC-002`, etc.).
- **Boundary:** Specifications must NEVER be fractured into component subfolders, nor renamed to mirror component FQNs. Narrative context is referenced from `domain/`, not duplicated inside the specification.

---

## 3. PROPOSED DUAL SPECIFICATION (LEX VS. NORM)

### SECTION A: THE LEX (INVIOLABLE HARD INVARIANTS, DoF = 0)
*Violations halt pipeline compilation immediately (`REJECT_TRACEABILITY_BREACH`).*

1. **INV-FQN-IDENTITY-01 (Dual Identity & Namespace Migration):**  
   Every component must possess an immutable Canonical Identifier (CID) and a valid hierarchical Fully Qualified Name (FQN) formatted in PascalCase dot-notation:  
   $$\text{FQN} = \langle\text{Namespace}\rangle.\langle\text{Subdomain}\rangle.\langle\text{Component}\rangle$$  
   Semantic namespace renames require an explicit alias declaration preserving the CID. Breaking references without an active alias deprecation window is strictly prohibited (`REJECT_DANGLING_FQN`).

2. **INV-SPEC-CENTRALITY-02 (Centralized Living Spec Library & Stable IDs):**  
   Living specifications must reside centrally in the `specs/` directory and retain their stable numerical IDs (`SPEC-001`, `SPEC-002`, etc.). Narrative domain text shall not pollute the specification body, and specifications shall not be scattered across component directories.

3. **INV-BIDIRECTIONAL-TRACEABILITY-03 (Bidirectional Provenance Navigation):**  
   The workspace must maintain an explicit, machine-navigable bidirectional traceability matrix:
   $$\text{Domain Problem} \longleftrightarrow \text{Domain Solution} \longleftrightarrow \text{Component (FQN)} \longleftrightarrow \text{SPEC-xxx} \longleftrightarrow \text{Implementation} \longleftrightarrow \text{Verification Evidence}$$
   Forward navigation (Problem $\to$ Evidence) and reverse navigation (Evidence $\to$ Problem) must resolve deterministically.

4. **INV-EVIDENCE-INTEGRITY-04 (Evidence Stratification & Zero False Readiness):**  
   Traceability mappings must strictly distinguish between textual declaration and empirical proof. **Verification can NEVER be inferred from the mere existence of a file on disk.**
   - `[SPECIFIED]`: Requirement is codified in living specification; implementation is pending or partial.
   - `[IMPLEMENTED]`: Source code is committed in `src/`, but test verification has not passed or been executed.
   - `[VERIFIED]`: Empirical test execution passes 100% green with recorded test logs, exit code 0, and verifiable cryptographic artifact hashes.
   - `[UNRESOLVED]`: Active normative conflict or unfulfilled upstream dependency.  
   Promoting an unverified capability to `VERIFIED` without active test execution results in immediate compiler rejection (`REJECT_FALSE_VERIFICATION`).

5. **INV-ROOT-PURITY-PRESERVATION-05 (Downstream Archetype Directory Authorization):**  
   To house durable Inception narratives and Component definitions without violating constitutional Root Purity (`verify.py`), the downstream archetype schema (`ALLOWED_ROOT_DIRS`) is amended to officially authorize:
   ```python
   ALLOWED_ROOT_DIRS = {
       ".git", ".vscode", "engine", "specs", "rfcs", "web",
       "src", "tests", "artifacts", "raw_test", "experiments",
       "domain", "components"  # <-- Explicitly authorized persistent trees
   }
   ```
   Creating unauthorized ad-hoc directories outside this schema remains strictly prohibited (`REJECT_ROOT_POLLUTION`).

---

### SECTION B: THE NORMS (ADAPTIVE GUIDANCE & HEURISTICS, DoF >= 1)
*Advisory guidelines and best practices. Deviation is permitted with explicit architectural rationale.*

1. **NORM 1 (Traceability Matrix Storage):**  
   Downstream projects should maintain a consolidated `TRACEABILITY.md` (or machine-parsable `traceability.json`) in the project root or `specs/`, regenerated automatically upon milestone release.

2. **NORM 2 (Component Sizing & Cohesion):**  
   Components should represent cohesive architectural units with a single primary responsibility. A component typically binds to 1–3 living specifications.

3. **NORM 3 (Visual Traceability Graph):**  
   Complex multi-tier systems should provide a Mermaid flowchart rendering the bidirectional traceability chain in the domain documentation.

---

## 4. DEFINITION OF DONE (DoD) FOR RATIFICATION

- [x] Candidate RFC-045 revised with dual FQN identity (CID + FQN) and migration lifecycle.
- [x] Conceptual separation between Domain (Why), Component (What/How), and Spec (Contract) locked.
- [x] Identity and location decoupling formalized.
- [x] Prohibition against inferring verification from file existence locked (`INV-EVIDENCE-INTEGRITY-04`).
- [x] Downstream root purity directory authorization (`domain/`, `components/`) explicitly defined.
- [ ] Explicit review and approval received from ACME Architect (Human Root of Trust).
