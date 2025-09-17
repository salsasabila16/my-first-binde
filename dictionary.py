siswa = {
    "nama": "Salsa",
    "umur": 15,
    "kelas": " X PPLG 2"
}

print(siswa)

print(siswa["nama"])
print(siswa["umur"])
print(siswa["kelas"])

siswa["kelas"] = "RPL 2"
print(siswa)

del siswa["umur"]
print(siswa)

for key in siswa:
    print(key)

for key in siswa:
    print(key, siswa[key])

for key, value in siswa.items():
    print(key, value)