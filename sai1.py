import random
num=random.randrange(0, 30)
print("you have to guess the number between 0 to 30")
print("you have 3 chances")
for i in range(3):
    k=int(input("enter the number: "))
    if(k>int(num)):
        print("greater number")
    elif(k<int(num)):
        print("lesser number")
    elif(k==int(num)):
        print("you won the game")
        break
if(k!=int(num)):
    print("you lost the game")
    print("the number is:",num)
