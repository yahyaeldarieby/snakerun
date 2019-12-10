# Name: Yahya Eldarieby
# Class: CS30
# Date: 12/2/2019
# Description: RPG Continuous Game Play with classes

import sys
from tabulate import tabulate
import pyfiglet


# This function is  taken from Internet.
# I changed parts of it to suit this project
# A nice print of my name
def welcome_msg():
    print(pyfiglet.figlet_format("Y. Eldarieby", font="slant"))

    msg = """
    Rules:
    1. This is a simple text based snake game. Below is the board of the game.
        The "f" means a fruit, the "o" means an obstacle,
        the "X" is where the snake is.
    2. Type 5 to quit at any time.
    3. Type 1,2,3, 4 to move the snake
    4. If the snake hits an obstacle: the game will end.
    5. If the snake eats a fruit: the snake
        gets longer and the score increases.
    """
    print(msg)

############################################################


class GameMap:
    def __init__(self, gb):
        self.game_board = gb

        # This function just draws the board of the game
    def draw_map(self):
        # This variable is used by tabulate
        # to print a header for the board of the game
        print (tabulate(self.game_board, tablefmt="grid"))

    # This function adds an inventory item (fruit or obstacle)
    # on the  board of the game.

    def add_inventory_item(self, item):
        x, y = item.get_coordinates()
        self.game_board[x][y] = 'I'

    # This function initialize the sanke on the  board of the game.
    def add_snake(self, snake1):
        x, y = snake1.get_coordinates()
        self.game_board[x][y] = 'X'


############################################################
class Snake:
    def __init__(self, x, y):
        # These are the x and y locations of the sanke
        self.location_x = x
        self.location_y = y

    def get_coordinates(self):
        return self.location_x, self.location_y

############################################################
        # This class defines Inventory items.
        # It is similar to the Car class example
        # in the Python CrashCourse book.


class Inventory:
    """Represent aspects of an inventory."""
    def __init__(self, x, y):
        self.location_x = x
        self.location_y = y

    def get_descriptive_name(self):
        name = 'item at:' + str(self.location_x) + ' ' + str(self.location_y)
        return name.title()

    def get_coordinates(self):
        return self.location_x, self.location_y

# This is the main menu function.
# It initializes the game, and gets into for-ever loop
# to take input commands from user in order to move the snake


def mainMenu():
    # Prints a welcome message
    welcome_msg()
    # This is the boad of the game. Empty strings mean empty cells on the board
    game_board1 = [
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                ]
    # Now convert the board game into classes
    game_map1 = GameMap(game_board1)

    # Create a snake
    snake2 = Snake(2, 2)
    game_map1.add_snake(snake2)

    # Create and add fruits and obstacles and the snake to  the board.
    item1 = Inventory(1, 2)
    print("this is the first inventory " + item1.get_descriptive_name())
    game_map1.add_inventory_item(item1)

    item2 = Inventory(4, 2)
    print("this is the second inventory " + item2.get_descriptive_name())
    game_map1.add_inventory_item(item2)
    item3 = Inventory(2, 3)
    print("this is the third inventory " + item3.get_descriptive_name())
    game_map1.add_inventory_item(item3)

    # Display the map
    game_map1.draw_map()

############################################################

    # for ever loop for playing the game ...  get user input
    while True:

        selection = int(input("Enter a choice 'number' below: "))
        if selection == 1:
            print("Command up......... ")
        elif selection == 2:
            print("Command down......... ")
        elif selection == 3:
            print("Command right......... ")
        elif selection == 4:
            print("Command left......... ")
        elif selection == 5:
            print("Quitting......... ")
            sys.exit()
        else:
            print("Invalid choice. Enter 1-5")


mainMenu()
