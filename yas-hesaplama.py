import  datetime

def yas(dogum):
    yil=datetime.date.today().year
    sonuc=yil-dogum
    return sonuc

print(yas(2007))