# NORM-002: SABİT BELLEK AKIŞ VE EN AZ EYLEM PROTOKOLÜ (CONSTANT MEMORY)
- **Kapsam:** Evrensel Çekirdek (Core)
- **DoF:** 0
- **Kural:**
  1. Veri akışlarında tüm veri tek seferde belleğe yüklenemez (OOM Engeli).
  2. Heap bellek kullanımı veri büyüklüğü $N \to \infty$ olsa dahi $O(1)$ akış mimarisinde kalmalıdır.
  3. Görev için tanımlanan RAM tavanı (örneğin 15 MB) mekanik profilleme ile doğrulanmalıdır.
