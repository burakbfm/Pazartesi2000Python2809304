# print("=== SAVAŞ BAŞLIYOR ===")
# print("Kahraman saldırıya geçti!")

# def fonksiyon_adi(x,y,z,...):
#     kodlar

# 1 FONKSİYON OLUŞTURMA
def savas_baslat():
    print("=== SAVAŞ BAŞLIYOR ===")
    print("Kahraman saldırıya geçti!")

# FONSKİYONLAR ÇAĞIRILMADIĞI SÜRECE ÇALIŞMAZ. ÇAĞIRMAK İÇİN FONKSİYONUN ADINI KULLANIRIZ.
    
# def: Fonksiyonu tanımlamak için kullanılır.
# savas_baslat() fonksiyonun ismidir.
# (): Parametrelerin yazıldığı bölümdür
# savas_baslat(): Fonksiyonu çalıştırır

# 2 PARAMETRELER VE RETURN KULLANIMI 
def saldiri_hesapla(guc, carpan): # guc ve carpan parametredir
    sonuc = guc * carpan
    return sonuc # return komutu çağırıldığı yere sağındaki bilgiyi yollar

saldiri = saldiri_hesapla(15,3) # 45

print("Toplam saldırı gücü:",saldiri)


# 3 VARSAYILAN PARAMETRELER
def toplam_guc(saldiri, savunma, bonus=0): # parametreye önden değer atarsanız kullanıcı değer vermese bile varsayılan atanan değeri kullanır
    return saldiri + savunma + bonus

print(toplam_guc(20,10)) # 30
print(toplam_guc(20,10,15)) # 45