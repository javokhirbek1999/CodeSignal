def alphabeticShift(inputString):
    t = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    r = [i for i in inputString]
    for i in range(len(inputString)):
        if r[i]=='z':
            r[i] = 'a'
        else:
            r[i] = t[t.index(r[i])+1]
    return ''.join(r)

