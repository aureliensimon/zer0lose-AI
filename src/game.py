def initBoard ():
    return [
        [' ', 'x', 'x'],
        [' ', '0', ' '],
        ['x', 'x', 'x']
    ]


def printBoard (board):
    for i in range (3):
        print (board[i][0], ' | ', board[i][1], ' | ', board[i][2])
        if (i != 2) : print('-------------')

def checkRow (board):
    for i in range (3):
        if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]) and (board[i][0] != ' '):
            return True
    return False

def checkColown (board):
    for i in range (3):
        if (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]) and (board[0][i] != ' '):
            return True
    return False

def checkDiagonal (board):
    return ((board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0] != ' ')) or ((board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[0][2] != ' '))

def gameOver (board):
    return checkColown(board) or checkRow(board) or checkDiagonal(board)

def printWinner (player):
    print (player, 'won')


board = initBoard()
printBoard(board)
print (gameOver(board))
