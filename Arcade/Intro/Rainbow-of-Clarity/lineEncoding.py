def lineEncoding(s):
    org = list(s)
    srted = [[]]
    for i in range(len(org)-1):
        if org[i]==org[i+1]:
            srted[-1].append(org[i])
        else:
            srted.append([org[i+1]])
    srted[0].append(org[0])
    res = ""
    for i in srted:
        if len(i)>1:
            res+=f"{len(i)}{i[0]}"
        else:
            res+=f"{i[0]}"
    return res
