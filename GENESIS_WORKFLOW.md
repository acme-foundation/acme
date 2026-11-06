# E-AUP HOLOGRAPHIC EXECUTION WORKFLOW
Status: Canonical | Governance: ACME CONSTITUTION v3.2.0

## 1. YATAY DÖNÜŞÜM HATTI (ONTOLOJİK PİPELİNE)
[01. Hikaye / Neden] <GK> [02. Gereksinim / 5N1K] <GK> [03. Çözüm / Mimari] <GK> [04. Sözleşme / SPEC.md] <GK> [05. Ürün / Kod]

- Her arayüz (<GK>) çift yönlü bağışıklık membranıdır.
- Dikey Geri Yayılım: 05/Müşteri aşamasında kök bir çelişki belirdiğinde yerel yama yapılmaz; ret dalgası geriye yayılarak hatalı şartnameyi budar (05 -> 04 -> 03 -> 02 -> 01) ve yeni duruşma açar.

## 2. DİKEY AUP FAZLARI İLE KİLİTLENME
- Inception Fazı: Hikaye ve Gereksinim odağıyla Problem Şartnamesini kilitler (Kod: Yok).
- Elaboration Fazı: Çözüm ve Sözleşme odağıyla Mimari Sözleşmeyi ve mikro-spike sondajını kilitler.
- Construction Fazı: Sözleşmeden doğrudan DoF=0 kod ve mekanik test üretir.
- Transition Fazı: Ürünü ilk Hikaye ile çarpıştırır, sapma sıfırsa teslim eder ve emsal içtihatları kaydeder.

## 3. RÜMİNASYON VE KİLİTLENME FRENİ
- Bir arayüzdeki çekişme en fazla 3 tur sürebilir (MAX_LOCAL_CYCLES = 3).
- 3. turda uzlaşılamazsa sistem yürütmeyi dondurur (fail-closed) ve karar Biyolojik Mimara eskale edilir.
