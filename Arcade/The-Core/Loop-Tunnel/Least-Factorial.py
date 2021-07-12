def leastFactorial(n):
    if n == 1:
        return 1
    factorial = 1
    for i in range(1,6):
        factorial = factorial*i
        if factorial>=n:
            return factorial

