import string
def process_line(line, word_count_dict):
    line = line.strip()
    word_list = line.strip()
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)