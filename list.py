# List kosong
daftar_kosong = []
print (daftar_kosong)

# List dengan angka 
angka = [1, 2, 3, 4, 5,]
print (angka)

# List dengan string
nama = ["Salsa", "Caca", "Bila", "Maira", "Sabila"]
print (nama)

# List campuran
campuran = ["Salsa", 16, "Caca", 5,  "Bila", 20, "Maira", 21, "Sabila"]
print (campuran)

# Mengakses elemen
buah = ["mangga", "stroberi", "alpukat", "durian"]
print (buah[0]) # Mangga
print (buah[2]) # stroberi
print (buah[1]) # alpukat
print (buah[-1]) # durian (elemen terakhir)

# Mengubah elemen
warna = ["oren", "abu" , "kuning"]
print (warna)
warna[1] = "kuning"
print (warna)  # ["oren", "abu" , "kuning"]

buah = ["apel", "jeruk"]
print(buah)
buah.append("durian")
print(buah)
buah.insert(1, "buah naga")
print(buah)

buah.remove ("jeruk")
print(buah)

buah.pop()
print(buah)

del buah[0]
print(buah)

buah = ["apel", "jeruk", "mangga"]
print(len(buah))

satu = [1,2,3,4,5]
print(satu)
dua = [6,7,8,9,10]
print(dua)

gabungan = satu + dua
print(gabungan)

banyak_buah = ["apel", "jeruk", "mangga", "salak"]
for buah in banyak_buah:
    print(buah)

for i in range(0, len(banyak_buah)):
    print(banyak_buah[i])

if "semangka" in banyak_buah:
    print ("Ada semangka")
else:
    print ("Tidak ada semangka")