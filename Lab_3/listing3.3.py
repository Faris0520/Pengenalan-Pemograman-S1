# masukkan value/input/nilai
limit_string = input("Jarak dari 1 ke input :")
# ubah dari string ke integer/angka
limit_integer = int(limit_string)
# inisialisasi variabel ke 1
count_integer = 1
# inisialisasi variabel ke 0
sum_integer = 0

# selama count_integer lebih kecil sama dengan limit_integer
while count_integer <= limit_integer:
    # tambahkan sum_integer dengan count_integer
    sum_integer = sum_integer + count_integer
    # tambahkan count_integer dengan 1
    count_integer = count_integer + 1
# hitung rata-rata
average_float = sum_integer / (count_integer - 1)
# tampilkan hasil
print(f"Jarak dari 1 ke {limit_integer} adalah {sum_integer}")

# terlalu banyak komentar