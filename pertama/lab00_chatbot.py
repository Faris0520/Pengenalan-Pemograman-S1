import random

def nilai_acak(min, max):
    return random.randint(min, max)

def hitung_kecocokan(nilai):
    if nilai >= 80:
        return "Sangat Cocok"
    elif nilai >= 60:
        return "Cukup Cocok"
    elif nilai >= 40:
        return "Kurang Cocok"
    else:
        return "Tidak Cocok"

print("Selamat datang di Chatbot Persahabatan!")
print("======================================")

namaKamu = input("Masukkan nama kamu: ")
namaTeman = input("Masukkan nama teman kamu: ")

tingkat_persahabatan = nilai_acak(0, 100)
tingkat_kesamaan = nilai_acak(0, 100)
tingkat_komunikasi = nilai_acak(0, 100)

print("\nHasil Analisis Persahabatan:")
print("============================")
print(f"1. Tingkat persahabatan antara {namaKamu} dan {namaTeman} adalah {tingkat_persahabatan}%")
print(f"2. Tingkat kesamaan minat: {tingkat_kesamaan}%")
print(f"3. Tingkat komunikasi: {tingkat_komunikasi}%")

rata_rata = (tingkat_persahabatan + tingkat_kesamaan + tingkat_komunikasi) / 3
kecocokan = hitung_kecocokan(rata_rata)

print(f"\nRata-rata keseluruhan: {rata_rata:.2f}%")
print(f"Kesimpulan: {namaKamu} dan {namaTeman} {kecocokan}")

if kecocokan == "Sangat Cocok":
    print("\nWah, kalian benar-benar sahabat sejati!")
    print("Terus jaga persahabatan kalian ya!")
elif kecocokan == "Cukup Cocok":
    print("\nHubungan kalian cukup baik.")
    print("Cobalah untuk lebih sering berkomunikasi dan berbagi minat bersama.")
elif kecocokan == "Kurang Cocok":
    print("\nSepartinya ada beberapa hal yang perlu diperbaiki dalam persahabatan kalian.")
    print("Coba luangkan waktu untuk lebih mengenal satu sama lain.")
else:
    print("\nJangan khawatir! Setiap persahabatan butuh waktu untuk berkembang.")
    print("Cobalah untuk menemukan kesamaan dan membangun komunikasi yang lebih baik.")

print("\nTerima kasih telah menggunakan Chatbot Persahabatan!")