print("Hello World")                   # Cetak teks Hello World

print("nama")                          # Cetak string "nama" (bukan variabel)

print("5" + 5)                         # ERROR → tidak bisa tambah string dengan angka

value = int("salah")                   # ERROR → "salah" tidak bisa diubah ke int

list_data = [1, 2, 3]                  # List dengan 3 elemen
print(list_data[5])                    # ERROR → index 5 tidak ada (IndexError)

orang = {"nama" : "Eko"}               # Dictionary dengan key "nama"
print(orang["umur"])                   # ERROR → key "umur" tidak ada (KeyError)

print(10 / 0)                          # ERROR → pembagian dengan nol (ZeroDivisionError)


print("=== KALKULATOR SEDERHANA ===")  # Judul program kalkulator

try:
    angka1 = int(input("angka1: "))    # Input angka pertama
    angka2 = int(input("angka2: "))    # Input angka kedua
    hasil = angka1 / angka2            # Hitung hasil pembagian
    print("Hasil", hasil)              # Cetak hasil
except ValueError:                     # Jika input bukan angka
    print("Input pengguna bukan angka")
except ZeroDivisionError:              # Jika pembagian dengan nol
    print("Tidak bisa dibagi dengan 0")
except:                                # Jika ada error lain
    print("Terjadi kesalahan program")

print("=== PROGRAM SELESAI ===")       # Penutup program kalkulator


try:
    angka = int(input("Masukkan angka : "))   # Input angka
except ValueError:                            # Jika input bukan angka
    print("Angka tidak valid")
else:                                         # Jika input valid (angka)
    print("Angka yang anda masukkan", angka)  # Cetak angka yang dimasukkan
    if angka > 0:
        print("Angka positif")                # Jika angka lebih dari 0
    elif angka < 0:
        print("Angka negatif")                # Jika angka kurang dari 0
    else:
        print("Angka nol")                    # Jika angka sama dengan 0
finally:
    print("Program selesai")                  # Bagian ini selalu dijalankan
