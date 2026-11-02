# Görev 3: Kayıp Puanlar – Zor

# Bir oyunda oyuncuların puanlarını iki katına çıkaran fonksiyon hazırlanmıştır. Ancak sonuç başka bir işlemde kullanıldığında hata oluşmaktadır.

def iki_kat(sayi):
    sonuc = sayi * 2
    print(sonuc)

puan = iki_kat(5)
print(puan + 10)