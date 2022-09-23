import random

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def get_user_choice():
    user_choice = input(f'Please pick out of the following options: {["rock", "paper", "scissors"]}')
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        winner = "draw"
    elif [computer_choice, user_choice] in [["rock", "paper"], ["paper", "scissors"], ["scissors", "rock"]]:
        winner = "user"
    else: winner = "computer"
    return winner

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)
    print(computer_choice)
    print(winner)

if __name__ == '__main__':
    play()