def alpha(n):
    for i in range(1, n+1):
        print("parrs" * i)

alpha(2)
print("\n==============================")

nilai = int(input("masukkan nilai mu : "))

if 90 <= nilai < 100:
    print(f"Nilai mu {nilai}, kamu dapat A")
elif 80 <= nilai < 90:
    print(f"Niali mu {nilai}, kamu dapat B")
elif 70 <= nilai < 80:
    print(f"Nilai mu {nilai}, kamu dapat C")
else: 
    print(f"ga usah sekolah kamu dek")