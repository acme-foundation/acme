# PRECEDENT: ING_001_STREAM_QUARANTINE_RULING
- **Daire / Etki Alanı:** Domain / Ingestion (ING)
- **Tescil Tarihi:** 2026-11-06
- **Menşe Vaka:** 100K Streaming Telemetry Breakdown
- **Bağlayıcılık:** Tüm Veri Akış Hatları İçin Bağlayıcı Emsal Hüküm

## 1. UYUŞMAZLIK ÖZETİ (CASE FACTS)
Yüksek hacimli ve bozuk segmentler içeren veri akışlarında bellek patlamaları (OOM) 
ve verinin sessizce yutulması ('except: pass') suretiyle kütle kaybı yaşandığı tespit edilmiştir.

## 2. HUKUKİ VE MİMARİ İLKE (RATIO DECIDENDI)
1. Kütle Korunumu: Giren kayıt adedi, geçerli ve karantinaya alınan kayıtların toplamına eşit olmak zorundadır.
2. Sabit Bellek: Akış büyüklüğü ne olursa olsun heap bellek tüketimi O(1) kalmalı, tepe bellek bütçesi (<= 15MB) aşılmamalıdır.
3. Adli Delil Kütüğü: Karantinaya alınan her satır için mutlak byte_offset, byte_length ve kök hata nedeni diske kazınmalıdır.

## 3. MEKANİK DELİL ÇAPASI
- Zirve RAM İspatı: 0.104 MB (<= 15.0 MB tavan)
- Kütle Korunumu İspatı: 84.940 (Temiz) + 15.060 (Karantina) = 100.000 (Girdi)
- AST Doğrulaması: Sıfır harici kütüphane bağımlılığı.
