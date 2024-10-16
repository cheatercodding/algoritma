def para_cekme_uygulaması():  # Corrected typo
    # Kullanıcıdan çekmek istediği miktarı al
    cekilecek_miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
    bakiye = 7000
    # bakiyeyi kontrol et
    if cekilecek_miktar > bakiye:
        print("Yetersiz bakiye! Çekmek istediğiniz miktar mevcut bakiyenizden fazla.")
    
        # Bakiyeyi güncelle
        bakiye -= cekilecek_miktar
        print(f"İşlem başarılı! Yeni bakiyeniz: {bakiye:.2f} TL")


para_cekme_uygulaması()  # Corrected typo