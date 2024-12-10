#square root = akar kuadrat

num_str = input("Find the square root of integer: ")
num_int = int(num_str)
guess_str = input("Initial guess: ")
guess_int = int(guess_str)
tolerance_float = float(input("What tolerance: "))

original_guess_int = guess_int
count_int = 0

# algoritma nya (kosong)

# output

print(f"Square root of {num_int} is {guess_int}")
print(f"Took {count_int} guesses to reach the tolerance {tolerance_float}")
print(f"Starting from a guess of {original_guess_int}")
