import os
import sys
from math import inf
from player import Player

# Creating 2 players
p1 = Player('human', 'x')
p2 = Player('zer0lose', 'o')

# Initialisation of the game board with empty char
def initBoard ():
    return [[' '] * 6 for i in range(7)]

# Restart game
def restartGame ():
    playAgain = input('Do you want to play again ? (Y-n) : ')
    quit = (playAgain == 'N' or playAgain == 'n')
    if (quit) : sys.exit(0)

    board = initBoard()
    return board

# Print Current Score
def printScore(draw):
    print('\n', p1.name, p1.score, ' - ',draw, ' - ', p2.score, p2.name)

# Print the current board
def printBoard (board):
    os.system('clear')
    for i in range(6):
        for j in range(7):
            print ('| ' + board[j][6 - i - 1], end=' ')
        print('|')
        print(' ---+---+---+---+---+---+---')
    print ('  1   2   3   4   5   6   7')

# Get the index of the first empty space in a colown
def getFreeSpace (board, col):
    for i in range(6):
        if (board[col][i] == ' '):
            return i
    return None

# Put the player's tag in the board at one spot
def fillBoard (board, col, index, tag):
    board[col][index] = tag
    return board

# Remove the player's tag in the board at one spot
def undoFillBoard (board, col, index):
    board[col][index] = ' '
    return board

# Check if a row is a winning one
def checkRow (board, row, tag):
    for i in range(4):
        if (board[i][row] == board[i + 1][row] == board[i + 2][row] == board[i + 3][row]) and (board[i][row] == tag):
            return True
    return False

# Check if a colomn is a winning one
def checkColumn (board, col, tag):
    for i in range(3):
        if (board[col][i] == board[col][i + 1] == board[col][i + 2] == board[col][i + 3]) and (board[col][i] == tag):
            return True
    return False

# Check if one of the diagonal is a winning one
def checkDiagonal (board, tag):
    for i in range(4):
        for j in range(3):
            if ((board[i][5 - j] == board[i + 1][4 - j] == board[i + 2][3 - j] == board[i + 3][2 - j]) and (board[i][5 - j] == tag)) or ((board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[3 + i][j + 3]) and (board[i][j] == tag)):
                return True
    return False

# Check if game is over
def gameOver (board, player):
    for i in range(6):
        if checkRow(board, i, player.tag): return True
    for i in range(7):
        if checkColumn(board, i, player.tag): return True

    return checkDiagonal(board, player.tag)

# Check if it's a draw (no more space)
def gameDraw (board):
    for i in range(7):
        for j in range(6):
            if (board[i][j] == ' '): return False
    return True

# Get the other player
def getOpponent (player):
    return p1 if player == p2 else p2

# List all possible spot that the ai can play
def getAvailableMoves (board):
    moves = []
    for i in range(7):
        if (getFreeSpace(board, i) != None):
            moves.append(i)
    return moves

# Return the strength of a 4 connected area on the board (the more the better for IA)
def evalQuadruplet (q):
    score = 0

    nbX = q.count('x')
    nbO = q.count('o')

    # X and O or none of them = neutral
    if ((nbX != 0) and (nbO != 0)) or ((nbX == 0) and (nbO == 0)):
        score = 0
    
    # only X
    if (nbX != 0) and (nbO == 0):
        if (nbX == 1): score = -1
        if (nbX == 2): score = -10
        if (nbX == 3): score = -500
    
    # only O
    if (nbO != 0) and (nbX == 0):
        if (nbX == 1): score = 1
        if (nbX == 2): score = 10
        if (nbX == 3): score = 1000
        if (nbX == 4): score = 100000

    return score

def evalBoard (board):
    score = 0
    for i in range(7):
        for j in range(6):
            if (i < 4):
                # check row
                score += evalQuadruplet([board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j]])
            if (j > 2):
                # check col
                score += evalQuadruplet([board[i][j], board[i][j - 1], board[i][j - 2], board[i][j - 3]])
            if (i < 4) and (j > 2):
                # check descending diag
                score += evalQuadruplet([board[i][j], board[i + 1][j - 1], board[i + 2][j - 2], board[i + 3][j - 3]])
            if (i < 4) and (j < 3):
                # check ascending diag
                score += evalQuadruplet([board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3]])
    return score

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
        board = fillBoard(board, move, getFreeSpace(board, move), player.tag)
        result, _ = minimax(board, getOpponent(player), depth + 1)
        # Remove the current spot from the board
        if (getFreeSpace(board, move) == None):
            board = undoFillBoard(board, move, 5)
        else:
            board = undoFillBoard(board, move, getFreeSpace(board, move) - 1)

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

# Minimax algorithm
def alphabeta (board, player, maxDepth, alpha = -inf, beta = inf, depth = 0):
    # Minimize the lose, maximise the profit
    best = -100000 if getOpponent(player) != p2 else 100000
    bestMove = None

    # Check if the game is over / draw
    if depth == maxDepth:
        return evalBoard(board), None
    if gameOver(board, p1):
        return -100000 + depth, None
    elif gameDraw(board):
        return 0, None
    elif gameOver(board, p2):
        return 100000 - depth, None

    # For every possible play
    for move in getAvailableMoves(board):
        # Trying the spot
        board = fillBoard(board, move, getFreeSpace(board, move), player.tag)
        result, _ = alphabeta(board, getOpponent(player), maxDepth, alpha, beta, depth + 1)
        # Remove the current spot from the board
        if (getFreeSpace(board, move) == None):
            board = undoFillBoard(board, move, 5)
        else:
            board = undoFillBoard(board, move, getFreeSpace(board, move) - 1)

        # If if it's the ai turn
        if player == p2:
            # If the move is better than the previous one
            if result > best:
                best, bestMove = result, move
            if best >= beta:
                return best, move
            
            alpha = max(alpha, result)
        else :
            # If the move is less worse than the previous one
            if result < best:
                best, bestMove = result, move
            if best <= alpha:
                return best, move
            
            beta = min(beta, result)
            
    return best, bestMove


# Start Connect 4 game
def connect4 ():
    board = initBoard()
    printBoard(board)

    playerWantToStart = input('\nDo you want to start ? (Y-n) : ')
    turn = (playerWantToStart == 'Y' or playerWantToStart == 'y')

    scoreDraw = 0

    # How many turn the AI will compute, the higher the stronger it will be, however it can start
    # to be very slow
    predict = 6

    while True:

        printBoard(board)
        printScore(scoreDraw)

        if gameOver(board, p2 if turn else p1):
            if (turn):
                print('\n', p2.name, 'win\n')
                p2.score += 1
            else:
                print('\n', p1.name, 'win\n')
                p1.score +=1
            board = restartGame()
            continue
        elif gameDraw(board):
            print('Draw !')
            scoreDraw += 1
            board = restartGame()
            continue

        if (turn):
            while True:
                choice = int(input('\nYour choice : '))
                if (choice < 1) or (choice > 7):
                    print('Please use numpad between [1 - 7]')
                    continue
                if (getFreeSpace(board, choice - 1) != None):
                    break
                else:
                    print('Already used')
                
        else:
            #score, choice = minimax(board, p2)
            score, choice = alphabeta(board, p2, predict)
            choice = choice + 1
        
        board = fillBoard(board, (choice - 1), getFreeSpace(board, choice - 1), p1.tag if turn else p2.tag)

        turn = not(turn)