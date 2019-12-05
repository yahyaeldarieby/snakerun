# Name: Yahya Eldarieby
# Class: CS30
# Date: 12/3/2019
# Description: RPG Continuous Game Play and User input

import sys
import rpg_intro_msg as rpgim
import rpg_game_map as rpggm
import rpg_snake as rpgs


#This function initializes the game. Prints a welcome message, adds fruits and obstacles and the snake to  the board.
def inititialize():    
    rpgim.welcome_msg()
    #draw_map()
    rpggm.add_fruits_obstacles()
    
    #initial snake location
    rpgs.snake_location_x =2
    rpgs.snake_location_y =12
    
    rpgs.snake_location(rpgs.snake_location_x, rpgs.snake_location_y)
    rpggm.draw_map()
    
#this is the main menu function. It initializes the game, and gets into for-ever loop to take input commands from user to move the snake
def mainMenu():
    inititialize()
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
