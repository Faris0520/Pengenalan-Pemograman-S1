import random
number = random.randint(0, 100)

print("Hi-Lo number guessing game: between 0 and 100 inclusive")
print()

guess_str = input("Guess a number: ")
guess = int(guess_str)

while 0 <= guess <= 100:
    if guess > number:
        print("Guessed too high")
    elif guess < number:
        print("Guessed too low")
    else:
        print("You guessed it! The number was:", number)
        break
    guess_str = input("Guess a number: ")
    guess = int(guess_str)
else:
    print("You quit early, the number was: ", number)