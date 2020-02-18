import os
from player import Player

p1 = Player('Aurel', 'x')
p2 = Player('zer0lose', 'o')

def initBoard ():
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

def printBoard (board):
    print(' ')
    for i in range (3):
        print (board[i][0], ' | ', board[i][1], ' | ', board[i][2])
        if (i != 2) : print('-------------')
    print(' ')

def fillBoard (board, player, x, y):
    board[x][y] = player.tag
    return board

def undoFillBoard (board, x, y):
    board[x][y] = ' '
    return board

def checkRow (board, tag):
    for i in range (3):
        if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]) and (board[i][0] == tag):
            return True
    return False

def checkColown (board, tag):
    for i in range (3):
        if (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]) and (board[0][i] == tag):
            return True
    return False

def checkDiagonal (board, tag):
    return ((board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0] == tag)) or ((board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[0][2] == tag))

def gameOver (board, player):
    return checkColown(board, player.tag) or checkRow(board, player.tag) or checkDiagonal(board, player.tag)

def freeBoard (board, x, y):
    return (board[x][y] == ' ')

def gameDraw (board):
    for i in range (3):
        for j in range (3):
            if (board[i][j] == ' '):
                return False
    return True

def getOpponent (player):
    return p1 if player == p2 else p2

def getAvailableMoves (board):
    moves = []
    for i in range(1, 10):
        if (freeBoard(board, 2 - int((i - 1) / 3), int((i - 1) % 3))):
            moves.append(i)
    return moves

def minimax (board, player, depth = 0):
    best = -10 if getOpponent(player) != p2 else 10
    bestMove = None

    if gameOver(board, p1):
        return -10 + depth, None
    elif gameDraw(board):
        return 0, None
    elif gameOver(board, p2):
        return 10 - depth, None

    for move in getAvailableMoves(board):
        board = fillBoard(board, player, 2 - int((move - 1) / 3), int((move - 1) % 3))
        result, _ = minimax(board, getOpponent(player), depth + 1)
        board = undoFillBoard(board, 2 - int((move - 1) / 3), int((move - 1) % 3))

        if player == p2:
            if result > best:
                best, bestMove = result, move
        else :
            if result < best:
                best, bestMove = result, move

    return best, bestMove

def ticTacToe ():
    board = initBoard()
    
    # 1: p1 trun
    # 0: p2 turn
    turn = 1

    score = None
    while True:
        os.system('clear')
        printBoard(board)
        
        if gameOver(board, p2 if turn else p1):
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
            score, choice = minimax(board, p2)

        board = fillBoard(board, p1 if turn else p2, 2 - int((int(choice) - 1) / 3), int((int(choice) - 1) % 3))
        
        turn = not(turn)