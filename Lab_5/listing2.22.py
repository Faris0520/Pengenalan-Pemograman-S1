print ("Allow the user to enter a series of even integers. Sum them")
print("Ignore non-even input. End input with a '.'")

number_str = input("Number: ")
the_sum = 0

while number_str != ".":
    number = int(number_str)
    if number % 2 == 1:
        print("Error, only even number please")
    else:
        the_sum += number
    number_str = input("Number: ")

print("The sum is:", the_sum)