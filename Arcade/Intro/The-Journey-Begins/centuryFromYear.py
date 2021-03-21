def centuryFromYear(year):
    y = 0
    cnt = 0
    while y < year:
        y = y + 100
        cnt = cnt + 1
    return cnt
