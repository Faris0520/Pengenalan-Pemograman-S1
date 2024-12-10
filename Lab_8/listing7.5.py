# Gettysburg address analysis
# count words , unique words

def make_word_list(a_file):
    """Create a list of words from a file"""
    word_list = []

    for line_str in a_file:
        line_list= line_str.split()
        word_list.extend(line_list)
    return word_list

gba_file = open("D:\Kuliah\Pengenalan Pemograman S1\Lab_8\gettysburg.txt", "r")
speech_list = make_word_list(gba_file)

print(speech_list)
print("Length: ", len(speech_list))