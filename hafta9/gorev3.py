# Bir karakterin mevcut canından aldığı hasarı çıkaran hasar_al fonksiyonunu oluştur.

# 2 parametre alcaksınız: can, hasar | Amacımız hasar al fonksiyonunu kullanıp kalan canı ekrana yazdırmak

def hasar_al(can, hasar):
    kalan = can - hasar
    if kalan < 0:
        kalan = 0
    return kalan

sonuc = hasar_al(100, 150)

print("Kalan Can:", sonuc)