def fibonacii(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacii(n-1) + fibonacii(n-2)