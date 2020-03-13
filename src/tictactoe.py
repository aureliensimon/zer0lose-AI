import os
from player import Player

# Creating 2 players
p1 = Player('human', 'x')
p2 = Player('zer0lose', 'o')

# Initialisation of the game board with empty char
def initBoard ():
    return [
        [[' '] * 3 for i in range(3)]

# Print the current board
def printBoard (board):
    os.system('clear')
    for i in range (3):
        print (board[i][0], ' | ', board[i][1], ' | ', board[i][2])
        if (i != 2) : print('-------------')

# Put the player's tag in the board at one spot
def fillBoard (board, player, x, y):
    board[x][y] = player.tag
    return board

# Delete the player's tag from the board at one spot
def undoFillBoard (board, x, y):
    board[x][y] = ' '
    return board

# Check if a row is a winning one
def checkRow (board, tag):
    for i in range (3):
        if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]) and (board[i][0] == tag):
            return True
    return False

# Check if a colomn is a winning one
def checkColown (board, tag):
    for i in range (3):
        if (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]) and (board[0][i] == tag):
            return True
    return False

# Check if a diagonal is a winning one
def checkDiagonal (board, tag):
    return ((board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0] == tag)) or ((board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[0][2] == tag))

# Check if game is over
def gameOver (board, player):
    return checkColown(board, player.tag) or checkRow(board, player.tag) or checkDiagonal(board, player.tag)

# Check if the location if empty or not
def freeBoard (board, x, y):
    return (board[x][y] == ' ')

# Check if it's a draw (no more space)
def gameDraw (board):
    for i in range (3):
        for j in range (3):
            if (board[i][j] == ' '):
                return False
    return True

# Get the other player
def getOpponent (player):
    return p1 if player == p2 else p2

def getX (num):
    return 2 - int((num - 1) / 3)

def getY (num):
    return int((num - 1) % 3)

# List all possible spot that the ai can play
def getAvailableMoves (board):
    moves = []
    for i in range(1, 10):
        if (freeBoard(board, getX(i), getY(i))):
            moves.append(i)
    return moves

# Minimax algorithm
def minimax (board, player, depth = 0):
    # Minimize the lose, maximise the profit
    best = -10 if getOpponent(player) != p2 else 10
    bestMove = None

    # Check if the game is over / draw
    if gameOver(board, p1):
        return -10 + depth, None
    elif gameDraw(board):
        return 0, None
    elif gameOver(board, p2):
        return 10 - depth, None

    # For every possible play
    for move in getAvailableMoves(board):
        # Trying the spot
        board = fillBoard(board, player, getX(move), getY(move))
        result, _ = minimax(board, getOpponent(player), depth + 1)
        # Remove the current spot from the board
        board = undoFillBoard(board, getX(move), getY(move))

        # If if it's the ai turn
        if player == p2:
            # If the move is better than the previous one
            if result > best:
                best, bestMove = result, move
        else :
            # If the move is less worse than the previous one
            if result < best:
                best, bestMove = result, move

    return best, bestMove

# Start Tic Tac Toe game
def ticTacToe ():
    board = initBoard()
    
    # 1: p1 trun
    # 0: p2 turn
    turn = 1

    score = None
    while True:
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
                if (len(choice) != 1) or (49 > ord(choice)) or (58 < ord(choice)):
                    print('Please use numpad')
                    continue
                if (freeBoard(board, getX(int(choice)), getY(int(choice)))):
                    break
                else:
                    print('Already used')
                
        else:
            score, choice = minimax(board, p2)

        board = fillBoard(board, p1 if turn else p2, getX(int(choice)), getY(int(choice)))
        turn = not(turn)
