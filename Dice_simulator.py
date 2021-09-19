import random

loop = True

while(loop):
    number = int(input("Enter how many dies you want to roll, 1 or 2?"))
    if(number == 1):
        print(random.randint(1,6))
    elif(number == 2):
        print(random.randint(2,12))
    else:
        print("You entered a number greater than our limit!")
        continue
    again = input('Do you want to roll the dies again. Enter (y/n)?')
    if(again.lower() != 'y'):
        print("Thanks for playing")
        loop = False