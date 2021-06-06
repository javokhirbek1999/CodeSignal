def arrayChange(inputArray):
    c = 0
    for i in range(len(inputArray)-1):
        if inputArray[i]>=inputArray[i+1]: 
            t = abs(inputArray[i]-inputArray[i+1]+1)
            inputArray[i+1] +=t
            c += t
    return c
