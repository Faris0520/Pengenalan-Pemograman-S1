# find a word with a single example of the vowels a, e, i, o, u in that order
data_file = open("D:/Kuliah/Pengenalan Pemograman S1/Lab_7/dictionary.txt", 'r')

def clean_word(word):
    """Return word in lower case stripped of whitespace"""
    return word.strip().lower()

# main program
for word in data_file:
    word = clean_word(word)
    if len(word) <= 6:
        continue
    print(word)