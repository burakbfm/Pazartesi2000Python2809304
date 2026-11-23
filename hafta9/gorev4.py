# Oyuncunun puanına göre seviyesini belirleyen bir fonksiyon oluştur.

# Kurallar: 70 ve üzeri puan alanlar "Usta", diğerleri "Çaylak" olacak.
# 0–49: Çaylak
# 50–79: Gelişen
# 80 ve üzeri: Usta


# birden fazla koşulda yanlzıca if kullanırsak bütün if ler kontrol edilir ve birden fazzla doğru cevap olabilir
# eliflerde doğru olan bulunduktan sonra diğer cevaplara bakılmaz o yüzden en zor ihtimalden en kolay ihtimale göre yazılır
def seviye_belirle(puan): 
    if puan >= 80:
        return "Usta"
    elif puan >= 50:
        return "Gelişen"
    else:
        return "Çaylak"

    
isim = input("İsminiz: ")
puan = int(input("Puanınız: "))

print(isim,seviye_belirle(puan))
print("Ali", seviye_belirle(85))
print("Ayşe", seviye_belirle(50))