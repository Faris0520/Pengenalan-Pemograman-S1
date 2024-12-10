def make_word_list(a_file):
    word_list = []

    for line_str in a_file:
        line_list = line_str.split()
        for word in line_list:
            word = word.lower()
            word = word.strip('.,')
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
print("Speech Length: ", len(speech_list))
unique_list = make_unique(speech_list)

print(unique_list)
print("Unique Length: ", len(make_unique(unique_list)))