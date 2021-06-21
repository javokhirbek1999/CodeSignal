def arrayMaxConsecutiveSum(inputArray, k):
    win = initializeSum(inputArray,k)
    m = win
    for i in range(1,(len(inputArray)-k)+1):
        win = win - inputArray[i-1]+inputArray[i+k-1]
        m = max(m,win)
    return m

def initializeSum(arr,k):
    s = 0
    for i in range(k):
        s+=arr[i]
    return s
