import string
def process_line(line, word_set):
    line = line.strip()
    word_list = line.strip()
    for word in word_list:
        if word != '--':
            word = word.strip()
            word = word.strip(string.punctuation)
            word = word.lower()
            add_word(word, word_set)