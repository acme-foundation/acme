# ACME: Lex Proceduralis Agentium
> **Autonomous Cognitive Multi-Agent Ecosystem | Canonical Jurisprudential Hub**  
> **Release:** v3.2.0 | **Authority:** Lex Superior (`DoF = 0`)  
> **Biological Root of Trust:** Serkan BAYHAN (Chief Architect)  
> *"Nulla Actio Sine Spec, Nullum Iudicium Sine Lege"*  
> *(Şartname olmadan icraat, kanun olmadan hüküm kurulamaz.)*

---

## 1. KÜNYE VE DİVAN
ACME, çoklu ajan sistemlerini kontrolsüz prompt tamamlama kargaşasından çıkarıp; usul hukuku kuralları, emsal içtihat kütükleri ve katı anayasal kısıtlarla (`DoF = 0`) işleten yüksek yargı ve denetim karargâhıdır.

---

## 2. DEPO TOPOLOJİSİ (ADLİYE SARAYI MİMARİSİ)
```text
acme/
├── README.md                      # Vitrin, operasyon rehberi ve sevkiyat protokolü
├── CONSTITUTION.md                # Kök Anayasa (Lex Superior: Madde 0 - 7)
├── verify.py                      # Mekanik CI/CD hakem turnikesi (7 Kapı)
│
├── templates/                     # Resmi Matbu Evrak Şablonları
│   ├── WORK_TEMPLATE.md           # Şantiye iş/muhakeme kütüğü kalıbı
│   ├── PRECEDENT_TEMPLATE.md      # Emsal karar ilam şablonu
│   └── NORM_TEMPLATE.md           # Pozitif kanun teklif şablonu
│
├── precedents/                    # İçtihat Bilgi Bankası (Emsal Kararlar / O(1) Cache)
│   ├── core/                      # COR_{hex3}_*.md (Sistemik emsaller)
│   ├── ingestion/                 # ING_{hex3}_*.md (Veri hattı hükümleri)
│   └── procedural/                # PRO_{hex3}_*.md (Usul hükümleri)
│
├── norms/                         # Pozitif Kanunlar Külliyatı (3 Harfli Hex Normlar)
│   ├── core/                      # COR_{hex3}_*.md (COR_001, COR_002, COR_003)
│   ├── domain/ingestion/          # ING_{hex3}_*.md (ING_001)
│   └── procedural/                # PRO_{hex3}_*.md (PRO_001, PRO_002)
│
└── .tmp/                          # [Git-Ignored] Canlı telemetri ve geçici lab alanı
```

---

## 3. DOWNSTREAM SEVKİYAT VE ENTEGRASYON PROTOKOLÜ (.norm)

Şantiye projeleri ACME'yi kök dizindeki `.norm` manifestosu ile bağlar ve RFC adaylarını üst depoya şu protokolle sevk eder:

```json
{
  "norm_version": "1.0",
  "project_name": "client-core",
  "extends": "https://github.com/acme-foundation/acme.git#v3.2.0",
  "active_norm_scopes": [
    "norms/core/*",
    "norms/domain/ingestion/*",
    "norms/procedural/*"
  ],
  "upstream_dispatch": {
    "remote": "origin",
    "branch_template": "rfcs/{project_name}/RFC_{hex3}_{slug}",
    "auto_dispatch": true
  }
}
```

### Şantiyeden Karargâha İcra Döngüsü

1. **Şantiye İcrası:** Proje içinde `works/WORK_{hex3}_{slug}.md` kütüğü tutulur.
2. **Kural Sevkiyatı:** Sistemik sürtünmeler arındırılarak `rfcs/{project}/RFC_{hex3}_{slug}` dalı ile üst depoya açılır.
3. **Sınama Potası (The Crucible):** ACME Karargâhı `.tmp/lab_{hex3}/` ortamında kuralı hasımlı yüklerle test eder.
4. **Tescil:** Sınamayı geçen kurallar `precedents/` altına Emsal İlam veya `norms/` altına Kanun olarak mühürlenir.

---

## 4. İŞLETİM VE DOĞRULAMA KOMUTU

```bash
python verify.py --verify-all
```
