# Name: Yahya Eldarieby
# Class: CS30
# Date: 12/3/2019
# Description: sanke location and movement



import sys
import rpg_game_map as rpggm

#these are the x and y locations of the sanke
snake_location_x = 0
snake_location_y = 0

#this is thesocre of the user.
score=0


#this function places the snake on the x and y coordinates on the board of the game. 
def snake_location(x,y):
    rpggm.game_board [x] [y] ="X"
 
#this function moves the snake to x and y coordinates on the board of the game.
#it checks if the snake hists an obstacle/fruit and acts.
def move_snake (x,y):
    rpggm.game_board [snake_location_x] [snake_location_y] =""
    
    #coordinates of the new location of snake
    snake_location_x =x
    snake_location_y =y
    
    #This is the code if the snake hits an obstacle
    if (rpggm.game_board [snake_location_x] [snake_location_y] == "o"):
        print ("you hit an obstacle. Your score is %d" %(score))
        print("Quitting......... ")
        sys.exit()
    #This is the code if the snake eats a fruit    
    elif(rpggm.game_board [snake_location_x] [snake_location_y] =="f"):
        print ("you ate a fruit")
        score +=10
    ##This is the code if the snake moves to an empty cell
    else:
        print ("safe move: score increased")
        score+=1
        rpggm.game_board [snake_location_x] [snake_location_y] ="X"
        