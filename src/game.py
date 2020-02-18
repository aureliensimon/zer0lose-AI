import os

def initBoard ():
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


def printBoard (board):
    for i in range (3):
        print (board[i][0], ' | ', board[i][1], ' | ', board[i][2])
        if (i != 2) : print('-------------')


def fillBoard (board, player, x, y):
    board[x][y] = player 
    return board

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
    if (player):
        name = 'Aurel'
    else:
        name = 'zer0lose'

    print (name, 'won')


def ticTacToe ():
    board = initBoard()
    
    # 1: human trun
    # 0: computer turn
    turn = 1

    while True:
        os.system('clear')
        printBoard(board)
        
        if (gameOver(board)):
            printWinner(turn)
            return

        if (turn):
            humanChoice = input()
            if (len(humanChoice) > 1) or (48 > ord(humanChoice)) or (58 < ord(humanChoice)):
                print('Please use numpad')

            board = fillBoard(board, 'x', 2 - int((int(humanChoice) - 1) / 3), int((int(humanChoice) - 1) % 3))

ticTacToe()