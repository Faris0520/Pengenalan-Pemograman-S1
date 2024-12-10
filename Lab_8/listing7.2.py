def are_anagrams(word1, word2):
    """Return True, if words are anagrams"""
    # 2. sort the characters in the words
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    # 3. check that the sorted words are idnetical
    if word1_sorted == word2_sorted:
        return True
    else:
        return False

print("Anagram test")

# 1. input two words
two_words = input("Enter two space separated words: ")
two_word_list = two_words.split()

word1 = two_word_list[0]
word2 = two_word_list[1]

if are_anagrams(word1, word2):
    print("The words are anagrams")
else:
    print("The words are not anagrams")