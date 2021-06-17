def variableName(name):
    digits = ['1','2','3','4','5','6','7','8','9','0']
    if name[0] in digits:
        return False
    temp = []
    name = name.lower()
    t = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    for i in name:
        if i in digits or i in t or i == "_":
            pass
        else:
            temp.append(i)
    return len(temp)==0
