import sys
sys.path.append("./src")

# import main game function
from tictactoe import ticTacToe
from connect4 import connect4

# Menu
print('Choose Game\n1 : TictacToe \n2 : Connect 4')
game = int(input('Choice : '))

if (game == 1):
    ticTacToe()
elif (game == 2):
    connect4()