def pretty_print(ga_set, doi_set):
    print('COunt of unique words of length 4 or greater')
    print('Gettysburg addr: {}, Decl of Ind: {}\n'.format(len(ga_set),len(doi_set)))
    print('{:15s} {:15s}'.format('Operation', 'Count'))
    print('-'*35)
    print('{:15s} {:15d}'.format('Union', len(ga_set.union(doi_set))))
    print('{:15s} {:15d}'.format('Intersection', len(ga_set.intersection(doi_set))))
    print('{:15s} {:15s}'.format('Sym Diff', len(ga_set.symetric_difference(doi_set))))
    print('{:15s} {:15s}'.format('GA_DoI', len(ga_set.difference(doi_set))))
    print('{:15s} {:15s}'.format('DoI-GA', len(doi_set.difference(ga_set))))

    intersection_set = ga_set.intersection(doi_set)
    word_list = list(intersection_set)
    word_list.sort()
    print('\n Common words to both')
    print('-'*20)
    count = 0
    for w in word_list:
        if count % 5 == 0:
            print()
        print('{:13s}'.format(w), end=' ')
        count += 1
