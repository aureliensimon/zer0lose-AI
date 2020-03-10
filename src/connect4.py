import os
import numpy as np
from player import Player

# Creating 2 players
p1 = Player('human', 'x')
p2 = Player('zer0lose', 'o')

def initBoard ():
    return [[' '] * 7 for i in range(7)]

def printBoard (board):
    for i in range(7):
        print ('| ' + board[0][6 - i] + ' | ' + board[1][6 - i] + ' | ' + board[2][6 - i] + ' | ' + board[3][6 - i] + ' | ' + board[4][6 - i] + ' | ' + board[5][6 - i] + ' | ' + board[6][6 - i] + ' | ')
        print (' ---+---+---+---+---+---+---')
    print ('  0   1   2   3   4   5   6')

def getFreeSpace (board, col):
    for i in range(7):
        if (board[col][i] == ' '):
            return i
    return None

def fillBoard (board, col, tag):
    index = getFreeSpace(board, col)
    if (index == None):
        print('Full')
        return
    else:
        board[col][index] = tag

def checkLine (board, line, tag):
    for i in range(4):
        if (board[i][line] == board[i + 1][line] == board[i + 2][line] == board[i + 3][line]) and (board[i][line] == tag):
            return True
    return False

def checkColumn (board, col, tag):
    for i in range(4):
        if (board[col][i] == board[col][i + 1] == board[col][i + 2] == board[col][i + 3]) and (board[col][i] == tag):
            return True
    return False

def checkDiagonal (board, tag):
    # Upper diag
    for i in range(4):
        for j in range(4):
            if ((board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[3 + i][j + 3]) and (board[i][j] == tag)) or ((board[6 - i][6 - j] == board[5 - i][5 - j] == board[4 - i][4 - j] == board[3 - i][board[3 - j]]) and (board[6 - i][6 - j] == tag)):
                return True
    return False

b = initBoard()
b[0][0] = 'x'
b[0][1] = 'x'
b[0][2] = 'x'
b[0][3] = 'x'
b[0][4] = 'x'
b[0][5] = 'x'
b[0][6] = 'x'

b[1][1] = 'x'
b[2][2] = 'x'
b[3][3] = 'x'
b[6][0] = 'o'
b[6][1] = 'o'
b[6][2] = 'o'
b[6][3] = 'o'

b[1][0] = 'x'
b[2][0] = 'x'
b[3][0] = 'x'

printBoard(b)
fillBoard(b, 0, 'P')
print(checkLine(b, 0, 'x'))
print(checkColumn(b, 6, 'o'))
print(checkDiagonal(b, 'x'))

