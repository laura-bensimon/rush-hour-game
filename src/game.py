from board import Board
from car import Car
from helper import *
import sys
import helper

class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code and erase the "pass"
        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code and erase the "pass"
        user_input = input("Choose a color and a direction: ")
        space = ','
        direction = 'udlr'
        color = 'RGWOBY'

        if user_input == '!':
            print("You left the Game")
            exit(0)
        if len(user_input) != 3:
            print("This is not a correct input")
            return
        if user_input[0] not in color:
            print("This color doesn't exist")
            return
        if user_input[2] not in direction:
            print("This direction doesn't exist")
            return
        if user_input[1] != space:
            print("This is not a correct input")
            return
        if not self.board.move_car(user_input[0], user_input[2]):
            print("Invalid move")


    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code and erase the "pass"

        while self.board.cell_content((3, 7)) is None:
            print(self.board)
            self.__single_turn()
        print('You won!!')
        print(self.board)


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    # implement your code and erase the "pass"

    cars = helper.load_json(sys.argv[1])
    board = Board()
    possible_colors = 'RGWOBY'
    directions = [1,0]
    for name in cars:

        car2add = Car(name, cars[name][0], cars[name][1], cars[name][2])
        if not (2 <= car2add.length <= 4):
            continue
        cond1 = 0 <= car2add.location[0] <= 6
        cond2 = 0 <= car2add.location[1] <= 6
        if not cond1 or not cond2:
            continue
        if car2add.name in possible_colors and car2add.orientation in directions:
            board.add_car(car2add)

    game = Game(board)
    game.play()
