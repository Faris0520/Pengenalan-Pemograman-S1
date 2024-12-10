def make_word_list(a_file):
    word_list = []

    for line_str in a_file:
        line_list = line_str.split()
        for word in line_list:
            if word != "--":
                word_list.append(word)
    return word_list

def make_unique(word_list):
    unique_list = []

    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)

    return unique_list

gba_file = open("D:\Kuliah\Pengenalan Pemograman S1\Lab_8\gettysburg.txt", "r")
speech_list = make_word_list(gba_file)

print(speech_list)
print("Speech length: ", len(speech_list))
print("Unique length: ", len(make_unique(speech_list)))