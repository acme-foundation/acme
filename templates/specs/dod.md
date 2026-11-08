# DEFINITION OF DONE & ACCEPTANCE GATES

## 1. TIER-1 STRUCTURAL ASSERTIONS
- [ ] `Exit Code Invariant:` Every pipeline instruction must exit with code `0` (`exit_code == 0`).
- [ ] `Filesystem Invariant:` All expected output artifacts exist at target paths with non-zero byte size.
- [ ] `Dependency Invariant:` Zero untracked or external binary dependencies referenced.
- [ ] `Encoding Invariant:` Tracked specification and text files verified as UTF-8 No-BOM.

## 2. TIER-2 CRAFTSMANSHIP & QUALITY GATES
- [ ] `Aesthetic Integrity:` Zero black frames, visual stutter, or corrupted clipping in media assets.
- [ ] `Acoustic Integrity:` Absence of clipping, crackle, or harmonic distortion across all audio channels.
- [ ] `Complexity Cap:` Cyclomatic complexity delta within baseline bounds (no nested spaghetti branches).
- [ ] `Fluff Density:` Subjective adjective density <= 0.02 across all generated documentation.
- [ ] `Goodhart Shield:` Independent Arbiter sign-off confirmed before build release sealing.
