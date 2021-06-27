def bishopAndPawn(bishop, pawn):
    letters = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    numbers = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
    if bishop[0] == pawn[0]:
        return False
    board = [
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1]
            ]
    return board[letters[bishop[0]]][numbers[bishop[1]]]==board[letters[pawn[0]]][numbers[pawn[1]]]
