def rounders(n):
    s = [int(i) for i in list(str(n))]
    k = -1
    for i in range(len(s)-1):
        if s[k] != 0 and s[k] >= 5:
            s[k] = 0
            s[k-1] +=1
        elif s[k] != 0 and s[k] < 5:
            s[k] = 0
        k-=1
    return int("".join([str(i) for i in s]))
