# NORM-ING-001: BAYT-HASSAS İKİLİ KARANTİNA PROTOKOLÜ (STREAM QUARANTINE)
- **Kapsam:** Veri Giriş Hatları (Domain / Ingestion / ING)
- **Dayanak:** RFC-001 / Precedent-ING-001
- **DoF:** 0
- **Kural:**
  1. Akış sırasında bozuk, eksik veya çözümlenemeyen her satır 'quarantine.jsonl' dosyasına tecrit edilir.
  2. Asgari Denetim Metadata Şeması zorunludur:
     - `byte_offset`: Dosya başından itibaren mutlak bayt ofseti.
     - `byte_length`: Bozuk segmentin bayt uzunluğu.
     - `reason`: Bozulmanın teknik sınıfı (DecodeError, ParseError, SchemaViolation).
     - `raw_preview`: Bozuk kaydın ham metin/bayt önizlemesi.
