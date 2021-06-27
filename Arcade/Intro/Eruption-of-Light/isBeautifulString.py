def isBeautifulString(inputString):
    t = [i for i in inputString]
    t.sort()
    max_count = t.count(t[0])
    cnts = [t.count(i) for i in 'abcdefghijklmnopqrstuvwxyz']
    for i in range(len(cnts)-1):
        if cnts[i]<cnts[i+1]:
            return False
    return True
            
