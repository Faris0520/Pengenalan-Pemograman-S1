# menghitung luas(area) dan keliling(circumference) lingkaran dari jari-jarinya
# 1. masukkan jari-jari lingkaran
# 2. masukkan ke formula
# 3. hitung hasilnya

import math

radius_str = input("Enter the radius of your circle: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print(f"The circumference is: {circumference} \
      and the area is {area}")