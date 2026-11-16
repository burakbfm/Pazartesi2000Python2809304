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
    

print("=== SÜPER KAHRAMAN ARENASI ===")

# Görev 1: Kahramanları listele.
# Görev 2: Kullanıcıdan seçim al.
# Görev 3: Kahramanın özelliklerini bul.
# Görev 4: Bonus puan iste.
# Görev 5: Toplam gücü hesapla.