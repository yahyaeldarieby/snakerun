# Name : Yahya Eldarieby
# Class : CS20
# Date : 09/23/2019
# Description : Organizing Lists


fruits = ['orange', 'banana', 'pineapple']
print(fruits)

fruits.append('apple')
print(fruits)

fruits = ['orange', 'banana', 'pineapple']
fruits.insert(0, 'apples')
print(fruits)

fruits = ['blueberry', 'orange', 'banana', 'pineapple']
print(fruits)

del fruits[0]
print(fruits)

fruits = ['orange', 'banana', 'pineapple', 'blueberry']
print(fruits)

popped_fruit = fruits.pop()
print(fruits)
print(popped_fruit)

fruits = ['orange', 'banana', 'pineapple', 'blueberry']
print(fruits)

fruits.remove('blueberry')
print(fruits)

fruits = ['orange', 'banana', 'pineapple', 'apple', 'blueberry']
fruits.sort()
print(fruits)

print("Here is the original list:")
print(fruits)

print("\nHere is the sorted list:")
print(sorted(fruits))

print("\nHere is the original list again:")
print(fruits)

fruits = ['orange', 'banana', 'pineapple', 'apple', 'blueberry']
print(fruits)
fruits.reverse()
print(f"This is the reverse list of: ")

fruits = ['orange', 'banana', 'pineapple', 'apple', 'blueberry']
print(len(fruits))

obstacles = ['blocks', 'rocks']
print(f"You will get hit by obstacles such as:{obstacles} ")
print(obstacles)
