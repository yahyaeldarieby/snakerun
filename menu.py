directions = ['*right', '*left', '*up', '*down']

fruits = ['*apples', '*pineapples', '*blueberry']

print("GO TO THIS FOLLOWING DIRECTIONS:")
for direction in directions[:4]:
    print(direction.title())

print("THE FOLLOWING FRUITS MAKE YOU BIGGER OR SMALLER ")
for fruit in fruits[0:3]:
    print(fruit.title())

directions = input("your decision of moving:")


for x in directions:
    if direction.lower() == x:
        print(direction+"!")



for x in fruits:
    if fruit.lower() == x:
        print(fruit+"!")
