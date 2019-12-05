# Name: Yahya Eldarieby
# Class: CS30
# Date: 12/3/2019
# Description: welcome message and instructions to play game

import pyfiglet

def welcome_msg():
    #this function is  taken from Internet. I changed parts of it to suit this project
    # a nice print of my name ...
    print(pyfiglet.figlet_format("Y. Eldarieby", font = "slant"  ))
    
    msg = """
    Rules:
      1. This is a simple text based snake game. Below is the board of the game. The "f" means a fruit, the "o" means an obstacle,
      the "X" is where the snake is.
      2. Type 5 to quit at any time.
      3. Type 1,2,3, 4 to move the snake
      4. if the snake hits an obstacle: the game will end.
      5. if the snake eats a fruit: the snake gets longer and the score increases.
    """
    print(msg)
    
    
    