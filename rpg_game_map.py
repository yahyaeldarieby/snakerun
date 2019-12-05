# Name: Yahya Eldarieby
# Class: CS30
# Date: 12/4/2019
# Description: Map and fruits and vegetable layout.


from tabulate import tabulate


#This is the boad of the game.  empty strings mean empty cells on the board
game_board = [["1","","","","","","","","","","","","","",""],
              ["2","","","","","","","","","","","","","",""],
              ["3","","","","","","","","","","","","","",""],
              ["4","","","","","","","","","","","","","",""],
              ["5","","","","","","","","","","","","","",""],
             ]

# this variable is used by tabulate to print a header for the board of the game
column_headers = ["row/col","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]


#this function just draws the board of the game
def draw_map():
    print (tabulate  (game_board, headers= column_headers , tablefmt = "grid"))
    
    
#this function adds fruits and obstacles to the board of the game. 
def add_fruits_obstacles():  
    for x in range (1,6,1):
        game_board [x-1] [x] ="f"  
    for x in range (1,6,1):
        game_board [x-1] [x*2] ="o" 