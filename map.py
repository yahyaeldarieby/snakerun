# Name: Yahya Eldarieby
# Class: CS30
# Date: 11/06/2019
# Description: RPG Modules and Maps


from tabulate import tabulate
import pyfiglet
import sys


game_board = [
              ["", "o", "", "", "", "", "f", "", "", "", "", "", "", ""],
              ["", "", "", "", "f", "", "", "", "", "", "", "", "", ""],
              ["", "o", "", "", "", "", "f", "", "", "", "", "", "", ""],
              ["", "", "", "f", "", "", "", "", "", "", "", "", "", ""],
              ["", "", "", "", "f", "", "o", "", "", "", "", "", "", ""],
             ]


def welcome_msg():
    print (pyfiglet.figlet_format("Yahya", font="slant"))
    msg = """
    Rules:
    1. This is a simple text based snake game.
    2. Type q to quit at any time.
    3. Type up, down, right, or left to move the snake
    4. if the snake hits an obstacle:
    5. if the snake eats a fruit:
    """
    print(msg)


def draw_map():
    global game_board
    print(tabulate(game_board, tablefmt="grid"))


def inititialize():
    welcome_msg()
    draw_map()


def mainMenu():
    # fruits = ['*apples', '*pineapples', '*blueberry', '*oranges']
    # directions = ['right', 'left', 'up', 'down']
    # print("THE FOLLOWING FRUITS MAKE YOU BIGGER OR SMALLER ")
    # print (fruits)
    # print("GO IN THE FOLLOWING DIRECTIONS:")
    # print (directions)

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


inititialize()
mainMenu()
