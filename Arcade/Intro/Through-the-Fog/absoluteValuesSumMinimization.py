def absoluteValuesSumMinimization(a):
    res = []
    for i in a:
        temp = 0
        for j in a:
            temp+=abs(j-i)
        res.append([temp,i])
    res.sort()
    return res[0][1]
