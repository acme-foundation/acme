# NORM-COR-001: KÜTLE KORUNUMU VE SIFIR SIZINTI DEĞİŞMEZİ (MASS BALANCE)
- **Kapsam:** Evrensel Çekirdek (Core / COR)
- **DoF:** 0
- **Kural:**
  1. Girdi olarak alınan veri/görev kümesi ile işlem sonrası oluşan çıktılar arasında mutlak kütle dengesi aranır:
     Girdi_Adet = Gecerli_Adet + Karantina_Adet
  2. Hiçbir kayıt, veri parçası veya istisna 'except: pass' ile sessizce yutulamaz (Silent Drop Yasaktır).
  3. Karantinaya atılan her eleman için mutlak konum ve hata sınıfı delillendirilmek zorundadır.
