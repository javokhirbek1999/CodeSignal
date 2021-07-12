def mirrorBits(a):
    return int("".join(list(bin(a)[2:])[::-1]),2)
