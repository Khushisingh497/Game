'''Rock beats scisssor, scissor beats paper and paper beats rocks,and same hand signal tie'''

import random

li = ["rock","paper","scissor"]
#       0      1       2
playerScore = 0
systemScore = 0

for i in range(1,4):
    randomValue = li[random.randint(0,2)]
    userValue = input("1.scissor\n2.rock\n3.paper\n your choice :")

    if randomValue =="scissor" and userValue =="paper":
        systemScore +=1
        print(f"You choosed {userValue} opponent choosed {randomValue}. so opponent get 1 point...")

    elif randomValue =="rock" and userValue =="scissor":
        systemScore +=1
        print(f"You choosed {userValue} opponent choosed {randomValue}. so opponent get 1 point...")   

    elif randomValue =="paper" and userValue =="rock":
        systemScore +=1
        print(f"You choosed {userValue} opponent choosed {randomValue}. so opponent get 1 point...")

    elif userValue =="scissor" and randomValue =="paper":
        playerScore +=1
        print(f"You choosed {userValue} opponent choosed {randomValue}. so you get 1 point...") 

    elif userValue =="rock" and randomValue =="scissor":
        playerScore +=1
        print(f"You choosed {userValue} opponent choosed {randomValue}. so you get 1 point...") 

    elif userValue =="paper" and randomValue =="rock":
        playerScore +=1
        print(f"You choosed {userValue} opponent choosed {randomValue}. so you get 1 point...") 

    elif userValue =="paper" and randomValue =="paper":
        print(f"You choosed {userValue} opponent choosed {randomValue}. match draww...")

    elif userValue =="rock" and randomValue =="rock":
        print(f"You choosed {userValue} opponent choosed {randomValue}. match draww...") 

    elif userValue =="scissor" and randomValue =="scissor":
        print(f"You choosed {userValue} opponent choosed {randomValue}. match draww...")     

if playerScore==systemScore:
    print("Match draw...")
elif playerScore>systemScore:
    print("You won the game.") 
else:
    print("You lose the game.")                          
          

         