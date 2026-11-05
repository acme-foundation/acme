# ACME Consultancy Hub: Operations & Onboarding Manual
## Standard: Autonomous Consultancy Workspace Governance (DoF = 0)

---

## 1. TELEOLOGY (CORE PURPOSE)
This consultancy headquarters provides a deterministic, zero-drift engagement framework that converts ambiguous client business problems into mathematically bounded, verified software deliverables without cognitive leakage or scope creep.

---

## 2. ROLES & AUTHORITIES

```text
┌──────────────────────────────────────────────┐       ┌──────────────────────────────────────────────┐
│ BIOLOGICAL ARCHITECT / MANAGING PARTNER      │       │ DOWNSTREAM AUTONOMOUS AGENT (POLYMATH WORKER)│
│ - Ultimate sovereign sign-off authority      │◄─────►│ - Executes scoped tasks within island sandbox │
│ - Holds legal, commercial, and ethical root  │       │ - Zero speculative mutations outside mandate │
│ - Signs formal Work Orders & Acceptance docs │       │ - Strictly bounded by DoF = 0 specifications │
└──────────────────────────────────────────────┘       └──────────────────────────────────────────────┘
```

---

## 3. INPUT / OUTPUT CONTRACT

### A. Accepted Ingestion Inputs
1. Client incident logs, telemetry dumps, and architecture diagrams.
2. Discovery interview transcripts and preliminary call records (`forms/FORM_01_ON_SITE_DISCOVERY.md`).
3. Legacy brownfield codebases and configuration manifests.

### B. Ratified Deliverables
1. Ground-truth problem specifications (`artifacts/problem_spec.md`).
2. Bilaterally signed work orders (`forms/FORM_02_SPEC_SIGN_OFF.md`).
3. Surgical code diffs bounded by $\le 500$ tokens per atomic unit with zero unanchored refactoring.
4. Formal delivery and acceptance certificates (`forms/FORM_03_ACCEPTANCE_DELIVERY.md`).

---

## 4. VIA NEGATIVA (EXPLICIT NEGATIVE SCOPE)
To conserve energy and prevent systemic liability, this workspace **STRICTLY DOES NOT**:
- **Cross-Contaminate Client Contexts:** Never mingle data, code, or telemetry between distinct client offices under `offices/{client_id}/`.
- **Execute Without Signed Contracts:** Never write implementation code or modify client infrastructure without a ratified `FORM_02_SPEC_SIGN_OFF.md`.
- **Introduce Unjustified Dependencies:** Never install unvetted npm packages or external database servers when CDN leverage or standard library tools suffice (`INV-MIN-DEPENDENCY`).
- **Commit Client Secrets:** Never commit raw API credentials, private certificates, or personally identifiable information (`INV-DECONTAMINATION`).

---

## 5. AGENT ONBOARDING SEQUENCE (3-LINE LLM ORIENTATION)
When a new autonomous agent or model instance initializes inside this workspace, execute this immediate three-step sequence:

```text
1. Read `.acme` and verify `mode: consultancy_hub` is active.
2. Confirm target client sub-office under `offices/{client_id}/` (`INV-ISLAND-BOUNDARY`).
3. Inspect `forms/FORM_02_SPEC_SIGN_OFF.md` to ensure active work order exists before authoring code diffs.
```

### Onboarding Dialogue Trigger
Upon session start, the agent shall greet the operator with the canonical orientation response:
> *"ACME Consultancy Hub active. Field forms prepared under forms/. Client engagements isolated under offices/{client_id}/. Which client office are we opening or which specification are we sealing?"*

