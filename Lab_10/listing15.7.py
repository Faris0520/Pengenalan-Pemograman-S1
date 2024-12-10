def factorial(n):
    indent = 4*(6-n)*" "
    print(indent + "Enter factorial n = ", n)
    if n == 1:
        print(indent + "Base case.")
        return 1
    else:
        print(indent + "Before recursive call f(" + str(n-1) + ")")
        rest = factorial(n-1)
        print(indent + "After recursive call f(" + str(n-1) + ") = ", rest)
        return n*rest