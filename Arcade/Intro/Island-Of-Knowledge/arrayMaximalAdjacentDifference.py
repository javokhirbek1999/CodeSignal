def arrayMaximalAdjacentDifference(inputArray):
    diffs = []
    for i in range(len(inputArray)-1):
        diffs.append(abs(inputArray[i]-inputArray[i+1]))
    return sorted(diffs)[-1]
