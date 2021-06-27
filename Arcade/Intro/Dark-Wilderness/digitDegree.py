def digitDegree(n):
    t = str(n)
    c = 0
    while len(t)!=1:
        temp = 0
        for i in t:
            temp+=int(i)
        t = str(temp)
        c+=1
    return c
