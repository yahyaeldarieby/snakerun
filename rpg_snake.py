# Name: Yahya Eldarieby
# Class: CS30
# Date: 12/3/2019
# Description: sanke location and movement


import sys
import rpg_game_map as rpggm

# These are the x and y locations of the sanke
snake_location_x = 0
snake_location_y = 0

# This is the socre of the user.
score = 0


# This function places the snake on the x and y
# coordinates on the board of the game.


def snake_location(x, y):
    rpggm.game_board[x][y] = "X"

# This function moves the snake to x and y
# coordinates on the board of the game.
# It checks if the snake hits an obstacle/fruit and acts.


def move_snake(x, y):
    rpggm.game_board[snake_location_x][snake_location_y] = ""

    # Coordinates of the new location of snake
    snake_location_x = x
    snake_location_y = y
    #continue here.

