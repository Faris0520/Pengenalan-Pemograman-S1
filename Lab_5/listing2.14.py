# classify a range of numbers with respect to perfect, adundant, or deficient
# unless otherwise stated, variables are assumed to be of type int

top_num_str = input("What is the upper number for the range: ")
top_num = int(top_num_str)
number = 2
while number < top_num:
    divisor = 1
    sum_of_divisors = 0
    while divisor < number:
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor
        divisor = divisor + 1
    number += 1