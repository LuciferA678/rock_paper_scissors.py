                        # ROCK PAPER SCISSORS GAME

import random

options = ("rock", "paper", "scissors")
name = input("Enter your name: ")
running = True

while running:

    computer = random.choice(options)
    player = input(f"{name} choose from (rock, paper, scissors):")

    print(f"Computer's choice: {computer}")
    print(f"{name}'s choice: {player}")


    if player == computer:
            print("It's a tie ;), let's play again")
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
            print("Hurray!! you win")
    else:
         print("Uh Oh :( Computer wins")

    play_again = input("Would you like to play again ? (y/n):")
    if play_again != "y":
        running = False


print(f"It was nice playing with you {name}!!")


