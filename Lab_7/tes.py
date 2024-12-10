import random
import string

characters = string.ascii_letters + string.digits + string.whitespace + string.punctuation
long_string = ''.join(random.choices(characters, k=5000))

file = open("d:/kuliah/pengenalan pemograman s1/lab_7/jumble.txt", "w")
file.write(long_string)

file_name = input("Enter the file name: ")
whitespace_counts = {' ': 0, '\t': 0, '\n': 0}

try:
    file = open(file_name, "r")
    content = file.read()
        
    for char in content:
        if char in whitespace_counts:
            whitespace_counts[char] += 1

    print("Histogram of whitespace counts:")
    for whitespace, count in whitespace_counts.items():
        if whitespace == ' ':
            print(f"Spaces: {'*' * count}")
        elif whitespace == '\t':
            print(f"Tabs: {'*' * count}")
        elif whitespace == '\n':
            print(f"Newlines: {'*' * count}")

except FileNotFoundError:
    print(f"The file {file_name} does not exist.")