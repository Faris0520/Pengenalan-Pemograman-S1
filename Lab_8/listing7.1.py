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