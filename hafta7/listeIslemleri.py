puanlar = [50, 80, 65] # Köşeli parantez geldiği anda değişkenimiz bir listeye dönüşür.

print(puanlar) # [50, 80, 65]

puanlar.append(95) # append fonskiyonu listeye eleman eklemeye yarar .append(x) | Listeye eklenen eleman sona eklenir.

print(puanlar) # [50, 80, 65, 95]

puanlar.remove(80) # remove fonksiyonu listeden eleman çıkartmaya yarar .remove(x)

print(puanlar) # [50, 65, 95]


print("Puanlar:", puanlar)
print("Oyuncu Sayısı:", len(puanlar)) # len() fonksiyonu içine yazılan listenin eleman sayısını verir.
print("En Yüksek Puan:", max(puanlar)) # max() fonskiyonu listedeki sayısal elemanlardan en yükseğini verir.
print("En Düşük Puan:", min(puanlar)) # min() fonskiyonu listedeki sayısal elemanlardan en düşüğünü verir.

for i in range(5): # for belirlediğimiz sayı kadar tekrar yapar ve 0 dan başlayarak kendi içindeki değişkene eleman atar yanlızca biz eleman vermezsek.
    print("Burak", i)

for i in range(len(puanlar)): # listedeki elemanlar arkaplanda 0 dan başlayarak sıra numarası alır puanlar[0] kodu, punlar listesindeki 1. elemana tekabül eder.
    print("Sıra Numarası:", i, "Puan:", puanlar[i])

# len(puanlar) liste elemanı sayısı kadar yani 3 olduğu için for 3 tekrar yapar. her tekrarda i 0 dan başlayarak değer alır.