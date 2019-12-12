# Yahya Eldarieby
# CS30
# 2019/12/11
# Exception Handling


import sys

while True:
    try:
            selection = int(input("Enter a choice 'number' below: "))
    except:
        print ("Invalid input... enter a NUMBER between 1-5:")
    else:
        if selection == 1:
                print("Command up......... ")
        elif selection == 2:
                print("Command down......... ")
        elif selection == 3:
                print("Command right......... ")
        elif selection == 4:
                print("Command left......... ")
        elif selection == 5:
                print("Quitting......... ")
                sys.exit()
        else:
                print ("Invalid input... enter a number BETWEEN 1-5:")
