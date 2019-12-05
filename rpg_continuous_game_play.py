# Name: Yahya Eldarieby
# Class: CS30
# Date: 11/6/2019
# Description: RPG Continuous Game Play




import sys

#from rpg_nested_dictionaries.py import  add_fruits(), add_obstacles(), snake_location()
from rpg_nested_dictionaries.py import  *
from menu.py import *


def inititialize(): 
    welcome_msg()
    # draw_map()
    add_fruits()
    add_obstacles()
    draw_map()
    
    # Initial snake location
    snake_location_x =2
    snake_location_y =12
    
    snake_location(snake_location_x, snake_location_y)
    draw_map()
    

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
           print("Invalid choice. Enter 1-3")
           
    # The option of moving to any of the four directions and quitting the system
    




