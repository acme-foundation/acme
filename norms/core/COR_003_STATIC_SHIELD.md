# NORM: COR_003_STATIC_SHIELD: MECHANICAL ABSTRACT SYNTAX TREE SHIELD (AST SHIELD)
- **Scope:** Universal Core (Core / COR)
- **DoF:** 0
- **Rule:**
  1. Code artifacts synthesized by autonomous agents must not violate the zero-unjustified external dependency invariant.
  2. External import declarations outside allowlisted standard libraries are detected via AST analysis and rejected with exit code 126.
  3. Obfuscated dynamic execution calls (`eval`, `exec`, or unmonitored OS subprocess invocations) constitute critical compile errors.
