# Name: Yahya Eldarieby
# Class: CS30
# Date: 11/6/2019
# Description: RPG Continuous Game Play


import sys


def mainMenu():
    while True:
        print("1. Start")
        print("2. How to play")
        print("3. Quit")
        selection = int(input("Enter a choice 'number' below: "))
        if selection == 1:
            start()
        elif selection == 2:
            play()
        elif selection == 3:
            print("Quitting......... ")
            sys.exit()
        else:
            print("Invalid choice. Enter 1-3")


def play():
    print("How to Play: type any of the four directions listed")


def start():
    print("Start ...... ")

    fruits = ['*apples', '*pineapples', '*blueberry', '*oranges']
    directions = ['right', 'left', 'up', 'down']

    print("THE FOLLOWING FRUITS MAKE YOU BIGGER OR SMALLER ")
    for fruit in fruits:
        print(fruit.title())

    print("GO IN THE FOLLOWING DIRECTIONS:")
    for direction in directions:
        print(direction.title())

    while True:
        user_command = input("your decision of moving:")
        x = 0
        for direction in directions:
            x += 1
            if user_command == 'q':
                return
            elif direction == user_command:
                    print (fruits[x-1])


mainMenu()
