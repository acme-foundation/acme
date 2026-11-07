# NORM: COR_001_MASS_BALANCE: MASS CONSERVATION AND ZERO LEAKAGE INVARIANT (MASS BALANCE)
- **Scope:** Universal Core (Core / COR)
- **DoF:** 0
- **Rule:**
  1. Input records ingested by a stream processing unit must strictly balance against terminal output states:
     $\text{Input\_Count} = \text{Valid\_Count} + \text{Quarantine\_Count}$
  2. No record, segment, or error condition shall be silently swallowed (`except: pass` is strictly prohibited).
  3. Quarantined records must retain explicit byte offset coordinates and verified error classification.
