def deleteDigit(n):
    digits = []
    num = list(str(n))
    for i in range(len(num)):
        num.pop(i)
        temp = "".join(num)
        digits.append(int(temp))
        num = list(str(n))
    return max(digits)
