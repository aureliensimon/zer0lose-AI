def getAvailableMoves (board):
    moves = []
    for i in range(1, 10):
        if (freeBoard(board, 2 - int((i - 1) / 3), int((i - 1) % 3))):
            moves.append(i)
    return moves

def minimax (board, player, depth = 0):
    best = -10 if getOpponent(player) != p2 else 10
    bestMove = None

    if gameOver(board, getOpponent(player)):
        return -10 + depth, None
    elif gameDraw(board):
        return 0, None
    elif gameOver(board, player):
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