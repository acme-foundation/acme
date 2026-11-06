# NORM-003: MEKANİK SOYUT SÖZDİZİM AĞACI KALKANI (AST SHIELD)
- **Kapsam:** Evrensel Çekirdek (Core)
- **DoF:** 0
- **Kural:**
  1. Ajanlar tarafından üretilen kodlar, harici bağımlılık yasağını ihlal edemez.
  2. İzin verilen standart kütüphaneler haricindeki harici 'import' bildirimleri AST statik analiziyle tespit edilip reddedilir (Exit 126).
  3. Çalıştırılabilir kod içine gizlenmiş 'eval', 'exec' veya yetkisiz OS kabuk çağrıları derleme hatasıdır.
