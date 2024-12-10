# mengklasifikasikan serangkaian angka terhadap angka sempurna, 
# berlimpah atau kurang kecuali dinyatakan sebaliknya, variabel diasumsikan bertipe int.

top_num_str = input("What is the upper number for the range: ")
top_num = int(top_num_str)
number = 2
while number <= top_num:
    divisor = 1
    sum_of_divisors = 0
    while divisor < number:
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor
        divisor = divisor + 1

    if number == sum_of_divisors:
        print(number, "is perfect")
    if number < sum_of_divisors:
        print(number, "is abundant/berlebih")
    if number > sum_of_divisors:
        print(number, "is deficient/kurang")
    number += 1