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