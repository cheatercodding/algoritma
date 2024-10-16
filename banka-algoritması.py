def para_cekme_uygulaması():  # Corrected typo
    # Kullanıcıdan mevcut bakiyesini al
    bakiye = float(input("Mevcut bakiyenizi giriniz: "))  # Corrected typo

    # Kullanıcıdan çekmek istediği miktarı al
    cekilecek_miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))

    # bakiyeyi kontrol et
    if cekilecek_miktar > bakiye:
        print("Yetersiz bakiye! Çekmek istediğiniz miktar mevcut bakiyenizden fazla.")
    else:
        # Bakiyeyi güncelle
        bakiye -= cekilecek_miktar
        print(f"İşlem başarılı! Yeni bakiyeniz: {bakiye:.2f} TL")


para_cekme_uygulaması()  # Corrected typo