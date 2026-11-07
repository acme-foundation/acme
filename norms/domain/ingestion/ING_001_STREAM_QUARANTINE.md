# NORM-ING-001: BYTE-PRECISE DUAL-QUARANTINE PROTOCOL (STREAM QUARANTINE)
- **Scope:** Ingestion and Data Influx Pipelines (Domain / Ingestion / ING)
- **Authority:** RFC-001 / Precedent-ING-001
- **DoF:** 0
- **Rule:**
  1. Corrupt, truncated, or unparseable stream records must be isolated immediately into `quarantine.jsonl`.
  2. Mandatory Audit Metadata Schema:
     - `byte_offset`: Exact byte offset from the start of the source stream.
     - `byte_length`: Byte length of the isolated corrupt slice.
     - `reason`: Classification of failure (e.g., DecodeError, ParseError, SchemaViolation).
     - `raw_preview`: Lossless raw preview of the quarantined payload.
