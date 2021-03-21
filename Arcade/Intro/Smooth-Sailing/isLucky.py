def isLucky(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = n//10
    digits.reverse()
    return sum(digits[:len(digits)//2])==sum(digits[len(digits)//2:])
