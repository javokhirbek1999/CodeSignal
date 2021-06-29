import re
def sumUpNumbers(inputString):
    t = inputString.split(",")
    r = re.sub("[^\d]",","," ".join(t))
    s = re.sub("[,]"," ",r)
    total = []
    for i in s.split(' '):
        if i.isdigit():
            total.append(int(i))
    return sum(total)
