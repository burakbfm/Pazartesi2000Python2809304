# Sözlük, Anahtar vve değer kavramları

# Minecraft Envanter Sistemi
envanter = {
    "Elmas": 64,
    "Odun": 10,
    "Demir": 5
}
print(envanter["Elmas"]) # sözlükte elemanlar bu şekilde çekilir

print("Elmas:", envanter["Elmas"])

envanter["Altın"] = 7 # sözlüğe elemanlar bu şekilde eklenir. Önce eleman adı sonrasında dış kısma atanacak değeri Sözlük["Değer Adı"] = Değer
print(envanter)

# var olan anahtar kavramlarının değerini artırma

envanter["Odun"] += 5 # sözlükte halihazırda var olan anahtar kavramın değerini artırma

print(envanter)