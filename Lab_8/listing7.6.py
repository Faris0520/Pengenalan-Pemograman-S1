def make_word_list(a_file):
    word_list = []

    for line_str in a_file:
        line_list = line_str.split()
        for word in line_list:
            if word != "--":
                word_list.append(word)
    return word_list

gba_file = open("D:\Kuliah\Pengenalan Pemograman S1\Lab_8\gettysburg.txt", "r")
speech_list = make_word_list(gba_file)

print(speech_list)
print("Speech Length: ", len(speech_list))