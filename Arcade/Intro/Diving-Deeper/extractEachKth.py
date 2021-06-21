def extractEachKth(inputArray, k):
    n = len(inputArray)//k
    indices = []
    j = k-1
    for _ in range(n):
        indices.append(j)
        j +=k
    r = []
    for i in range(len(inputArray)):
        if i not in indices:
            r.append(inputArray[i])
    return r
