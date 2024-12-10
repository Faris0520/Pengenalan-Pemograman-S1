a = input("masukkan angka:")

a = int(a)
b = 1
c = 0

while b <= a:
    c = c + a
    b = b + 1

avg = c/(b-1)
print(f"{avg}, {a}") 