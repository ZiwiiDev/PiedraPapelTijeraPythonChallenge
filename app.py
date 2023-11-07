#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# We are going to develop the Python console mini-game. It will be rock, paper, scissors.
# Rules of the game: Rock beats scissors (breaks them). The scissors have beaten the paper (cut it). The paper beats the stone (wraps it). The mini-game is multiplayer and the team plays the role of the opponent and chooses a random item from the list of items.
# Player interaction: The console is used to interact with the player. The player can choose one of three options: rock, paper or scissors. The player can choose whether to play again. The player should be warned if he/she enters an invalid option. The player sees his score at the end of the game.
# Validation of the user's entry: In each round, the player must enter one of the listed options and be informed whether he won, lost or tied with the opponent. The mini-game must check the user's entries, lowercase them and inform the user if the option is invalid. At the end of each round, the player must answer if he wants to play again or not.
# Implement it.

import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def play_game():
    user_score = 0
    opponent_score = 0

    while True:
        user_choice = get_user_choice()
        opponent_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"You chose: {user_choice}")
        print(f"Opponent chose: {opponent_choice}")

        if user_choice == opponent_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'rock' and opponent_choice == 'scissors') or
            (user_choice == 'paper' and opponent_choice == 'rock') or
            (user_choice == 'scissors' and opponent_choice == 'paper')
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Opponent wins this round!")
            opponent_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Your score: {user_score}")
    print(f"Opponent's score: {opponent_score}")
    if user_score > opponent_score:
        print("You win the game!")
    elif user_score < opponent_score:
        print("Opponent wins the game!")
    else:
        print("It's a tie in the overall game!")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
