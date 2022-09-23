# Computer-vision

## Milestone 1

Using the Teachable Machine website I have created a computer vision model with 4 classes: Rock, Paper, Scissors and Nothing, using hundreds of training images for each class. I will be using this model to make a game which allows users to play Rock Paper Scissors against the Computer using their own webcam.

## Milestone 2

I set up a virtual environment with opencv-python, tensorflow, and ipykernel installed. \
I've also written the basic code needed to ask the user for their RPS input, and compare it with the computer's random RPS choice to output who has won.

```python
import random

def get_computer_choice():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    return computer_choice

def get_user_choice():
    user_choice = input(f'Please pick out of the following options: {["Rock", "Paper", "Scissors"]}')
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        winner = "Draw"
    elif [computer_choice, user_choice] in [["Rock", "Paper"], ["Paper", "Scissors"], ["Scissors", "Rock"]]:
        winner = "User"
    else: winner = "Computer"
    return winner

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)
    print(computer_choice)
    print(winner)

if __name__ == '__main__':
    play()
```