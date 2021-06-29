

def chessKnight(cell):
    letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    numbers = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7}
    
    board = [
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
    ]
    
    available_movements = 0


    if 0<=int(letters[cell[0]])+2 < len(board) and 0<=int(numbers[cell[1]])+1<len(board[0]):
       available_movements += 1
   
    if 0<=int(letters[cell[0]])+2 < len(board) and 0<=int(numbers[cell[1]])-1 < len(board[0]):
        available_movements+=1
    
    if 0<=int(letters[cell[0]])+1 < len(board) and 0<=int(numbers[cell[1]])+2 < len(board[0]):
        available_movements += 1
    
    if 0<=int(letters[cell[0]])+1 < len(board) and 0<=int(numbers[cell[1]])-2 < len(board[0]):
        available_movements += 1

    if 0<=int(letters[cell[0]])-1 < len(board) and 0<=int(numbers[cell[1]])+2 < len(board[0]):
        available_movements += 1
    
    if 0<=int(letters[cell[0]])-1 < len(board) and 0<=int(numbers[cell[1]])-2 < len(board[0]):
        available_movements += 1
    
    if 0<=int(letters[cell[0]])-2 < len(board) and 0<=int(numbers[cell[1]])+1 < len(board[0]):
        available_movements += 1

    if 0<=int(letters[cell[0]])-2 < len(board) and 0<=int(numbers[cell[1]])-1 < len(board[0]):
       available_movements += 1


    return available_movements
