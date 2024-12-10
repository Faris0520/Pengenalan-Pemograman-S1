divisor = 1
sum_of_divisors = 0
while divisor < number:
    if number % divisor == 0:
        sum_of_divisors = sum_of_divisors + divisor
    divisor = divisor + 1