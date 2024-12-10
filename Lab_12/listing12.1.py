def special_sum(a,b):
    if type(a) == int and type(b) == int:
        result = a + b
    else:
        try:
            result = int(a) + int(b)
        except ValueError:
            result = 0
    return result