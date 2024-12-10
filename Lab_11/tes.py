angka = int(input("masukkan angka: "))

total = 0

for i in range(1, angka+1):
    total += i

print(f"jumlah dari 1 ke {angka} adalah {total}")
print("")
# 

array = [1, 2, 60, 3, 32]

maksimum = 0

for angka in array:
    if angka > maksimum:
        maksimum = angka
        
print(f"nilai maksimum adalah {maksimum}")