# RFC REQUEST: CROSS-AGENT STATE CONTINUITY AND EVIDENCE-BASED CONTEXT HANDOFF (RFC-044)
> **Reporting Client / Node:** acme-premier-studio (PMO / Control Plane)  
> **Status:** CANDIDATE_REQUEST  
> **Target Faculty:** faculty-systems / faculty-law  
> **Target Release:** ACME v2.29.0  
> **Anchored Theses:** THESIS-001 (Least Action), THESIS-006 (Noise Rejection), THESIS-015 (Epoch Checkpointing), THESIS-029B (Scar Tissue), THESIS-037 (Tri-Tier Fabric), THESIS-038 (Merkle Streaming), THESIS-039 (E-AUP), THESIS-043 (Sequence Precedence), THESIS-044 (Circadian Cadence)  
> **Protocol Anchor:** AOP-LIFECYCLE-SYS-127  

---

## 1. OBSERVED FRICTION & PROBLEM STATEMENT (WHAT BROKE?)

### 1.1. Context & Operational Friction
Across the ACME ecosystem, autonomous workflows and developer operations routinely involve multiple heterogeneous AI agents operating across distinct sessions, varying tool harness environments (e.g., Antigravity IDE, Claude Desktop, CI/CD runners, headless server daemons), or alternating cognitive model families (e.g., Gemini, Claude, GPT).

When a new AI agent joins an existing ACME-governed workspace, it must immediately establish an accurate, comprehensive, and grounded operational model of the project's current status. Currently, there is no standardized, normative, cross-agent state persistence contract. As an empirical consequence:

1. **Conversational Memory Dependence:** Agents and human operators routinely resort to conversational transcripts, prompt-pasting, or chat summaries to transfer context. This violates the **Principle of Least Action (THESIS-001)** and **Semantic Noise Rejection (THESIS-006)** by flooding prompt windows with high-entropy conversational fluff, stale reasoning artifacts, and unverified assumptions.
2. **Stateless Re-Discovery Tax:** Lacking a designated state artifact, newly arriving agents spend excessive cognitive tokens executing ad-hoc exploratory filesystem walks, reading raw source trees, re-running test suites, or inferring requirements from disparate markdown files.
3. **Amnesic Defect Recurrence & Scope Confusion:** Without an immutable record of pending blockers, rejected candidate paths, and pending biological decisions, an incoming agent frequently re-proposes solutions already rejected or attempts actions whose prerequisites remain unfulfilled, violating **INV-SEQUENCE-PRECEDENCE (RFC-038)** and **Anti-Amnesia Process Immunization (THESIS-039)**.
4. **Ungrounded Hallucination of Project State:** In the absence of an explicit state declaration, agents speculate whether a feature is merely planned, drafted in a spec, partially coded, or verified, breaching **Observer Core (CONSTITUTION.md Art 5: `REJECT_SPECULATIVE_STATE`)**.

---

## 2. EXISTING NORMATIVE COVERAGE & PRECEDENT ANALYSIS

ACME Lex Superior (v2.28.0) contains foundational principles addressing state and boundaries, but does not provide a turnkey handoff contract:

1. **CONSTITUTION.md Art 2 (Dynamic Conatus) & Art 5 (Observer Core):** Mandates that on boundary blockages or undefined context, an agent must halt and serialize a `State Delta` to the Biological Root of Trust.  
   *Limitation:* The format, storage location, schema, and consumption protocol of this `State Delta` are unspecified (`SPECIFIED_ONLY`).
2. **THESIS-039 / RFC-016-B (Agentic Unified Process Meta-Pipeline):** Enforces 4 lifecycle gates (Inception, Elaboration, Construction, Transition) and prohibits conversational multi-agent bureaucracy (`INV-EAUP-03: Zero Inter-Agent Chatter`).  
   *Limitation:* E-AUP assumes a single polymath agent morphing roles intra-session. It does not address asynchronous inter-session handoffs between independent agent lifecycles.
3. **THESIS-044 / RFC-039 (Circadian Cadence & Reveille/Retreat Protocol):** Enforces morning alignment (`INV-REVEILLE-01`) and evening retreat (`INV-RETREAT-02`) sealing living state hashes into git.  
   *Limitation:* Sealing git commit hashes records *historical provenance*, but does not formulate a structured, human-and-machine readable ledger of active blockers, verification evidence, and the immediate next authorized action.
4. **THESIS-043 / RFC-038 (Sequence Precedence & Socratic Circuit Breaker):** Strictly forbids premature phase jumps (`INV-SEQUENCE-PRECEDENCE-01`).  
   *Limitation:* Enforces negative bounds (rejection of leaps), but lacks a positive declarative state contract specifying which stage is currently active.
5. **THESIS-037 / RFC-033 (Tri-Tier Context Fabric & Single Root `.acme` Manifest):** Forbids configuration dotfile sprawl (`INV-SINGLE-MANIFEST`).  
   *Limitation:* `.acme` is strictly reserved for static workspace metadata (repo, normative version, mode, feed flags). It is not a volatile runtime execution ledger.

---

## 3. CONFIRMED ARCHITECTURAL GAP

| Project Dimension | Current ACME Baseline | Required Handoff Standard | Gap Status |
| :--- | :--- | :--- | :--- |
| **Project Identity & Purpose** | Statically defined in `.acme`, `README.md` | Verifiable inline teleological invariant | `VERIFIED` |
| **Current Lifecycle Phase** | E-AUP & SYS-127 FSM specified in doctrine | Explicitly declared active phase coordinate | `PARTIAL` |
| **Actual Implementation Status** | Inferred from directory tree & file inspection | Granular taxonomy per capability/work package | `PARTIAL` |
| **Verified Test Results** | `verify.py` executable on-demand | Signed test ledger with timestamp & commit SHA | `PARTIAL` |
| **Active Specs & Dependencies** | Listed in `specs/` (downstream PMO specific) | Standardized cross-project dependency graph | `PARTIAL` |
| **Last Confirmed Milestone** | Git tags and commit messages | Declaratively linked to acceptance criteria | `PARTIAL` |
| **Current Blockers** | Mandated as abstract `State Delta` | Structured, actionable blockage registry | `SPECIFIED_ONLY` |
| **Pending Human Decisions** | Biological Primacy mandated | Explicit decision queue with question & options | `SPECIFIED_ONLY` |
| **Normative & Merkle Provenance** | Sealed commit SHA & `.acme` manifest | Cryptographically bound state ledger | `VERIFIED` |
| **Next Authorized Action** | Inferred by incoming agent | Deterministic work directive with DoF budget | `UNKNOWN` |

**Conclusion:** A genuine normative gap exists across all ACME-governed repositories.

---

## 4. CANDIDATE STATE REPRESENTATIONS & COMPARATIVE EVALUATION

In strict accordance with the Principle of Least Action, this RFC evaluates candidate representations through the normative crucible:

| Representation Option | Pros | Cons | Verdict |
| :--- | :--- | :--- | :--- |
| **Option A: Monolithic Markdown (`STATE.md`)** | Human-readable, zero tooling dependency, renders natively in web/IDE. | Harder to parse deterministically with rigid AST; prone to unstructured prose drift. | Viable for human-centric PMO; high token risk if unconstrained. |
| **Option B: Pure JSON (`state.json` or `.acme/state.json`)** | 100% deterministic schema validation, $O(1)$ programmatic parsing, strict typing. | Inferior human readability; prone to git merge conflicts on concurrent writes. | Ideal for automated execution harnesses and CI/CD pipelines. |
| **Option C: Git Notes / Merkle Stream** | Perfectly coupled to git history; zero filesystem footprint. | Opaque to standard AI toolsets without specialized CLI tools; difficult for humans to inspect. | Violates transparency and least action for local agents. |
| **Option D: Dual-Fidelity Hybrid (Normalized JSON + Auto-Rendered Markdown View)** | Deterministic JSON schema as single source of truth, with lightweight, human-readable markdown summary header. | Requires synchronization discipline. | **RECOMMENDED STANDARD** |

This RFC establishes the normative contract independent of storage syntax, permitting Option B or Option D based on project operational mode.

---

## 5. AGENT-INDEPENDENT HANDOFF CONTRACT & EVIDENCE TAXONOMY

### 5.1. The 7-Element Project State Contract (PSC)
Every ACME-governed project must expose a verifiable Project State Contract containing exactly seven orthogonal dimensions:

1. **Header & Provenance:** Project canonical ID, current normative anchor version, Git Merkle commit SHA, and state timestamp.
2. **Lifecycle Coordinate:** Active AUP phase (`INCEPTION`, `ELABORATION`, `CONSTRUCTION`, `TRANSITION`) and AOP stage (`READY`, `DIRECTIVE`, `MARCH`, `EXECUTE`, `RELEASE`, `RETREAT`, `EOD_SUMMARY`).
3. **Work Package Inventory:** Status matrix of all work packages classified strictly under the 7-tier evidence ladder:
   - `VERIFIED`: Backed by automated passing test assertions and Merkle commit SHA.
   - `IMPLEMENTED`: Code written, pending automated test execution or verification gate.
   - `PARTIAL`: Active construction underway; specific incomplete modules identified.
   - `SPECIFIED_ONLY`: Formal specification written and approved; zero code compiled.
   - `PLANNED`: Itemized in teleological roadmap; specification not yet drafted.
   - `BLOCKED`: Work halted due to an explicit unfulfilled prerequisite or error condition.
   - `UNKNOWN`: State unverifiable; requires immediate human or diagnostic inquiry.
4. **Verification Ledger:** Last executed test suite, pass/fail counts, referee exit code, and environment hash.
5. **Blocker & Friction Registry:** Active blockers, error traces, and architectural tensions serialized as formalized `State Delta` objects.
6. **Pending Human Decisions:** Explicit queue of choices awaiting Biological Root of Trust ratification (Question, Context, Evaluated Options, Recommended Choice).
7. **Next Authorized Action:** Single, unambiguous, bounded directive for the next execution sprint, complete with Permitted Degrees of Freedom ($\text{DoF}$).

---

## 6. DETERMINISTIC STATE RECONCILIATION & FRESHNESS RULES

### 6.1. State Staleness Invalidation (DoF = 0)
A state ledger is considered **stale and untrusted** if:
1. The recorded `git_merkle_sha` does not match `git rev-parse HEAD`.
2. The working directory contains uncommitted changes not recorded in the ledger's delta field.
3. The normative anchor declared in `.acme` differs from the ledger's declared anchor.

When staleness is detected, an incoming agent must execute **State Reconciliation**:
- Advance directly to **MARCH** phase: run `verify.py` and test discovery.
- Update the verification ledger with empirical facts.
- Re-anchor the state ledger to current HEAD before accepting new directives.

---

## 7. PROVENANCE, PRIVACY & SECURITY BOUNDARIES

1. **Scrubbing & Dewdrop Boundary:** State ledgers must never contain:
   - Internal credentials, API tokens, private SSH keys, or access secrets (`REJECT_SECRET_LEAK`).
   - Absolute local filesystem paths (`C:\`, `G:\`, `/home/`) violating domain decontamination (RFC-014).
   - Unredacted corporate or personal PII.
2. **Cryptographic Non-Repudiation:** State updates committed at RETREAT must be sealed within the git tree Merkle history.

---

## 8. PRE-MORTEM FAILURE MODES & VIA NEGATIVA (LEX: DoF = 0)

*Violations halt pipeline verification immediately (`REJECT_STATE_VIOLATION`). Top 3 failure modes strictly prohibited:*

1. **FAILURE MODE 1 (Conversational Handoff Drift):** Relying on natural-language chat logs, prompt-based memory summaries, or verbal commitments between agents as evidence of project completion -> `[PROHIBITED]` Conversational memory has zero evidentiary standing. Only machine-verifiable state contracts are admitted (`INV-EVIDENCE-ONLY-01`).
2. **FAILURE MODE 2 (Unanchored Implementation Claim):** Tagging a feature or spec as `VERIFIED` without a passing test log or automated referee receipt -> `[PROHIBITED]` Status claims without empirical test anchors are downgraded to `PARTIAL` or `UNKNOWN` (`INV-GROUNDED-STATUS-02`).
3. **FAILURE MODE 3 (Orphaned Blocker Evaporation):** Terminating an agent session while encountering an execution deadlock without serializing the blocker into the state ledger, forcing subsequent agents to rediscovering the failure -> `[PROHIBITED]` Unhandled blockages must be written to the friction registry before session exit (`INV-PERSISTENT-DELTA-03`).

---

## 9. PROPOSED DUAL SPECIFICATION (LEX VS. NORM)

### A. Proposed Lex (Inviolable Hard Invariants, DoF = 0)
* **INV-STATE-CONTINUITY-01 (Machine-Readable State Contract):** Every ACME-governed repository must maintain a canonical, machine-readable project state contract located at a deterministic root coordinate.
* **INV-EVIDENCE-LADDER-02 (Strict Status Taxonomy):** Status designations must strictly adhere to the 7-tier evidence taxonomy (`VERIFIED`, `IMPLEMENTED`, `PARTIAL`, `SPECIFIED_ONLY`, `PLANNED`, `BLOCKED`, `UNKNOWN`). Conversational assertions are inadmissible.
* **INV-ATOMIC-RETREAT-UPDATE-03 (Retreat Cadence Sealing):** Updating the state contract is mandatory during the RETREAT phase (SYS-127 Phase 6). Bypassing state ledger update during retreat raises `REJECT_DIRTY_RETREAT`.
* **INV-STALENESS-GATE-04 (HEAD Mismatch Circuit Breaker):** An incoming agent detecting a mismatch between the state contract's commit SHA and `git rev-parse HEAD` must halt active construction and trigger empirical reconciliation before executing new directives.

### B. Proposed Norms (Adaptive Guidance & Heuristics, DoF >= 1)
* **NORM 1 (Dual-Fidelity Storage):** High-traffic autonomous workspaces should maintain `.acme/state.json` as the machine-verifiable authority, accompanied by an auto-generated, human-readable summary in `README.md` or `STATE.md`.
* **NORM 2 (Token Budget Ceiling):** The state contract must be strictly optimized for minimal context overhead: the entire state representation should consume $\le 1,500$ tokens to preserve LLM context budget for active construction.
* **NORM 3 (Pending Decision Protocol):** Biological decision requests in the pending queue should present a maximum of 3 distinct, mutually exclusive options, with the recommended option explicitly indicated (`(Recommended)`).

---

## 10. MEASURABLE ACCEPTANCE CRITERIA & DEFINITION OF DONE (DoD)

- [ ] RFC authored in strict compliance with ACME `RFC_TEMPLATE.md` in UTF-8 No-BOM.
- [ ] Confirms architectural gap across all 10 project dimensions without doctrine duplication.
- [ ] Formulates the 7-Element Project State Contract and 7-Tier Evidence Ladder.
- [ ] Incorporates top 3 Pre-Mortem Anti-Pattern Gates with $\text{DoF}=0$ error handling.
- [ ] Fully decontaminated of absolute host paths, API secrets, and PII (RFC-014).
- [ ] Dispatched to upstream ACME intake queue (`acme/rfcs`).
- [ ] Cryptographic SHA-256 dispatch receipt recorded in local PMO telemetry.

---

## 11. UPSTREAM DISPATCH & HUMAN DECISION ESCALATION

* **Submission Target:** `acme/rfcs/RFC_044_CROSS_AGENT_STATE_CONTINUITY.md`
* **Human Root of Trust Decision Required:**
  1. Authorize upstream intake review of RFC-044 for candidate release in ACME v2.29.0.
  2. Select preferred normative representation format: Option B (`.acme/state.json`) vs Option D (Dual-Fidelity Hybrid).
* **Next Permitted Action:** Dispatch RFC-044 via `python cli.py dispatch rfcs/RFC_044_CROSS_AGENT_STATE_CONTINUITY.md`. Zero local implementation work until human ratification.
