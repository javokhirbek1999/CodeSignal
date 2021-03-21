def shapeArea(n):
    total = 1
    if n == 1:
        return total
        pass
    else:
        r = n-1
        for i in range(0, n*2):
            total = total + r
        return total
