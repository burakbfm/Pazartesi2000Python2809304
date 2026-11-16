# Ders Türü: Uygulamalı proje geliştirme

# BÖLÜM 1 — Proje Tanıtımı
# Proje Senaryosu
# Bir süper kahraman turnuvası düzenlenmektedir.
# Turnuvaya katılan kahramanların farklı saldırı ve savunma özellikleri bulunmaktadır.
# Oyuncular bir kahraman seçecek, kahramanın özelliklerini görüntüleyecek ve toplam gücünü hesaplayacaktır.
# Projede Kullanılacak Kahramanlar


# Kahraman adı: Alev
# Saldırı: 15
# Savunma: 7

# Kahraman Adı: Buz
# Saldırı: 12
# Savunma: 10

# Gölge
# Saldırı: 18
# Savunma: 4

# Güç Formülü:
# Toplam Güç = Saldırı × 2 + Savunma + Bonus

# BÖLÜM 2 — ANA PROJE: SÜPER KAHRAMAN GÜÇ HESAPLAYICISI

# Süre: 20 dakika

# PROJE 01 | Kahramanını Seç ve Gücünü Hesapla

# Zorluk: Orta
# Konular: Fonksiyonlar, sözlükler, koşullar ve kullanıcı girdileri

# A. SİZDEN BEKLENENLER
# Kahramanların özelliklerini sözlükte sakla.
# Kullanıcıdan kahraman seçmesini iste.
# guc_hesapla fonksiyonunu oluştur.
# Kahramanın saldırı ve savunma gücünü fonksiyona gönder.
# Kullanıcıdan bonus puan al.
# Toplam gücü hesaplayarak ekrana yazdır.
# Geçersiz kahraman seçimlerini kontrol et.

# B. ÖĞRENCİYE VERİLECEK BAŞLANGIÇ KODU

kahramanlar = {
    "Alev": {"saldiri": 15, "savunma": 7},
    "Buz": {"saldiri": 12, "savunma": 10},
    "Gölge": {"saldiri": 18, "savunma": 4}
}

def guc_hesapla(saldiri, savunma, bonus=0):
    # Güç hesaplama işlemini tamamla
    toplam = saldiri * 2 + savunma + bonus
    return toplam
    

print("=== SÜPER KAHRAMAN ARENASI ===")

# Görev 1: Kahramanları listele.
print("Kahramanlar:")
for isim in kahramanlar:
    print("-", isim)
# Görev 2: Kullanıcıdan seçim al.
secim = input("Kahraman seç: ")
if secim in kahramanlar:
    kahraman = kahramanlar[secim]
    # Görev 4: Bonus puan iste.
    bonus = int(input("Bonus puan (0*10): "))
    if bonus < 0 or bonus > 10:
        print("Geçersiz Bonus! Bonus:0 yapıldı.")
        bonus = 0
    
    # Görev 5: Toplam gücü hesapla.
    toplam_guc = guc_hesapla(kahraman["saldiri"],kahraman["savunma"],bonus)
    # Görev 3: Kahramanın özelliklerini bul.
    print("KAHRAMAN BİLGİLERİ")
    print("Kahraman:", secim)
    print("Saldırı:",kahraman["saldiri"])
    print("Savunma:",kahraman["savunma"])
    print("Bonus:",bonus)

    print("Toplam Güç:",toplam_guc)
else:
    print("Böyle bir kahraman bulunamadı")


