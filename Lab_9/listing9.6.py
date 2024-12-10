def read_table(a_file, a_dict):
    data_reader = csv.reader(a_file)

    for row in data_reader:
        if row[0].isdigit():
            symbol_str = row[1]
            a_dict[symbol_str] = row[:8]