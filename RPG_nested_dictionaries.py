# Name: Yahya Eldarieby
# Class: CS30
# Date: 14/12/2019
# Description: RPG Nested Dictionaries

from tabulate import tabulate

# The 3 players favourite colors
Player0 = {'name': "Yahya", 'description': "Black"}
Player1 = {'name': "Yusuf", 'description': "Blue"}
Player2 = {'name': "Nour",  'description': "Pink"}

# Three locations  and thier description ()
Location0 = {'x': 5, 'y': 3, 'description': "MM"}
Location1 = {'x': 4, 'y': 4, 'description': "KK"}
Location2 = {'x': 3, 'y': 5, 'description': "PP"}


# This is how items are represented on a website. I changed it to the game.
Inventory = [
    {'name': "apple", 'x_position': 0, 'y_position': 0, 'description':
        'Apples do not makeyou bigger'},
    {'name': "orange", 'x_position': 1, 'y_position': 2, 'description':
        'Oranges  make you bigger'},
    {'name': "banana", 'x_position': 3, 'y_position': 2, 'description':
        'Bananas are good  '},
    {'name': "Pole", 'x_position': 3, 'y_position': 5, 'description':
        'Poles hinder you. '},
    {'name': "Wall", 'x_position': 3, 'y_position': 5, 'description':
        'Dead End. '}
]

# PLayers favourite colors ...a print out
print ("\n Here are the players")
print ("Player| %10s| loves the color of |%10s|" %
       (Player0['name'], Player0['description']))
print ("Player| %10s| loves the color of |%10s|" %
       (Player1['name'], Player1['description']))
print ("Player| %10s| loves the color of |%10s|" %
       (Player2['name'], Player2['description']))

# Locations  ... and a print
print ("\n Here are the locations")
print ("At location| %2d| | %2d| one finds  |%10s|" %
       (Location0['x'], Location2['y'], Location0['description']))
print ("At location| %2d| | %2d| one finds  |%10s|" %
       (Location1['x'], Location2['y'], Location1['description']))
print ("At location| %2d| | %2d| one finds  |%10s|" %
       (Location2['x'], Location2['y'], Location2['description']))

# Lsit of inventory items  printed with a for loop
print("\nHere is a list of Inventory Items:\n")
for item in Inventory:
    print("|item |%10s|%2d|%2d|%30s|" %
          (item['name'], item['x_position'], item['y_position'],
           item['description']))
