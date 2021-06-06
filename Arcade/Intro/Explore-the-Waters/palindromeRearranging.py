def palindromeRearranging(inputString:str):
    characters = []
    c = 0
    for i in inputString:
        characters.append(i)
    for i in set(characters):
        if characters.count(i)%2!=0:
            c+=1
    return c<=1
