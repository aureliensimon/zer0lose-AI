# zer0lose

Artificial intelligence playing tic tac toe and connect4 using minimax algorithm optimised by alpha beta prunning.

## How to play
`
$ > python3 game.py
`
<br><br>
You are allow to play only with numeric value between 1 and 9, the numpad is the representation of the tic tac toe grid like so

|     |     |   |
| ------------- |-------------| -----|
| 7 | 8 | 9 |
| 4 | 5 | 6 |
| 1 | 2 | 3 |

<br>

## Minimax algorithm

Minimax algorithm calculate the minimax decision at a current state and try to find the optimal move for a player, assuming that your opponent also plays optimally.
It use a backtracking-like method, doing a simple recursive call developping all leaf of the tree, pushing up these values level by level. Minimax explore (DFS Depth First Search) the tree.

Here is a visual exemple of how minimax works
![minimax](https://github.com/aureliensimon/zer0lose/blob/master/img/ZXEdz.png)

Pseudo-code of minimax :

```
function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value
        

minimax(origin, depth, TRUE)
```

Now that minimax is working fine, the program can find the optimal solution *almost* instantaneous **EXECPT** when the IA is playing the first move, it takes an average of 4.565382957458496s to find the best solution, but does it really need to calculate every game possible before finding the best option ? No, so we are going to need to optimise minimax

<br><br>
## Alpha Beta prunning
1956, John McCarthy is presiding Dartmouth's conference, in which he presents alpha-beta prunning, that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. Such moves need not be evaluated further. When applied to a standard minimax tree, it returns the same move as minimax would, but prunes away branches that cannot possibly influence the final decision.

Visual explanation of alpha-beta prunning
![abprunning](https://github.com/aureliensimon/zer0lose/blob/master/img/abprunning.png)

Pseudo-code of alpha-beta prunning

```
function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            α := max(α, value)
            if α ≥ β then
                break (* β cut-off *)
        return value
    else
        value := +∞
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            β := min(β, value)
            if α ≥ β then
                break (* α cut-off *)
        return value
```

Now, let's compare efficiency of both minimax and alpha-beta prunning when the IA is doing the first move

| algorithm        | time (s)           |
| ----------- |:----------:|
| minimax     | 4.565382957458496 |
| alpha-beta prunning      | 0.206006288528442      |

As you can see alpha-beta prunning is more than **22 times** more efficient, and this is only for game with 3x3 or 7x7 board, this optimisation is even more important in chess engine.
