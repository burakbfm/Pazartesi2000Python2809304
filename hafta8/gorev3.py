# GÖREV 03 | Return Hatasını Bul

# Zorluk: Orta

# B. SİZDEN BEKLENENLER
# Programın neden hata verdiğini bul.
# print() ile return arasındaki farkı açıkla.
# Fonksiyonu düzelt.
# Son gücü doğru hesapla.

# A. ÖĞRENCİYE VERİLECEK HATALI KOD

def guc_artir(guc):
    yeni_guc = guc + 20
    print(yeni_guc)

sonuc = guc_artir(50)

print("Son güç:", sonuc + 10)