print("=== SIMPAN DATA NILAI ===")            # Judul program untuk simpan data

file = open("nilai_siswa.txt", "w")          # Buka file untuk ditulis (mode write)

while True:                                  # Perulangan input data
    nama = input("Nama siswa (enter untuk selesai): ")  # Input nama siswa
    if nama == "":                           # Jika kosong, keluar loop
        break

    nilai = input("Nilai siswa :")           # Input nilai siswa

    file.write(nama + "," + nilai + "\n")    # Simpan ke file dalam format nama,nilai
    print("Data", nama, "berhasil disimpan") # Konfirmasi data tersimpan

file.close()                                 # Tutup file
print("=== PROGRAM SELESAI ===")             # Penutup bagian simpan data


print("=== MENAMPILKAN DATA NILAI ===")      # Judul program untuk menampilkan data

try:
    with open("nilai_siswa.txt", "r") as file:   # Buka file untuk dibaca (read)
        for line in file:                        # Baca baris per baris
            data = line.strip().split(",")       # Pisahkan data berdasarkan koma
            print(data[0], ":", data[1])         # Cetak nama : nilai
except FileNotFoundError:                        # Jika file tidak ditemukan
    print("file tidak ditemukan")

print("=== PROGRAM SELESAI ===")             # Penutup program
