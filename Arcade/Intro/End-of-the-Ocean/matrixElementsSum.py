def matrixElementsSum(matrix):
    r = 0
    for i in range(1, len(matrix)):
        for k in range(len(matrix[i-1])):
            if matrix[i-1][k] == 0:
                matrix[i][k] = 0
    for i in matrix:
        r += sum(i)
    return r 
