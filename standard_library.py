# Yahya Eldarieby
# CS30
# 2/12/2019
# Python Standard Library


import sys
from pyfiglet import figlet_format

# x=1
y = int(input("Enter Y:"))
z = int(input("Enter z:"))
# while x<15 :
for x in range(1, 15, 1):
    print("Hello, this is question %d. What is %d * %d: Enter you answer"
          % (x, y, z))
    answer = int(input())
    if answer == y*z:

        print(figlet_format("Correct ", font="banner"))
    else:

        print(figlet_format("InCorrect ", font="banner"))

    z += 3
    y += 2
#    x+=1
    print ("Let's move on to question number %d" % (x+1))
