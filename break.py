angka_rahasia = 16033

while True:
    tebakan = int(input("Masukakan tebakan: "))

    if tebakan == angka_rahasia:
        print("selamat, Anda benar")
        break
    else:
        print("Salah, coba lagi")
