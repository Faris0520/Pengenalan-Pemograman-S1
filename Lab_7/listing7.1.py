# Find a word with a single ecample of the vowels a i u e o in that order

data_file = open("D:/Kuliah/Pengenalan Pemograman S1/Lab_7/dictionary.txt", "r")

def clean_word(word):
    return word.strip().lower()

def get_vowels_in_word(word):
    vowel_str = "aeus"
    vowels_in_word = ""
    for char in word:
        if char in vowel_str:
            vowels_in_word += char
    return vowels_in_word

# main program
print("Find words containing vowels 'aiueo' in that order: ")
for word in data_file:
    word = clean_word(word)
    if len(word) <= 6:
        continue
    vowel_str = get_vowels_in_word(word)
    if vowel_str == 'aeiou':
        print(word)