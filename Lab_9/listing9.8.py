import csv

def read_table(a_file, a_dict):
    """Read Periodic Table file into a dictionary with element symbol as key.
    The periodic file is a file object opened for reading."""
    data_reader = csv.reader(a_file)

    for row in data_reader:
        # Ignore header rows: elements begin with a number
        if row[0].isdigit():
            symbol_str = row[1]
            a_dict[symbol_str] = row[:8]  # Ignore end of row

def parse_element(element_str):
    """Parse element string into symbol and quantity,
    e.g. Si2 returns ('Si', 2)"""
    symbol_str = ""
    quantity_str = ""
    
    for ch in element_str:
        if ch.isalpha():
            symbol_str += ch
        else:
            quantity_str += ch
    
    if quantity_str == "":  # If no number, default is 1
        quantity_str = "1"
    
    return symbol_str, int(quantity_str)

# 1. Read File
periodic_file = open("Periodic-Table.csv", "r", encoding="windows-1252")

# 2. Create Dictionary of Periodic Table using element symbols as keys
periodic_dict = {}
read_table(periodic_file, periodic_dict)

# 3. Prompt for input and convert compound into a list of elements
compound_str = input("Input a chemical compound, hyphenated, e.g. C-O2: ")
compound_list = compound_str.split("-")

# 4. Initialize atomic mass
mass_float = 0.0
print("The compound is composed of: ", end=' ')

# 5. Parse compound list into symbol-quantity pairs, print name, and add mass
for c in compound_list:
    symbol_str, quantity_int = parse_element(c)
    print(periodic_dict[symbol_str][5], end=' ')  # Print element name
    mass_float += quantity_int * float(periodic_dict[symbol_str][6])  # Add atomic mass

print("\n\nThe atomic mass of the compound is", mass_float)

# Close the file
periodic_file.close()
