def fileNaming(names):
    result = []
    for name in names:
        if name in result:
            k = 1
            while "{}({})".format(name, k) in result:
                k += 1
            name = "{}({})".format(name, k)
        result.append(name)
    return result
