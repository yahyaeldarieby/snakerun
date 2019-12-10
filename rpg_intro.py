# Name: Yahya Eldarieby
# Class: CS30
# Date: 12/3/2019
# Description: welcome message and instructions to play game

import pyfiglet
import rpg_game_map as rpg_map
import rpg_snake as rpgs

# This function is taken from the Internet.
# I changed parts of it to suit this project.
# A nice print of my name.


def welcome_msg():
    print(pyfiglet.figlet_format("Y. Eldarieby", font="slant"))

    msg = """
    Rules:
      1. This is a simple text based snake game.
      Below is the board of the game.
      The "f" stands for fruits, the "o" stands for obstacles,
      the "X" is where the snake is.
      2. Type 5 to quit at any time.
      3. Type 1,2,3, 4 to move the snake
      4. If the snake hits an obstacle: the game will end.
      5. If the snake eats a fruit:
      the snake gets longer and the score increases.
    """
    print(msg)

# This function initializes the game and prints a welcome message,
# Adds fruits and obstacles and the snake to the board.


def initialize():
    welcome_msg()
    # rpg_map.draw_map()

    # Add fruits and obstacles to an empty map
    rpg_map.add_fruits_obstacles()

    # Initial snake location on map
    # Can change this to have the user select initial location
    rpgs.snake_location(2, 12)

    rpg_map.draw_map()

# Welcome_msg()
