def firstDigit(inputString):
    digits = [int(i) for i in inputString if i in ['1','2','3','4','5','6','7','8','9','0']]
    max_digit = max(digits[:(len(digits)+1)//2])
    return str(max_digit)
