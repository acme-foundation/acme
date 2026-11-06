# NORM-PRO-002: HEYET İNCELEMESİ VE AMPİRİK SINAMA POTASI (THE CRUCIBLE PROTOCOL)
- **Kapsam:** Usul Hukuku (Procedural / PRO)
- **DoF:** 0
- **Kural:**
  1. Downstream projelerden 'rfcs/{project}/RFC_{hex3}_{slug}' dalıyla sevk edilen hiçbir kural doğrudan kabul edilemez.
  2. İntikal eden kural '.tmp/lab_{hex3}/' izole alanında 3 hasımlı teste sokulur:
     - Bozuk Yük Saldırısı (Adversarial Payload): OOM ve kilitlenme eşiği.
     - Kütle Dengesi Denetimi (Mass Balance): Sıfır kayıp bayt teyidi.
     - AST Bağımlılık Zırhı: Harici import ve yetkisiz OS çağrısı taraması.
  3. Lab testini geçemeyen kurallar gerekçeli bozma kararıyla (REMAND) şantiyeye iade edilir.
  4. Sınamayı geçen kurallar Yüksek Heyet (Mimar + Node-1) onayıyla 'precedents/' altına İlam veya 'norms/' altına Kanun olarak tescil edilir.
  5. Sınama bittiğinde geçici lab dizini tamamen yok edilir (Zero Residue / DoF=0).
