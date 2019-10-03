# The character gets bigger when eating the fruits
print("When the character eats these fruits: it gets bigger")
fruits = ['apples', 'bananas', 'grapes', 'pineapple', 'blueberry']
print(fruits[0:5])
i = 1
for fruit in fruits[:5]:
    print i , ".", fruit.title()
    i = i+1

# The game is over when the character gets hit by the obstacles
print("When the character gets hit by these obstacles: the game is over")
obstacles = ['cones', 'blocks', 'rocks']
print(obstacles[0:3])
a = 1
for obstacle in obstacles[:3]:
    print a, obstacle.title()
    a = a+1
