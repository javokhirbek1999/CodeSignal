def spiralNumbers(n):
    matrix = [[0]*n for i in range(n)]

    mx, my = [0, 1, 0, -1], [1, 0, -1, 0]
    x,y,c = 0, -1, 1

    for i in range(n+n-1):
        for j in range((n+n-i)//2):
            x += mx[i%4]
            y += my[i%4]
            matrix[x][y] = c
            c += 1
    
    return matrix
