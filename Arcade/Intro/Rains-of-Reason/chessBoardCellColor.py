def chessBoardCellColor(cell1, cell2):
    letters = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
    numbers = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
    
    board = [[1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1]]
    return board[letters[cell1[0]]][numbers[cell1[1]]]==board[letters[cell2[0]]][numbers[cell2[1]]]

# O(1) Solution
