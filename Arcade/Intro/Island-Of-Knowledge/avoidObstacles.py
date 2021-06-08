def avoidObstacles(inputArray):
    i = 1
    while True:
        j = i
        while True:
            if j in inputArray:
                break
            elif j>max(inputArray):
                return i
            else:
                j+=i
        i+=1

        if max(inputArray)<i:
            return i
