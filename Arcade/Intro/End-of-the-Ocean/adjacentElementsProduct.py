def adjacentElementsProduct(inputArray):
    arr = []
    for i in range(len(inputArray)-1):
        x = inputArray[i]
        y = inputArray[i+1]
        arr.append(x*y)
    return max(arr)
