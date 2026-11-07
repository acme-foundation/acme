# NORM: COR_002_CONSTANT_MEMORY: CONSTANT MEMORY STREAMING AND LEAST ACTION PROTOCOL (CONSTANT MEMORY)
- **Scope:** Universal Core (Core / COR)
- **DoF:** 0
- **Rule:**
  1. Unbounded datasets must never be loaded into heap memory in a single read call (OOM Prevention).
  2. Memory utilization must remain strictly bounded ($O(1)$ space complexity) even as stream length $N \to \infty$.
  3. Peak memory usage for streaming operations must not exceed the specified ceiling (e.g., 15.0 MB) verified by mechanical memory profiling.
