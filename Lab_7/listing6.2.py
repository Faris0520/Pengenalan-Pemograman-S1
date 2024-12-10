# print all words in a dictionary file that has one word per line

# open file named "dictionary.txt" for reading('r')
data_file = open("D:/Kuliah/Pengenalan Pemograman S1/Lab_7/input.txt", 'r')

# iterate through the file one line at a time
for line_str in data_file:
    print(line_str)