import os
from player import Player

# Creating 2 players
p1 = Player('human', 'x')
p2 = Player('zer0lose', 'o')

# Initialisation of the game board with empty char
def initBoard ():
    return [[' '] * 7 for i in range(7)]

# Print the current board
def printBoard (board):
    os.system('clear')
    for i in range(7):
        print ('| ' + board[0][6 - i] + ' | ' + board[1][6 - i] + ' | ' + board[2][6 - i] + ' | ' + board[3][6 - i] + ' | ' + board[4][6 - i] + ' | ' + board[5][6 - i] + ' | ' + board[6][6 - i] + ' | ')
        print (' ---+---+---+---+---+---+---')
    print ('  1   2   3   4   5   6   7')

# Get the index of the first empty space in a colown
def getFreeSpace (board, col):
    for i in range(7):
        if (board[col][i] == ' '):
            return i
    return None

# Put the player's tag in the board at one spot
def fillBoard (board, col, index, tag):
    board[col][index] = tag
    return board

# Check if a row is a winning one
def checkRow (board, Row, tag):
    for i in range(4):
        if (board[i][Row] == board[i + 1][Row] == board[i + 2][Row] == board[i + 3][Row]) and (board[i][Row] == tag):
            return True
    return False

# Check if a colomn is a winning one
def checkColumn (board, col, tag):
    for i in range(4):
        if (board[col][i] == board[col][i + 1] == board[col][i + 2] == board[col][i + 3]) and (board[col][i] == tag):
            return True
    return False

# Check if one of the diagonal is a winning one
def checkDiagonal (board, tag):
    for i in range(4):
        for j in range(4):
            if ((board[i][6 - j] == board[i + 1][5 - j] == board[i + 2][4 - j] == board[i + 3][3 - j]) and (board[i][6 - j] == tag)) or ((board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[3 + i][j + 3]) and (board[i][j] == tag)):
                return True
    return False

# Check if game is over
def gameOver (board, player):
    for i in range(7):
        if checkRow(board, i, player.tag) or checkColumn(board, i, player.tag): return True
    return checkDiagonal(board, player.tag)

# Check if it's a draw (no more space)
def gameDraw (board):
    for i in range(7):
        for j in range(7):
            if (board[i][j] == ' '): return False
    return True

# Start Connect 4 game
def connect4 ():
    board = initBoard()
    printBoard(board)

    # 1: p1 trun
    # 0: p2 turn
    turn = 1

    while True:

        if (turn):
            while True:
                choice = int(input())
                if (choice < 1) or (choice > 7):
                    print('Please use numpad between [1 - 7]')
                    continue
                if (getFreeSpace(board, choice - 1) != None):
                    break
                else:
                    print('Already used')
                
        else:
            while True:
                choice = int(input())
                if (choice < 1) or (choice > 7):
                    print('Please use numpad between [1 - 7]')
                    continue
                if (getFreeSpace(board, choice - 1) != None):
                    break
                else:
                    print('Already used')

        board = fillBoard(board, (choice - 1), getFreeSpace(board, choice - 1), p1.tag if turn else p2.tag)
        
        printBoard(board)
        if gameOver(board, p1 if turn else p2):
            print(p1.name if turn else p2.name, 'win')
            return
        elif gameDraw(board):
            print('Draw !')
            return

        turn = not(turn)

connect4()