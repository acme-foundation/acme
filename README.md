# ACME: Lex Proceduralis Agentium
> **Autonomous Cognitive Multi-Agent Ecosystem | Living Specification & Normative Hub**  
> **Release:** v3.2.0 | **Authority:** Lex Superior (`DoF = 0`)  
> **Biological Root of Trust:** Serkan BAYHAN (Chief Architect)  
> *"Nulla Actio Sine Spec, Nullum Iudicium Sine Lege"*  
> *(Şartname olmadan icraat, kanun olmadan hüküm kurulamaz.)*

---

## 1. KÜNYE VE AMACIN TANIMI
ACME, büyük dil modellerini (LLM) başıboş kod üreten istatistiksel tamamlama araçları olmaktan çıkarıp, usul hukuku kuralları ve katı anayasal kısıtlarla (`DoF = 0`) çalışan deterministik yargı ve icra aktörlerine dönüştüren bilişsel bir çoklu-ajan işletim mimarisidir.

---

## 2. DEPO TOPOLOJİSİ
```text
acme/
├── README.md                      # Vitrin, operasyonel kılavuz ve downstream entegrasyonu
├── CONSTITUTION.md                # Kök Anayasa (Lex Superior: Madde 0 - 7)
├── verify.py                      # Mekanik CI/CD turnikesi ve anayasal hakem
│
├── norms/                         # Kelsen Normlar Hiyerarşisi (Lex Specialis)
│   ├── core/                      # Evrensel sistem normları (Kütle dengesi, sabit bellek, AST)
│   ├── domain/                    # Alana özgü normlar (Ingestion, karantina, state machine)
│   └── procedural/                # Usul ve icra normları (Diyalektik konsensüs, rüminasyon freni)
│
├── worklogs/                      # Mühürlü karar ve içtihat kütüğü (WL_*.md)
└── .tmp/                          # [Git-Ignored] Canlı telemetri ve geçici karar taslakları
```

---

## 3. DOWNSTREAM PROJE ENTEGRASYONU (.norm)

İstemci projeler ACME'yi harici bir anayasal otorite olarak kök dizinlerindeki tekil `.norm` manifestosu üzerinden bağlar:

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
  "corporate_invariants": [
    "Zero binary dependencies: Compile locally from verified source",
    "Boolean DoD: Every module requires deterministic PASS/FAIL assertions"
  ]
}
```

---

## 4. TEMEL İŞLETİM VE DOĞRULAMA KOMUTLARI

### Mekanik Hakem Turnikesi (Turnstile Check)

Depodaki tüm anayasal değişmezleri, dosya formatlarını ve norm hiyerarşisini denetler:

```bash
python verify.py --verify-all
```

### Karar ve İçtihat Akışı

1. **Canlı Gözlem:** Ajanların anlık çekişmeleri `.tmp/decisions/` altında izlenir.
2. **Karar Mührü:** Çözüme kavuşan durumlar `worklogs/WL_TEMPLATE.md` formatında mühürlenir.
3. **Norm Terfisi:** Sistemik sürtünmeler soyutlanarak `norms/` kütüphanesine veya istemcinin `.norm` dosyasına eklenir.
