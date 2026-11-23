# Oyuncunun mevcut puanına bonus puan ekleyen ve sonucu return ile döndüren bir fonksiyon oluştur.

# ÖRNEK
# def puanlama(puan, carpan):
#     toplam = puan * carpan
#     return toplam # return çağırıldığı yere bilgiyi yollar. çağırıldığı yere toplamı yollicak

# sonuc = 10 * puanlama(10,5) # 50
# print("TAM SONUÇ:", sonuc)

# toplu yorum satırı için aralığı seçip: CTRL + K + C yapıyoruz. yorum satırıdnan çıkartmak için CTRL + K + U

# CEVAP

def puan_ekle(puan, bonus):
    toplam = puan + bonus
    if toplam > 100:
        toplam = 100
    return toplam

puan = int(input("Puanınızı Girin: "))
bonus = int(input("Bonusunuzu Girin: "))

sonuc2 = puan_ekle(puan, bonus)

print("Yeni Puan:", sonuc2)