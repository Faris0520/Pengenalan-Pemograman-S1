number_str = input("Find the square root of integer: ")
number_int = int(number_str)
guess_str = input("Initial guess: ")
guess_float = float(guess_str)
tolerance_float = float(input("What tolerance: "))

original_guess_float = guess_float
count_int = 0
previous_float = 0

while (previous_float - guess_float) > tolerance_float:
    previous_float = guess_float
    quotient_float = number_int/guess_float
    guess_float = (quotient_float + guess_float)/2
    count_int = count_int + 1

# output
print(f"Square root of {number_int} is: {guess_float}")
print(f"Took {count_int} guesses to reach the tolerance {tolerance_float}")
print(f"Starting from a guess of: {original_guess_float}")

