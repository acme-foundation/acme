# RFC REQUEST: PORTABLE SPECIFICATION & HYBRID EXECUTION CONTRACT (RFC-046)
> **Reporting Client / Node:** ACME Architect  
> **Status:** CANDIDATE_REQUEST  
> **Target Faculty:** faculty-systems (SYS-129 / Portable Execution & Capability Matrix)  
> **Target Release:** ACME v2.29.0  
> **Constitutional Anchor:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Article 2 (Dynamic Conatus), Article 3 (Habitable Zone & Ceiling), Section II, Article 4 (Dewdrop Boundary Invariant), Article 5 (Observer Core), Article 7 (Downstream Non-Pollution & Single Manifest), Article 8 (Dual Normative Stratification), Article 11 (INV-ARCHETYPE-INHERITANCE), Article 12 (INV-STANDALONE-INSTANCE), Article 14 (INV-SPEC-INLINE), and Section III (Biological Primacy)

---

## 1. OBSERVED FRICTION & STRATEGIC INTENT

- **Context:** Classical software development and contemporary AI agent frameworks tightly couple the *definition of work* (specifications, requirements) to the *execution environment* (proprietary cloud backends, specific LLM vendor APIs, or monolithic local runtimes). This creates three severe architectural failure modes:
  1. *Vendor Lock-In & Cloud Hostage:* Users cannot formulate engineering specifications without binding themselves to a proprietary SaaS or specific cloud compute provider.
  2. *Model Fragility:* Prompt engineering is frequently conflated with system requirements. When an LLM model is deprecated, updated, or replaced, system behavior breaks unpredictably because specifications were written as model-specific prompts rather than invariant engineering contracts.
  3. *Data Sovereignty & Bandwidth Exhaustion:* In data-intensive domains (such as 4K/8K action video, healthcare, or sensitive telemetry), blindly pushing hundreds of gigabytes of raw data to centralized cloud hosts violates local-first privacy, causes astronomical bandwidth costs, and breaches thermodynamic efficiency (Principle of Least Action).

- **Teleological Objective:** ACME must evolve into a **local-first, model-agnostic, provider-independent, specification-driven architecture**.
  - **The primary product is the Specification itself.** A fully compiled ACME Living Specification is a complete, self-contained, portable engineering contract.
  - **Execution is strictly decoupled and optional.** A portable specification can be produced locally, exported as a portable bundle, and executed either:
    - Entirely offline on the user's local machine (CPU/GPU/NPU);
    - Via Bring-Your-Own-Compute (BYOC) using the user's chosen endpoints, external providers, or rented hardware;
    - Via ACME-brokered managed compute on rented infrastructure with explicit budget caps and human consent gates;
    - Or handed off to a third party or completely different execution engine.
  - In all scenarios, **independent verification** determines success against the contract, never trust in the executor or model.

---

## 2. THE PORTABLE SPECIFICATION CONTRACT SCHEMA

A specification is an **executable contract, not executable code**. It defines *What* must be achieved, *Under What Constraints*, and *How Verification is Proven*.

### 2.1. The 14 Required Contract Capabilities
Every portable ACME specification package (`spec-package.json` or content-addressed bundle) must provide fourteen standardized structural facets conforming to JSON Schema Draft 2020-12:

```json
{
  "$schema": "https://acme-standard.org/schemas/v1/portable-spec.json",
  "contract_version": "1.0.0",
  "identity": {
    "spec_id": "SPEC-002",
    "title": "Cadence Headless Video Pipeline",
    "canonical_component_id": "cid:comp-timeline-01",
    "component_fqn": "PremierStudio.VideoProduction.TimelineCompiler",
    "version": "0.1.0"
  },
  "teleology": {
    "intent": "Compile multi-track video timeline without visual GUI dependency using I-frame stream-copy",
    "problem_reference": "domain/video_production/problem_statement.md#L45-L80",
    "rationale": "Eliminates render UI overhead and prevents variable frame rate desynchronization"
  },
  "schema": {
    "input_schema": "schemas/timeline_input.schema.json",
    "output_schema": "schemas/timeline_spec.schema.json"
  },
  "io": {
    "inputs": [
      {
        "id": "triage_report",
        "type": "application/json",
        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "required": true
      }
    ],
    "outputs": [
      {
        "id": "timeline_spec",
        "type": "application/json",
        "path": "artifacts/TIMELINE_SPEC.json"
      }
    ]
  },
  "contracts": {
    "preconditions": [
      "ASSERT(triage_report.total_scenes >= 1)",
      "ASSERT(triage_report.cfr_verified == true)"
    ],
    "postconditions": [
      "ASSERT(output.timeline_duration_seconds <= 120.0)",
      "ASSERT(output.stream_copy_lossless == true)"
    ]
  },
  "execution_graph": {
    "dependencies": ["SPEC-005:Ladder2Proxy", "SPEC-003:StyleDNA"],
    "concurrency_mode": "deterministic_sequential"
  },
  "resource_requirements": {
    "min_ram_mb": 2048,
    "recommended_ram_mb": 4096,
    "cpu_cores": 2,
    "accelerator": "none_required",
    "accelerator_optional": ["cuda", "metal", "vulkan", "npu"],
    "disk_space_mb": 500
  },
  "data_locality_and_privacy": {
    "classification": "LOCAL_CONFIDENTIAL",
    "outbound_network_allowed": false,
    "data_residency": "ORIGIN_LOCAL_ONLY",
    "egress_requires_consent": true
  },
  "permissions_and_side_effects": {
    "filesystem_write_roots": ["artifacts/"],
    "spawn_subprocess": ["ffmpeg"],
    "network_egress": []
  },
  "acceptance_and_evidence": {
    "test_command": "python -m unittest tests/test_compiler.py",
    "expected_exit_code": 0,
    "referee_gate": "verify.py",
    "required_evidence_artifacts": ["artifacts/TIMELINE_SPEC.json"]
  },
  "provenance": {
    "git_commit_sha": "b2de7aae104642fb2f2e53744658097bdf7f191b",
    "contract_digest_sha256": "4a5b6c...",
    "acme_normative_anchor": "v2.28.0"
  },
  "failure_and_resumability": {
    "retry_policy": "exponential_backoff_max_3",
    "checkpoint_interval_seconds": 10,
    "idempotent": true,
    "circuit_breaker": "REJECT_ON_CORRUPTED_KEYFRAME"
  },
  "result_format": {
    "receipt_schema": "schemas/execution_receipt.schema.json",
    "telemetry_format": "json_lines"
  },
  "cost_and_resource_estimates": {
    "estimated_execution_seconds": 8.5,
    "nominal_cost_usd": 0.00,
    "max_cost_ceiling_usd": 0.00,
    "slippage_buffer_percent": 15,
    "hard_freeze_threshold_percent": 25
  }
}
```

---

## 3. THE THREE COMMERCIAL & TECHNICAL OPERATING MODES

All three execution modes consume and produce the **identical canonical specification contract**:

```
                              ┌───────────────────────────────────┐
                              │ CANONICAL ACME LIVING SPEC PACKAGE│
                              │ (Contract, Invariants, Acceptance)│
                              └─────────────────┬─────────────────┘
                                                │
                 ┌──────────────────────────────┼──────────────────────────────┐
                 ▼                              ▼                              ▼
      ┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
      │ MODE A: SPEC ONLY    │      │ MODE B: BYOC         │      │ MODE C: MANAGED      │
      ├──────────────────────┤      ├──────────────────────┤      ├──────────────────────┤
      │ • Zero Compute Dep.  │      │ • User Local CPU/GPU │      │ • ACME Brokers Spot  │
      │ • Exportable Bundle  │      │ • User API Keys      │      │ • Zero Owned Servers │
      │ • Handed to 3rd Party│      │ • Self-Hosted Models │      │ • Strict Budget Cap  │
      │ • Pure Contract Value│      │ • Zero Cloud Leakage │      │ • Consent Gate       │
      └──────────┬───────────┘      └──────────┬───────────┘      └──────────┬───────────┘
                 │                              │                              │
                 └──────────────────────────────┼──────────────────────────────┘
                                                ▼
                              ┌───────────────────────────────────┐
                              │ INDEPENDENT CONFORMANCE VERIFIER  │
                              │ verify.py / Deterministic Referee │
                              └───────────────────────────────────┘
```

### 3.1. Mode A: Specification Only
- **Commercial & Operational Model:** ACME acts purely as the specification and architectural compiler. The user purchases or generates the specification package without using any ACME execution service.
- **Portability:** The user can export the specification package (JSON + Markdown + Schemas) and hand it to an independent software team, a bespoke execution script, or a third-party workflow runner (e.g. Apache Airflow, Temporal, local shell script, DaVinci Resolve script).
- **Verification:** Any compliant executor that delivers the required artifacts and passes the acceptance criteria satisfies the contract.

### 3.2. Mode B: Bring Your Own Compute (BYOC)
- **Commercial & Operational Model:** The user provides their own compute resources: local workstation hardware (CPU/GPU/NPU), local AI runtimes (Ollama, vLLM, llama.cpp), or their own external cloud credentials (AWS, GCP, RunPod, Modal, OpenAI/Anthropic API keys).
- **Orchestration:** The ACME local runner or desktop harness orchestrates execution directly against the user's designated compute targets.
- **Infrastructure Footprint:** ACME maintains zero servers, zero GPUs, and zero data storage for the user. Privacy and data locality remain 100% under user control.

### 3.3. Mode C: Managed Execution
- **Commercial & Operational Model:** The user elects not to manage local or cloud infrastructure. ACME brokers ephemeral, on-demand external compute from spot/serverless providers (e.g. decentralized GPU grids, Modal, RunPod, AWS Spot).
- **Asset-Light Invariant:** ACME owns zero proprietary GPU farms or servers. It operates strictly as an intelligent, stateless broker and escrow.
- **Cost Ceiling & Invariant Gate:**
  - Upfront guaranteed cost quote with dynamic TTL (`INV-DYNAMIC-QUOTE-TTL`).
  - Slippage buffer capped at $\le 15\%$; execution freezes automatically if compute exceeds $25\%$ over budget (`INV-ZERO-PREMATURE-BILLING`).
  - Mandatory human authorization required before any billable job initiates.

---

## 4. LOCAL-FIRST HYBRID RUNTIME ARCHITECTURE

### 4.1. Core Application Architecture
The ACME application architecture is structured as a **Headless Core Engine** decoupled from user-facing presentations:
1. **Core Headless Engine (Python stdlib / Rust Core):** Implements specification compilation, invariant validation, dependency graph resolution, and local file I/O.
2. **Thin Presentation Clients:**
   - **Browser / Offline PWA:** Web standards, WebAssembly (Wasm), WebGPU, Origin Private File System (OPFS). Useful for contract authoring, visualization, and client-side review.
     - *Permission Boundary:* PWA sandboxes cannot spawn native OS processes (`ffmpeg`) or read arbitrary host filesystem paths without explicit user file picker prompts.
   - **Desktop Application (Tauri vs. Electron Evaluation):**
     - *Tauri:* Preferred for Principle of Least Action (PLA). Uses OS-native Webview + lightweight Rust core ($\approx 15\text{ MB}$ binary, $\le 40\text{ MB}$ RAM), with direct native access to files and subprocesses.
     - *Electron:* Bundles Chromium + Node.js ($\approx 150\text{ MB}$ binary, $\ge 180\text{ MB}$ RAM). Deprecated in favor of Tauri due to cognitive and memory entropy.
   - **Local Headless Daemon / CLI:** For CI/CD, headless terminals, and unattended background workers.

### 4.2. Capability-Based Execution Planning
Before any task executes, the engine performs **Capability Discovery**:
```
[Task Requirements] ───> [Workload Analyzer] <─── [Local Hardware Probe (CPU, GPU, VRAM, RAM, Disk)]
                                   │
                                   ▼
                   Can task execute 100% locally?
                   ├───────────── Yes ────────────> Execute Locally (Zero Data Transfer)
                   │
                   └────────────── No ────────────> Propose Offload Plan:
                                                    • Exactly which bytes must transfer
                                                    • Estimated network latency & cost
                                                    • Prompt human: [Authorize / Cancel / Lower Res]
```
- **Rule of Least Egress:** Raw bulk data (e.g. 300 GB video) never moves across the network. Only derived low-bandwidth representations (Ladder-1 proxies, JSON specs, telemetry vectors) are candidates for remote execution, and only upon explicit user consent.

---

## 5. MODEL AGNOSTICISM & CAPABILITY NEGOTIATION

1. **Vendor Neutrality:** Specifications are authored in standardized declarative schemas and pure NLP domain descriptions. No specification may reference vendor-specific parameters (`temperature`, `top_p`, `model: gpt-4o`, `anthropic-version`).
2. **Model Adapters:** Adapters translate ACME specification tasks into vendor-specific prompt templates or tool-calling schemas at execution time.
3. **Deterministic Falsification:** Because LLM generation is inherently non-deterministic, ACME forbids evaluating correctness via an LLM judge. Correctness is evaluated exclusively by:
   - Schema validation of produced JSON artifacts;
   - Execution of deterministic unit test assertions (`tests/`);
   - Cryptographic hash checks and exit codes;
   - Anayasal hakem kapısı (`verify.py`).

---

## 6. PREMIER STUDIO SCENARIO VALIDATION

| Evaluation Vector | Local Execution (Mode B) | Managed Hybrid Execution (Mode C) | Specification Only Export (Mode A) |
| :--- | :--- | :--- | :--- |
| **Data Ingestion** | 300 GB remains 100% on local NVMe. | 300 GB remains local. Ladder-1/2 proxies generated locally. | 300 GB remains local. |
| **Data Transfer** | **0.00 MB** external egress. | Only `TIMELINE_SPEC.json` (< 100 KB) and selected clip slices (< 3 GB) uploaded. | **0.00 MB** external egress. |
| **Compute Cost** | **$0.00** (Uses creator's existing GPU/CPU). | Billed strictly for ~90 seconds of spot GPU render (~$0.08). | **$0.00** (Zero runtime charge). |
| **Privacy / IP** | Absolute data sovereignty. | Zero raw footage leaves machine unencrypted; slices deleted post-render. | Absolute data sovereignty. |
| **Executor Portability** | ACME local runner (`cli.py`). | Brokered cloud container. | Third-party NLE (DaVinci Resolve / Premiere script). |
| **Verification Gate** | `verify.py` passes 8/8 kapı locally. | Cryptographic receipt verified against output hash. | Independent validator verifies resulting MP4 against spec. |

---

## 7. RESOLUTION OF RFC-044 CONFLICT & MANIFEST INVARIANTS

### 7.1. The Conflict Analysis
In `RFC-044`, the proposed path `.acme/state.json` created a fatal structural collision with `INV-SINGLE-MANIFEST` (`RFC-033`), which mandates that `.acme` is an atomic file:
- On POSIX and Windows filesystems, a directory named `.acme` cannot coexist with a file named `.acme`.
- Mutating `.acme` into a directory breaks all existing downstream referee gates (`open(".acme")` fails).

### 7.2. Canonical Resolution ($\text{DoF} = 0$)
This RFC ratifies the canonical state file convention:
1. **The Manifest Remains an Atomic File:** Workspace configuration remains strictly in the single root file `.acme`.
2. **State Storage Options:**
   - *Option 1 (Sibling Suffix - Recommended):* Runtime volatile execution state resides in a sibling file: `.acme.state.json`.
   - *Option 2 (Authorized State Directory):* State resides in an authorized root directory: `state/state.json`.
   - *Option 3 (Specs State Pairing):* As currently practiced in living specifications, state is paired with specs (`specs/SPEC_xxx_state.json`).
- Under no circumstance shall the root `.acme` manifest be converted into a directory.

---

## 8. PROPOSED DUAL SPECIFICATION (LEX VS. NORM)

### SECTION A: THE LEX (INVIOLABLE HARD INVARIANTS, DoF = 0)
*Violations halt specification export or execution immediately (`REJECT`).*

1. **INV-CONTRACT-PORTABILITY-01 (Provider-Independent Contract):**  
   Every living specification must compile to a self-contained, machine-verifiable contract package that contains zero proprietary execution locks, zero hardcoded vendor API endpoints, and zero mandatory cloud services.

2. **INV-DATA-SOVEREIGNTY-02 (Default-Local & Consent Gate):**  
   All raw project assets reside locally by default (`LOCAL_ONLY`). Outbound data transfer requires explicit biological authorization detailing byte volume, target destination, and cryptographic content hash (`REJECT_UNAUTHORIZED_EGRESS`).

3. **INV-INDEPENDENT-VERIFICATION-03 (Executor-Agnostic Audit):**  
   Verification of contract completion must be executable by any conforming ACME referee without access to the executor's internal memory, weights, or proprietary logs. Verification relies exclusively on declared inputs, outputs, exit codes, and test assertions.

4. **INV-BUDGET-HARD-FREEZE-04 (Zero Premature Billing & Hard Cap):**  
   Managed execution must enforce a hard budget ceiling ($\le 1.25\times$ nominal quote). If compute or financial expenditure reaches the ceiling, execution freezes immediately; silent overruns or retroactive billing are strictly prohibited (`REJECT_UNAUTHORIZED_OVERRUN`).

---

### SECTION B: THE NORMS (ADAPTIVE GUIDANCE & HEURISTICS, DoF >= 1)
*Advisory guidelines and best practices. Contextual adaptation permitted with explicit architectural rationale.*

1. **NORM 1 (Packaging Format):**  
   Portable specification packages should be distributed as content-addressed zip/tar archives containing the manifest, JSON schemas, living specification markdown, and input checksums.

2. **NORM 2 (Tauri Desktop Preference):**  
   For graphical client interfaces, development teams should prefer Tauri over Electron to minimize idle memory footprint ($\le 40\text{ MB}$ RSS target).

3. **NORM 3 (Capability Probing Interval):**  
   Hardware capability probes should cache results for 1 hour unless a hardware change or explicit reload is signaled.

---

## 9. DEFINITION OF DONE (DoD) FOR RATIFICATION

- [x] RFC-046 authored in canonical `rfcs/` with full 14-point contract schema.
- [x] Three execution modes (Spec-Only, BYOC, Managed) formally specified.
- [x] Local-first hybrid runtime and capability planning defined.
- [x] Model agnosticism and deterministic verification decoupled from LLM judges.
- [x] Premier Studio 300 GB local-first scenario validated.
- [x] RFC-044 single-file manifest conflict resolved via `.acme.state.json` sibling convention.
- [ ] Explicit review and approval received from ACME Architect (Human Root of Trust).

