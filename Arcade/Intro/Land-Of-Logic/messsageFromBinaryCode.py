def messageFromBinaryCode(code):
    res = ""
    t = 0
    for _ in range(len(code)//8):
        res+=chr(int("".join(list(code)[t:t+8]), 2))
        t+= 8
    return res
