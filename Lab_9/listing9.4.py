def pretty_print(word_count_dict):
    value_key_list = []
    for key,val in word_count_dict.items():
        value_key_list.append((val,key))
    value_key_list.sort(reverse=True)
    print('{:11s}{:11s}'.format('Word', 'Count'))
    print('_'*21)
    for val,key in value_key_list:
        print('{:12s}  {:<3d}'.format(key,val))