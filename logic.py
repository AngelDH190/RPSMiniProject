import random

choices = ["rock", "paper", "scissors"]

playerchoice = input("enter your choice (rock, paper, scissors): ").lower()

num = random.randint(0, len(choices) - 1)
cpuchoice = choices[num]

if cpuchoice == "rock" and playerchoice == "scissors":
    print("you lose!")
elif cpuchoice == "rock" and playerchoice == "paper":
    print("you win!")
elif cpuchoice == "paper" and playerchoice == "scissors":
    print("you win!")
elif cpuchoice == "paper" and playerchoice == "rock":
    print("you lose!")
elif cpuchoice == "scissors" and playerchoice == "paper":
    print("you lose!")
elif cpuchoice == "scissors" and playerchoice == "rock":
    print("you win!")
else:
    print("tie!")