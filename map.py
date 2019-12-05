
# Name: Yahya Eldarieby
# Class: CS30
# Date: 11/6/2019
# Description: RPG Continuous Game Play


from tabulate import tabulate

# A grid that is 15 by 8
game_board = [
              ["0","","","","","","","","","","","","","",""],
              ["1","","","","","","","","","","","","","",""],
              ["2","","","","","","","","","","","","","",""],
              ["3","","","","","","","","","","","","","",""],
              ["4","","","","","","","","","","","","","",""],
             ]

column_headers = ["row/col","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]

def draw_map():
    
    print (tabulate  (game_board, headers= column_headers , tablefmt = "grid"))
    # Print (tabulate  (game_board, headers= column_headers , tablefmt = "grid"))