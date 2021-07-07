def sudoku(grid):
    
    for i in range(len(grid)):
        if validRow(grid,i) == False:
            return False
    
    for i in range(len(grid)):
        if validCol(grid,i) == False:
            return False
    
    for row in range(0,len(grid),3):
        for col in range(0,len(grid),3):
            if validSubGrid(grid,row,col) == False:
                return False
    return True
            
    


def validRow(grid,row):
    checked = []
    for i in range(len(grid)):
        if grid[row][i] in checked:
            return False
        else:
            checked.append(grid[row][i])
    return True

def validCol(grid,col):
    checked = []
    for i in range(len(grid)):
        if grid[i][col] in checked:
            return False
        else:
            checked.append(grid[i][col])
    return True

def validSubGrid(grid,startRow,startCol):
    checked = []
    for row in range(3):
        for col in range(3):
            box_val = grid[startRow+row][startCol+col]
            if box_val in checked:
                return False
            else:
                checked.append(box_val)
    return True
