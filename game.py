import sys
sys.path.append("./src")

# import main game function
from tictactoe import ticTacToe
from connect4 import connect4

# Menu
print('Choose Game\n1 : TictacToe \n2 : Connect 4')
game = int(input('Choice : '))

if (game == 1):
    # Tutorial how to play
    print('\nTo place a token where you want to play, give the number following this representation of the game grid :\n(for example if you want to play in the center you will have to type the number 5)\n\n')
    for i in range (3):
        print(7 - i*3, ' | ', 8 - i*3, ' | ', 9 - i*3)
        if (i != 2) : print('-------------')
    print('\n')
    
    ticTacToe()
elif (game == 2):
    connect4()