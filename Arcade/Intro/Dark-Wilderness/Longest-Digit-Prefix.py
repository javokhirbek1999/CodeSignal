def longestDigitsPrefix(inputString):
    pref = ""
    for i in inputString:
        if i in '0123456789':
            pref+=i
        else:
            break
    return pref
