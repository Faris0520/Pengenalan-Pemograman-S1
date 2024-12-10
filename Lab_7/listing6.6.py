# find a word with a single example of the vowels a, e, i, o, u in that order
data_file = open("D:/Kuliah/Pengenalan Pemograman S1/Lab_7/dictionary.txt", 'r')

def clean_word(word):
    """Return word in lower case stripped of whitespace"""
    return word.strip().lower()

def get_vowels_in_word(word):
    vowel_str = "aeiou"
    vowels_in_word = ""
    for char in word:
        if char in vowel_str:
            vowels_in_word += char
    return vowels_in_word

# main
print("Find words containing vowels 'aeiou' in that order: ")
for word in data_file:
    word = clean_word(word)
    if len(word) <= 6:
        continue
    vowel_str = get_vowels_in_word(word)
    if vowel_str == 'aeiou':
        print(word)