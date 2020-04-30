import os

SIZE = 9

# Initialisation of the game board with empty char
def initBoard ():
    # return [[' '] * SIZE for i in range(SIZE)]

    return [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 1, 4, 3, 6, 5, 8, 9, 7],
        [3, 6, 5, 8, 9, 7, 2, 1, 4],
        [8, 9, 7, 2, 1, 4, 3, 6, 5],
        [5, 3, 1, 6, 4, 2, 9, 7, 8],
        [6, 4, 2, 9, 7, 8, 5, 3, 1],
        [9, 7, 8, 5, 3, 1, 6, 4, 2]
    ]

# Print the current board
def printBoard (board):
    os.system('clear')
    print(' -----------╦-----------╦-----------')
    for i in range(SIZE):
        for j in range(SIZE):
            if not(j % 3) and (j != 0):
                print('║ ' + str(board[i][j]), end=' ')
            else:
                print('| ' + str(board[i][j]), end=' ')
        print('|')
        if not((i + 1) % 3):
            if (i == SIZE - 1):
                print(' -----------╩-----------╩-----------')
            else:
                print(' ═══════════╬═══════════╬═══════════')
        else :
            print(' ---+---+---║---+---+---║---+---+---')


# Check if a row is a valid one
def checkLine (board, row):
    print(board[0][row])
    #return (sum(board[i][board] for i in range(SIZE)) == 45)

b = initBoard()
printBoard(b)
checkLine(b, 0)