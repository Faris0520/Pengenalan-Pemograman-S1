# fungsi rekursif untnuk membalik string

def reverser (a_str):
    #base case
    if len(a_str):
        return a_str
    # recursive step
        #divide into parts
        #conquer/reassemble
         
the_str = input("Reverse what string:")
result = reverser(the_str)
print("The reverse of {} is {}".format(the_str,result))      