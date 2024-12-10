def main():
    gettysburg_address_set = set()
    declaration_of_indipendence_set = set()
    gettysburg_file = open('D:/Kuliah/Pengenalan Pemograman S1/Lab_9/gettysburg.txt')
    declaration_independence_file = open('decl0fInd.txt')
    for line in gettysburg_file:
        process_line(line, gettysburg_address_set)
    for line in declaration_independence_file:
        process_line(line, declaration_of_indipendence_set)
    pretty_print(gettysburg_address_set, declaration_of_indipendence_set)