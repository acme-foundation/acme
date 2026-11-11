# NORM: PRO_004_UNANCHORED_INTERRUPT_PROTOCOL
Title: Unanchored Decision Circuit Breaker and Flag Escalation Protocol
Scope: Runtime Governance, Ingestion, and Dialectic Triage
Authority: CONSTITUTION.md (Article 20)
Status: RATIFIED_CANONICAL

## 1. DOCTRINE OF NORMATIVE ANCHORING
1. **Nulla Actio Sine Norma:** No computational mutation, filesystem write, or architectural state transition may execute without citation to a ratified invariant (`CONSTITUTION.md`, `PRO_*.md`, or root tenant `.norm`).
2. **Fail-Closed Execution:** When a task, instruction, or architectural proposal lacks an identifiable normative anchor, the execution engine MUST NOT guess or interpret ($DoF = 0$).

## 2. FLAG ELEVATION & CIRCUIT BREAKER (🚩 / 🙋♂️)
1. **Interrupt Trigger:** Detection of an unanchored directive raises the `UNANCHORED_DECISION_FLAG` and immediately suspends the pipeline.
2. **Telemetry Payload:**
   - Source Directive / Task Token
   - Missing Authority Domain
   - Halt State Hash
3. **Bifurcation Paths:**
   - **Path A (Rejection):** Directive is discarded as out-of-scope speculation.
   - **Path B (Normative Promotion):** Stakeholder formalizes the constraint as a new invariant within `.norm` or an RFC before execution resumes.
