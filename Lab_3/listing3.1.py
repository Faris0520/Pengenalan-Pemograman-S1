a = input("Give a number: ")
# kode yg benar -> a = int(a)
b,c=1,0
while b<=a:
	c = c + b
	b = b + 1
print(a,b,c)
print("Result: ", c/b-1)