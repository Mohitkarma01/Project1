import random
'''
1 for snake
2 for water
3 for gun
'''

computer = random.choice([1,2,3])
youstr = input("Enter your choice: ")
youDict = {"s":1,"w":2,"g":3}
reverseDict = {1:"Snake",2:"Water",3:"Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its Draw")

else:
    if(computer == 2 and you == 1):
        print("You Win!")

    elif(computer == 2 and you == 3):
        print("You Lose!")

    elif(computer == 1 and you == 2):
        print("You Lose!")

    elif(computer == 1 and you == 3):
        print("You Win!")

    elif(computer == 3 and you == 2):
        print("You Win!")

    elif(computer == 3 and you == 1):
        print("You Lose!")
    
    else:
        print("Something went wrong!")