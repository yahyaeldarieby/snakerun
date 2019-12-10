# Name: Yahya Eldarieby
# Class: CS30
# Date: 12/3/2019
# Description: RPG Continuous Game Play and User input

import sys
import rpg_intro as intro

# This is the main menu function.
# It initializes the game, and gets into for-ever loop to take input
# commands from user in order to move the snake


def mainMenu():
    intro.initialize()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    
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
