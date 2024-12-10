file_str = input("Open what file:")

try:
    input_file = open(file_str)
    find_line_str = input("Which line (integer): ")
    find_line_int = int(find_line_str)
    line_count_int = 1
    for line_str in input_file:
        if line_count_int == find_line_int:
            print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
            break
        line_count_int += 1
    else:
        print("Line {} of file {} not found".format(find_line_int, file_str))
    input_file.close()

except FileNotFoundError:
    print("The file", file_str, "doesnt exist")

except ValueError:
    print("Line", find_line_str,"isnt a legal line number")

print("End of the program")