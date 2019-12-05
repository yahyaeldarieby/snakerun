# Name: Yahya Eldarieby
# Class: CS30
# Date: 22/10/2019
# Description: RPG Nested Dictionaries


from map.py import  game_board, column_headers, draw_map

snake_location_x = 0
snake_location_y = 0

def add_fruits():
    for x in range (1,6,1):
        game_board [x-1] [x] ="f"
    # F is for fruits that will be located on the map
    # Print (tabulate  (game_board, headers= column_headers , tablefmt = "grid"))

def add_obstacles():
    for x in range (1,6,1):
        game_board [x-1] [x*2] ="o"
    # O is for obstacles that will be located on the map
    # Print (tabulate  (game_board, headers= column_headers , tablefmt = "grid"))

def snake_location(x,y):
    game_board [x] [y] ="X"
    # The location of the snake




###########################Older code.

"""
fruits = {
    'apples': {
        'bigger': 'The apples do not make you bigger than how you started'
        'description': 'Apples do not make you bigger'
        'location': 'Black screen'
         },


     'pineapples': {
        'bigger': 'The pineapples make you twice as big than normally'
        'discription':'Pineapples make your chatacter twice as big than normally'
        'location': 'Black screen'
        },

    'oranges': {
       'bigger': 'The fruits orange will make you 3 times bigger than usual'
       'discription': 'Oranges make you 3 times bigger than your actual size'
       'location': 'Black screen'
       },

     }
    for fruits, fruits_info in fruit.items():
        print(f"\nfruits: {fruits}")
        bigger = f"{fruits_info['bigger']}"
        description = f"{fruits_info['discription']}"
        location = f"{fruits_info['location']}"

        print(f"\tbigger: {bigger.title()}")
        print(f"\tdescription: {description.title()}")
        print(f"\tlocation: {location.title()}")
"""
