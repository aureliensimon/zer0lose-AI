import os
import random

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

def freeBoard (board, x, y):
    return (board[x][y] == ' ')

def gameDraw (board):
    for i in range (3):
        for j in range (3):
            if (board[i][j] == ' '):
                return False
    return True

def ticTacToe (p1, p2):
    board = initBoard()
    
    # 1: p1 trun
    # 0: p2 turn
    turn = 1

    while True:
        os.system('clear')
        printBoard(board)
        
        if gameOver(board):
            print(p2.name if turn else p1.name, 'win')
            return
        elif gameDraw(board):
            print('Draw !')
            return

        if (turn):
            while True:
                choice = input()
                if (len(choice) > 1) or (48 > ord(choice)) or (58 < ord(choice)):
                    print('Please use numpad')
                    return
                if (freeBoard(board, 2 - int((int(choice) - 1) / 3), int((int(choice) - 1) % 3))):
                    break
                else:
                    print('Already used')
                
        else:
            while True:
                choice = random.randrange(10)
                if (freeBoard(board, 2 - int((int(choice) - 1) / 3), int((int(choice) - 1) % 3))):
                    break

        board = fillBoard(board, 'x' if turn else 'o', 2 - int((int(choice) - 1) / 3), int((int(choice) - 1) % 3))
        
        turn = not(turn)
