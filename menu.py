# Name: Yahya Eldarieby
# Class: CS30
# Date: 11/6/2019
# Description: RPG Continuous Game Play


# I took this code mostly from Internet and changed it to my game.

import pyfiglet

# Welcome message 
def welcome_msg():
    
    print(pyfiglet.figlet_format("Y. Eldarieby", font = "slant"  ))
    msg = """
    Rules:
      1. This is a simple text based snake game.
      2. Type q to quit at any time.
      3. Type up, down, right, or left to move the snake
      4. if the snake hits an obstacle: 
      5. if the snake eats a fruit: 
    """
    print(msg)
