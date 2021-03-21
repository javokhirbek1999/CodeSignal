def sortByHeight(a):
    t = []
    for i in a:
        if i == -1:
            pass
        else:
            t.append(i)
    t.sort()
    for i in range(len(a)):
        if a[i] == -1:
            t.insert(i,-1)
    return t
    
