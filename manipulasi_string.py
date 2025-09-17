nama = "salsa"
umur = 15

pesan = "Nama saya" + nama + ", umur " + str(umur)
print(pesan)

print(len(nama))
print(len(pesan))

nama = "python"
print(nama[0])
print(nama[1])
print(nama[2])

print(nama[-1])
print(nama[-2])
print(nama[-3])

nama = "python"
print(nama[:])
print(nama[0:3])
print(nama[2:])

nama = "Salsa"
print(nama)
nama_upper = nama.upper()   
print(nama_upper)
nama_lower = nama.lower()
print(nama_lower)

nama = "Salsa"
nama_title = nama.title()
print(nama_title)
nama_capilized = nama.capitalize()
print(nama_capilized)

nama = "   Salsa    "
name_strip = nama.strip()
print(name_strip)

kalimat = "I love Java"
kalimat_baru = kalimat.replace("Java", "Python")
print(kalimat_baru)

nama = "salsa sabila humaira"
jumlah_k = nama.count("salsa")
print(jumlah_k)

kalimat = "Python Programming"
posisi = kalimat.find("Programming")
print(posisi)

kalimat = "Baris pertama\nBaris kedua"
print(kalimat)

kalimat = "Nama:\tSalsa\nUmur:\t15"
print(kalimat)

kalimat = "Dia berkata \"Hello\" kepada saya"
print(kalimat)

nama = "Salsa"
umur = 15
kota = "Banjar"

kalimat = f"Halo, nama saya {nama}, umur saya {umur}, tinggal di {kota}"
print(kalimat)

harga = 10000
jumlah = 3

total = f"Total : {harga * jumlah}"
print(total)

nama = "salsa sabila humaira"
kalimat = f"Hello {nama.upper()}"
print(kalimat)
