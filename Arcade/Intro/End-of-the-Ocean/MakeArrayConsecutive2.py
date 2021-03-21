def makeArrayConsecutive2(statues):
    lowest = sorted(statues)[0]
    highest = sorted(statues)[-1]
    c = 0
    for i in range(lowest, highest+1):
        t = statues.count(i)
        if t == 0:
            c += 1
    return c
