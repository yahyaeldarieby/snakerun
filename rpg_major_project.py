# Name: Yahya Eldarieby
# Class: CS30
# Date: 12/4/2019
# Description: Map and fruits layout.

### Taken from the internet @ https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-i/tutorial/

import sys
from tabulate import tabulate
import pyfiglet
atBorders = 0

############################################################
class Snake:
	def __init__(self, snake_location_x, snake_location_y):
     	#these are the x and y locations of the sanke
    	self.snake_location_x = snake_location_x
    	self.snake_location_y = snake_location_y

	def snake_location(self, x,y):
    	return  self.snake_location_x, self.snake_location_y

	def get_coordinates(self):
    	return  self.snake_location_x, self.snake_location_y

	def move (self, x,y):
    	#coordinates of the new location of snake
    	self.snake_location_x =x
    	self.snake_location_y =y

############################################################
class GameMap:
	def __init__(self, game_board):
    	#This is the boad of the game.  empty strings mean empty cells on the board
    	self.game_board = game_board
    	self.score =0

	#this function just draws the board of the game
	def draw_map(self):
    	# this variable is used by tabulate to print a header for the board of the game
    	column_headers = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14", "15","16","17","18","19"]
    	print (tabulate  (self.game_board, headers= column_headers , tablefmt = "grid"))
    	#print (tabulate  (self.game_board , tablefmt = "grid"))

	def add_start_tile(self, x,y):
    	self.game_board [x][y] = 'START'

	def add_goal_tile(self, x,y):
    	self.game_board [x][y] = 'GOAL'

	def clear_tile(self, x,y):
    	self.game_board [x][y] = ''

	#this function initialize the sanke on the  board of the game.
	def add_snake(self, snake1):
    	x, y= snake1.get_coordinates()
    	self.game_board [x][y] = 'X'

	#this function adds an inventory item (fruit or obstacle) on the  board of the game.
	def add_inventory_item (self, item):
    	x, y= item.get_coordinates()
    	self.game_board [x][y] = 'I'
	#this function adds fruits and obstacles to the board of the game.
	def add_fruit (self, item):
    	x, y= item.get_coordinates()
    	self.game_board [x][y] = 'F'

	def add_obstacle (self, item):
    	x, y= item.get_coordinates()
    	self.game_board [x][y] = 'O'

	def check_move(self, x,y):
    	value = ((self.game_board [x] [y])).upper()
    	if ( value ==  "O"):
        	print ('\033[91m' + "you hit an obstacle. WoW. Quitting ..... Your score is %d " %(self.score) + '\033[0m' )
        	self.game_board [x] [y] = "DEAD"
        	quit_msg()

    	#This is the code if the snake eats a fruit
    	elif(value  == "F"):
        	self.score +=10
        	print ('\033[91m' + "you ate a fruit. Good. Your score is %d....  " %(self.score) + '\033[0m' )
        	self.game_board [x] [y] = "X"

    	elif(value == "I" ):
        	self.score +=3
        	print ('\033[91m' + "you ate a general item. Good. Your score is %d.....  " %(self.score) + '\033[0m' )
        	self.game_board [x] [y] = "X"

    	elif (  value == "GOAL"):
        	self.score +=100
        	print ('\033[91m' +"GOAL!!!!!  GOAL!!!!!! GOAL!!!!Your score is %d . Quitting" %(self.score) + '\033[0m')
        	#sys.exit()
        	quit_msg()

    	elif ( value  == "START"):
        	print ('\033[91m' +"!!!!!  @START Again!!!!" +'\033[0m')

    	##if the snake moves to an empty cell
    	else:
        	self.score+=1
        	print ('\033[91m' +"safe move: Your score is %d ....  " %(self.score) +'\033[0m')
        	self.game_board [x] [y] ="X"

############################################################
class Inventory:
	"""Represent aspects of an inventory."""
	def __init__(self, x, y):
        	self.location_x = x
        	self.location_y = y
	def get_descriptive_name(self):
        	long_name = 'inventory item at:' + str(self.location_x) + ' ' + str(self.location_y)
        	return long_name.title()
	def get_coordinates(self):
        	return  self.location_x, self.location_y

############################################################
class Fruit (Inventory):
	"""Represent aspects of a fruit"""
	def __init__(self, x,y):
        	"""Initialize attributes of the parent class."""
        	super().__init__(x,y)
	def get_descriptive_name(self):
        	long_name = 'Fruit item at:' + str(self.location_x) + ' ' + str(self.location_y)
        	return long_name.title()

############################################################
class Obstacle (Inventory):
	"""Represent aspects of a fruit"""
	def __init__(self, x,y):
        	"""Initialize attributes of the parent class."""
        	super().__init__(x,y)
	def get_descriptive_name(self):
        	long_name = 'Obstacle item at:' + str(self.location_x) + ' ' + str(self.location_y)
        	return long_name.title()

############################################################
#this function is  taken from Internet. I changed parts of it to suit this project
# a nice print of my name ...
def welcome_msg():
	print(pyfiglet.figlet_format("Y. Eldarieby", font = "slant"  ))

	msg = """
	Rules:
  	. This is a simple text based snake game.
  	. Type Q to quit at any time or type "H" to restart the game
  	. Type A, S, D, W to move the snake
  	. As the snake moves, its score increases by 1 point
  	. if the snake eats a fruit:  the score increases by 10 points.
  	. if the snake hits an obstacle: the game will end.
  	. if the sname hits the boader 3 times, the game will end.
  	. Below is the board of the game.
             	.."f" means a fruit,
             	.."o" means an obstacle,
             	.."X" is where the snake is.
	"""
	print(msg)
############################################################
#this function is  taken from Internet. I changed parts of it to suit this project
# a nice print of my name ...
def quit_msg():
	msg = """
	Still Missing:
	*******************
	Quitting......
	"""
	print(msg)
	print(pyfiglet.figlet_format("Y. Eldarieby", font = "slant"  ))
	sys.exit()

############################################################
def get_user_command (x,y):
   	selection = (input("Enter a character (ASDW  or Q or H):"   )) .upper ()
   	global atBorders

   	if selection == "A":
        	if (y > 0):   #going LEFT
            	return x, y-1
        	else:
            	atBorders +=1
            	print ("@BORDERS %d times" %(atBorders))

   	elif selection == "W":   #going UP
        	if (x > 0):
            	return x-1, y
        	else:
           	atBorders +=1
           	print ("@BORDERS %d times" %(atBorders))

   	elif selection == "S":   #going DOWN
        	if (x < 8):
            	return x+1, y
        	else:
            	atBorders +=1
            	print ("@BORDERS %d times" %(atBorders))

   	elif selection == "D":   #going Right
        	if (y < 19 ):
            	return x, y+1
        	else:
            	atBorders +=1
            	print ("@BORDERS %d times" %(atBorders))

   	elif selection == "H":
        	print("Wanna start Again???")
        	mainMenu()
        	######  DO some code here to start the game again
   	elif selection == "Q":
        	quit_msg()
   	else:
       	print("Invalid choice. Enter WASD --- or Q or H")

   	if (atBorders == 3):
       	quit_msg()
   	return x,y
############################################################

#this is the main menu function. It initializes the game, and gets into for-ever loop to take input commands from user in order to move the snake
def mainMenu():
	#  Prints a welcome message
	welcome_msg()
	#This is the boad of the game.  empty strings mean empty cells on the board
	game_board1 = [
          	["","","","","","","","","","","","","","","",  "", "", "", "", ""],
          	["","","","","","","","","","","","","","","",  "", "", "", "", ""],
          	["","","","","","","","","","","","","","","",  "", "", "", "", ""],
          	["","","","","","","","","","","","","","","",  "", "", "", "", ""],
          	["","","","","","","","","","","","","","","",  "", "", "", "", ""],
          	["","","","","","","","","","","","","","","",  "", "", "", "", ""],
          	["","","","","","","","","","","","","","","",  "", "", "", "", ""],
          	["","","","","","","","","","","","","","","",  "", "", "", "", ""],
          	["","","","","","","","","","","","","","","",  "", "", "", "", ""],
         	]
	#Now convert the board game into classes
	game_map1 = GameMap(game_board1)

	#create a start and goal tile
	game_map1.add_goal_tile(0,2)
	#game_map1.add_start_tile(2,10)

	# create and add fruits and obstacles and the snake to  the board.
	#item1 = Inventory(1,2)
	#game_map1.add_inventory_item(item1)

	fruit1 = Fruit(1,14)
	game_map1.add_fruit(fruit1)

	fruit2 = Fruit(2,12)
	game_map1.add_fruit(fruit2)

	fruit3 =  Fruit(5,4)
	game_map1.add_fruit(fruit3)

	fruit4 =  Fruit(7,13)
	game_map1.add_fruit(fruit4)


	obstacle1 =  Obstacle(1,7)
	game_map1.add_obstacle (obstacle1)

	obstacle2 =  Obstacle(3,4)
	game_map1.add_obstacle (obstacle2)

	obstacle3 =  Obstacle(5,9)
	game_map1.add_obstacle (obstacle3)

	obstacle4 =  Obstacle(6,16)
	game_map1.add_obstacle (obstacle4)

	#create a snake
	snake2 =  Snake(2,2)
	game_map1.add_snake(snake2)

	#Display the map
	game_map1.draw_map()

	#infinite loop for playing the game ...  get user input
	while True:
   	x,y = snake2.get_coordinates()
   	game_map1.clear_tile(x,y)
   	x,y =get_user_command(x,y)
   	snake2.move ( x, y )
   	game_map1.check_move(x,y)
   	game_map1.draw_map()

############################################################

mainMenu()
