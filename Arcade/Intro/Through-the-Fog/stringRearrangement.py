from itertools import permutations
def stringsRearrangement(inputArray):
    allPermutations = permutations(inputArray)

    for permutation in allPermutations:
        ans = True    
        for i in range(len(permutation)-1):
            if differByOneChar(permutation[i],permutation[i+1]) == False:
                ans = False
                break
    
        if ans:
            return True
    return False
    

def differByOneChar(str1,str2):
    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1
    
    if diff_count != 1:
        return False
    return True
