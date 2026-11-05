# ACME FORM-01: ON-SITE DISCOVERY & ATTENDANCE PROTOCOL
**Document Reference:** `DISC-{YYYYMMDD}-{CLIENT_CODE}`  
**Standard:** ISO/IEC/IEEE 29148 Requirements Engineering | **Classification:** Preliminary / Non-Binding

---

## 1. ENGAGEMENT METADATA

| Parameter | Specification Detail |
| :--- | :--- |
| **Client Legal Entity** | `[Client Corporate Name / Organization]` |
| **Engagement Location** | `[On-Site Facility / Remote Bridge URI]` |
| **Discovery Date** | `YYYY-MM-DD` |
| **ACME Lead Auditor** | `[Principal Consultant Name]` |
| **Primary Incident / Trigger** | `[Defect Ticket / Modernization Directive / Architectural Audit]` |

---

## 2. ATTENDANCE ROSTER (PARTICIPANT REGISTRY)

| Full Name | Organization & Department | Role / Official Title | Contact URI | Signature |
| :--- | :--- | :--- | :--- | :--- |
| 1. | Client Subsystem Owner | Lead Systems Architect | client.lead@domain.com | _________________ |
| 2. | Client Operations | Site Reliability Director | client.ops@domain.com | _________________ |
| 3. | ACME Advisory | Principal Systems Architect | lead@acme.foundation | _________________ |
| 4. | ACME Advisory | Autonomous Oversight Ref | node3@acme.foundation | _________________ |

---

## 3. OBSERVED SYMPTOMS VS. ROOT PATHOLOGY MATRIX

| ID | Surface Symptom (Reported Anomaly) | Metric Signature ($P_{99}$ / Error / Drift) | Suspected Root Pathology (Structural Hypothesis) |
| :--- | :--- | :--- | :--- |
| **S-01** | High latency under peak payload | Latency spikes $> 1400\text{ms}$ at 10k req/s | Unbounded database connection pooling / sync locks |
| **S-02** | Intermittent transaction drop | HTTP 504 Gateway Timeout ($2.1\%$ frequency) | Downstream third-party auth service timeout |
| **S-03** | Configuration drift across environments | Divergent secret formats in staging vs. prod | Lack of centralized normative schema manifest |

---

## 4. PRELIMINARY BOUNDARY & BLAST RADIUS DELINEATION

- **In-Scope Subsystems:** `[services/checkout, services/billing-gateway]`
- **Strictly Excluded Subsystems (Via Negativa):** `[legacy/core-erp, internal/auth-vault]`
- **Observed Constraints:** `[Must operate on existing Linux runtime; Zero schema breaks permitted]`

---

## 5. CLIENT CONFIRMATION & NON-BINDING ACKNOWLEDGMENT

> **LEGAL NOTICE:**  
> This protocol records preliminary on-site field discovery observations, architectural friction, and telemetric findings. **It does NOT constitute a binding statement of work, financial authorization, or guarantee of remediation.** Formal execution requires an executed `FORM_02_SPEC_SIGN_OFF.md`.

### Bilateral Acknowledgment Signatures

**Client Representative:**  
Name: ___________________________  
Title: ___________________________  
Signature: ______________________  
Date: ___________________________  

**ACME Lead Consultant:**  
Name: ___________________________  
Title: ___________________________  
Signature: ______________________  
Date: ___________________________  
