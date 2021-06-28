def isMAC48Address(inputString):
    if '-' not in inputString:
        return False

    splitted = inputString.split('-')

    if len(splitted) != 6:
        return False

    for i in splitted:
        if len(i) != 2:
            return False

        if not ((ord("A") <= ord(i[0]) <= ord("F")) or (ord("0") <= ord(i[0]) <= ord("9"))):
            return False
        
        if not ((ord("A") <= ord(i[1]) <= ord("F")) or (ord("0") <= ord(i[1]) <= ord("9"))):
            return False
        else:
            continue
    return True
