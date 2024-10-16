class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Mevcut bakiyeniz: ${ self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Yetersiz bakiye. Lütfen önce para yatırın.")
        else:
            self.balance -= amount
            print(f"Para çekme başarılı. Yeni bakiyeniz: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Para yatırma başarılı. Yeni bakiyeniz: ${self.balance}")

# Örnek kullanım:
atm = ATM(40000.64)  # ATM'yi $40,000.64 bakiye ile başlat

while True:
    print("MY Bank ATM'ye hoş geldiniz")
    print("1. Bakiye kontrolü")
    print("2. Para çekme")
    print("3. Para yatırma")
    print("4. Çıkış")

    option = int(input("Lütfen bir seçenek seçin: "))

    if option == 1:
        atm.check_balance()
    elif option == 2:
        amount = float(input("Ne kadar para çekmek istiyorsunuz? $"))
        atm.withdraw(amount)
    elif option == 3:
        amount = float(input("Ne kadar para yatırmak istiyorsunuz? $"))
        atm.deposit(amount)
    elif option == 4:
        print("MY Bank ATM'yi kullandığınız için teşekkür ederiz. Güle güle!")
        break
    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")