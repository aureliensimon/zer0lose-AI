import os
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

def checkRow (board, Row, tag):
    for i in range(4):
        if (board[i][Row] == board[i + 1][Row] == board[i + 2][Row] == board[i + 3][Row]) and (board[i][Row] == tag):
            return True
    return False

def checkColumn (board, col, tag):
    for i in range(4):
        if (board[col][i] == board[col][i + 1] == board[col][i + 2] == board[col][i + 3]) and (board[col][i] == tag):
            return True
    return False

def checkDiagonal (board, tag):
    for i in range(4):
        for j in range(4):
            if ((board[i][6 - j] == board[i + 1][5 - j] == board[i + 2][4 - j] == board[i + 3][3 - j]) and (board[i][6 - j] == tag)) or ((board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[3 + i][j + 3]) and (board[i][j] == tag)):
                return True
    return False

def gameOver (board, player):
    for i in range(7):
        if checkRow(board, i, player.tag) or checkColumn(board, i, player.tag): return True
    return checkDiagonal(board, player.tag)

def gameDraw (board):
    for i in range(7):
        for j in range(7):
            if (board[i][j] == ' '): return False
    return True

b = initBoard()

# tests
b[2][2] = 'x'
b[3][3] = 'x'
b[4][4] = 'x'
b[5][5] = 'x'
b[4][2] = 'o'
b[5][1] = 'o'
b[6][0] = 'o'

fillBoard(b, 0, 'P')
printBoard(b)
print(gameOver(b, p1))

