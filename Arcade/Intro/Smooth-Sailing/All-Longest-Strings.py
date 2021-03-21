def allLongestStrings(inputArray):
    max_size = 0
    for i in inputArray:
        if max_size<len(i):
            max_size = len(i)
    
    return ([arr for arr in inputArray if len(arr)==max_size])
            
