def minesweeper(matrix):
    result = []
    for _ in range(len(matrix)): 
        result.append([])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i].append(countBombSurrounding([i,j],matrix))
    return result

def countBombSurrounding(coordi,matrix):
    bombCount = 0
    deepBorder = len(matrix)-1
    wideBorder = len(matrix[0])-1

    deepLow = roundToBorder(coordi[0]-1,deepBorder)
    deepHigh = roundToBorder(coordi[0]+1,deepBorder)
    wideLow = roundToBorder(coordi[1]-1, wideBorder)
    wideHigh = roundToBorder(coordi[1]+1, wideBorder)

    for deep in range(deepLow, deepHigh+1):
        for wide in range(wideLow, wideHigh+1):
            if deep == coordi[0] and wide == coordi[1]:
                 continue
            if matrix[deep][wide] == True:
                bombCount += 1
    return bombCount


def roundToBorder(num, border):
    if num < 0: return 0
    if num > border: return border
    return num
