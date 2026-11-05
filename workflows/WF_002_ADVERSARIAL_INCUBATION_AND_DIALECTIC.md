# WF-002: Pre-Execution Adversarial Incubation & Dialectic Workflow
## Scope: Epistemic Intake -> Writers' Room -> Preview Gate -> Upstream RFC (DoF = 0)

### State 0: Epistemic Intake & Telos Classification
- [ ] Determine System Telos: What is the irreducible reason for being (Telos) of the target system?
- [ ] Delineate Engagement Nature:
  - **Greenfield (Teleological Absence):** Complete absence of legacy software topology. Execution is immediately bounded by clean-slate 3-tier modular contracts, formal binary acceptance criteria, and zero-code specifications.
  - **Brownfield (Pathological Defect):** Active production baseline with structural friction. Prohibit direct mutation; perform static AST scan, extract implicit invariants, and bound blast radius.
- [ ] Invariant Check: Unanchored leaps from raw intent directly into code are strictly prohibited (`INV-ONTOLOGICAL-GROUNDING`). Proceed to State 1.

### State 1: The Writers' Room (Adversarial Dialectic Crucible)
- [ ] Formulate Twin Specifications:
  - `SPEC-A (The Constructor)`: Designs minimal architectural blueprint satisfying the Telos under the Principle of Least Action ($\delta S = 0$).
  - `SPEC-B (The Adversary / Critic)`: Formulates adversarial refutation report, probes for Rice undecidability, uncovers unmodeled failure modes, and flags subjective adjectives.
- [ ] Crucible Collision: Collide `SPEC-A` and `SPEC-B` in the Writers' Room.
- [ ] Bounded Convergence: Limit dialectic oscillation to $N_{\max} \le 3$ iterations.
- [ ] Invariant Gate: `INV-PRE-EXEC-DIALECTIC-01` (`REJECT_UNDIALECTICAL_EXECUTION`).
  - No autonomous agent may begin physical code generation without a ratified execution plan ($DoF = 0$) sealed through adversarial consensus.
  - Upon consensus: Proceed to State 2.

### State 2: Dry Scaffolding Preview Gate (Zero-Divergence Audit)
- [ ] Synthesize non-destructive scaffolding preview: layout slots, schema interfaces, and type contracts.
- [ ] Compute Semantic Divergence: Measure difference between scaffolding preview and ratified specification ($\Delta\text{MSE}$).
- [ ] Invariant Gate: `INV-PREVIEW-DELTA-02` (`REJECT_UNALIGNED_SCAFFOLDING`).
  - If $\Delta > 0$: Halt execution immediately, discard unaligned scaffolding, and return to State 1.
  - If $\Delta == 0$: Semantic divergence is zero; unlock implementation authorization and proceed to State 3.

### State 3: Bounded Materialization & Upstream RFC Feedback Sieve
- [ ] Polymath worker executes atomic construction units ($\le 500$ tokens per surgical diff).
- [ ] Continuous Boundary Sieve: If downstream execution encounters unforeseen constraints, missing specification invariants, or runtime boundary friction:
  - Prohibit local ad-hoc patches, defensive hack blocks, or mock overrides (`REJECT_LOCAL_PATCH_BYPASS`).
  - Invariant Gate: `INV-UPSTREAM-RFC-03`.
  - Derive root-cause Request for Comments (RFC) conforming to `templates/RFC_TEMPLATE.md`.
  - Backpropagate RFC upstream to the ACME Core Review Board for architectural incorporation.
- [ ] If construction completes without divergence: Proceed to State 4.

### State 4: Terminal Verification & Quiescent Handover
- [ ] Execute full mechanical gatekeeper audit: `python verify.py --verify-all`.
- [ ] Confirm 100% binary PASS across all verification turnstiles ($DoF = 0$).
- [ ] Purge ephemeral test ballast (`.tmp/`) and verify No-BOM UTF-8 standard.
- [ ] Transition execution plane to quiescent `STANDBY`.
