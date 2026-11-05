# RFC REQUEST: FORMAL INTERMEDIATE REPRESENTATION (FIR) & STATE TRANSITION MATRIX (SPEC-048)
> **Reporting Client / Node:** acme-formal-compiler  
> **Status:** RATIFIED_SPEC  
> **Target Faculty:** faculty-systems  
> **Anchored Invariant:** INV-FORMAL-IR-GATE (DoF = 0)  

---

## 1. OBSERVED FRICTION (WHAT BROKE?)
- **Context:** Natural language specifications possess non-zero entropy and semantic ambiguity. When stochastic models interpret natural language contracts without a formal intermediate representation, they exploit semantic loopholes (specification gaming) and produce state transitions with hidden failure modes.
- **Root Tension:** Rice's Theorem dictates that non-trivial semantic properties of arbitrary programs cannot be decided statically from untyped natural language prose. Bounding agentic execution to $DoF = 0$ requires mathematical state transition closure prior to code dispatch.

---

## 2. AD-HOC WORKAROUND (HOW WAS WORK PRESERVED?)
- **Immediate Mitigation:** Relying on markdown bullet points, ad-hoc prompt engineering, and human-in-the-loop manual review.
- **Residual Risk:** High risk of cyclic deadlocks, unreachable states, unhandled edge cases, and catastrophic cascading failure during autonomous multi-agent handoffs.

---

## 3. PROPOSED HYPOTHESIS & DUAL SPECIFICATION
- **A. Proposed Lex (Hard Invariants, DoF = 0):**
  - **INV-FIR-01 (Formal Intermediate Representation Twin):** Every human or agentic specification must compile into a type-checked, mathematically grounded Formal Intermediate Representation (`.fir.json` or JSON-Schema) twin before dispatching to execution planes (`REJECT_UNVERIFIED_TRANSITION_MATRIX`).
  - **INV-FIR-02 (State Transition Matrix Completeness):** The FIR schema must explicitly formalize:
    1. `initial_state`: Deterministic baseline coordinate.
    2. `states`: Comprehensive set of discrete operational states.
    3. `action_transition_matrix`: Explicit mapping of `(current_state, event) -> next_state`.
    4. `pre_conditions` & `post_conditions`: Strict Boolean predicates ($DoF = 0$).
  - **INV-FIR-03 (Deadlock & Unreachable State Rejection):** Any FIR graph containing unreachable states, unhandled exceptions, or cyclic deadlocks fails mechanical compilation immediately (`REJECT_DEADLOCK_PRONE_IR`).
- **B. Proposed Norms (Adaptive Guidance, DoF >= 1):**
  - Standard FIR payloads should be co-located with specification artifacts as `<name>.fir.json`.
  - FIR schemas should provide machine-readable error tracebacks for downstream automated repair.

