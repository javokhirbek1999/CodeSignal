def differentSquares(matrix):
    diifferent_squares = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            t = [[]]
            t[-1].append(matrix[i][j])
            t[-1].append(matrix[i][j+1])
            t.append([])
            t[-1].append(matrix[i+1][j])
            t[-1].append(matrix[i+1][j+1])
            diifferent_squares.append(t)

    re = []
    for i in diifferent_squares:
        if i not in re:
            re.append(i)
    
    return len(re)
