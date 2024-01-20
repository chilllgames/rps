import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Welcome to Rock, Paper, Scissors Game!")
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    print("Computer chose:", computer_choice)
    print("You chose:", player_choice)

    if player_choice in choices:
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose. Try again.")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")

# Run the rock, paper, scissors game
rock_paper_scissors()
