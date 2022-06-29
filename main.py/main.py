from distutils.log import error

# user input
import random

action = {"R": "Rock", "P": "Paper", "S": "Scissors"}
cancun = list(action.keys())
print(cancun)
sen = True
pai = True
while pai:
    while sen:
        user = input("Enter a choice: R for Rock, P for Paper and S for Scissors ")
        if user in cancun:
            print("choice taken")
            sen = False

        else:
            print("Error, invalid choice. Try again")

#computer input
    comp = random.choice(cancun)
    print(comp)

#Display Selections
    print(f"Player ({action.get(user)}) : Computer ({action.get(comp)})")
#Gameplay
    playerWinMessage = "Player Wins"
    computerWinMessage = "Computer Wins"
    if user == comp:
        print("Tie")
        sen = True
        continue

    elif user == "R":
        if comp == "P":
            print(computerWinMessage)    
        else:
            print(playerWinMessage)    

    elif user == "P":
        if comp == "R":
            print(playerWinMessage)
        else:
            print(computerWinMessage)  

    elif user == "S":
        if comp == "P":
            print(playerWinMessage)
        else:
            print(computerWinMessage) 

    chan = True
    print("Do you want to continue?")
    while chan:
        calma = input("Enter n for no and y for yes: ")
        calma = calma.lower()
        if calma == "y".lower():
            pai = True
            sen = True
            chan = False

        elif calma == "n".lower():
            pai = False
            sen = False
            chan = False

        else:
            print("Invalid input, enter Y for Yes and N for No")




    
        

