import random
nomor = random.randint(0,100)

print("ini adalah game tebak angka. silahkan tebak angkanya")
print()

tebak_input = input("Masukkan angka :")
tebak = int(tebak_input)

while 0 <= tebak <= 100:
    if tebak < nomor:
        print("Tebakan mu terlalu kecil")
    elif tebak > nomor:
        print("Tebakan mu terlalu tinggi")
    else:
        print(f"Kamu benar! Angkanya adalah {nomor}")
        break
    tebak_input = input("masukkan angka: ")
    tebak = int(tebak_input)
else:
    print(f"tebakan mu terlalu jauh. jawabannya adlaah {nomor}")