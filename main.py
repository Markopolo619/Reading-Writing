import random
choice = ["rock", "paper", "scissors"]

player = input("Welcome to Rock,Paper,Scissors. Type one:  ")

computer = random.choice(choice)

if player == "rock" and computer == "rock":
    print("You drawn")
elif player == "rock" and computer == "scissors":
    print("You won")
elif player == "rock" and computer == "paper":
    print("You lost")


if player == "paper" and computer == "rock":
        print("You won")
elif player == "paper" and computer == "scissors":
        print("You lost")
elif player == "paper" and computer == "paper":
        print("You drawn")


if player == "scissors" and computer == "rock":
    print("You lost")
elif player == "scissors" and computer == "scissors":
    print("You drawn")
elif player == "scissors" and computer == "paper":
    print("You won")


if player != choice[0]:
    print("Please choose: Rock, Paper and Scissors")
elif player != choice[1]:
    print("Please choose: Rock, Paper and Scissors")
elif player != choice[2]:
    print("Please choose: Rock, Paper and Scissors")

