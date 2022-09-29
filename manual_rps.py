import random

class RPS:

    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        return computer_choice

    def get_user_choice(self):
        user_choice = input(f'Please pick out of the following options: {["Rock", "Paper", "Scissors"]}')
        return user_choice

    def get_winner(self,computer_choice, user_choice):
        if computer_choice == user_choice:
            self.winner = "Noone"
        elif [computer_choice, user_choice] in [["Rock", "Paper"], ["Paper", "Scissors"], ["Scissors", "Rock"]]:
            self.winner = "User"
            self.user_wins += 1
        else: 
            self.winner = "Computer"
            self.computer_wins += 1
        return self.winner

def play(winning_score = 3):
    game = RPS()
    while True:
        computer_choice = game.get_computer_choice()
        user_choice = game.get_user_choice()
        game.get_winner(computer_choice, user_choice)
        print(f"You chose {user_choice}")
        print(f"The computer chose: {computer_choice}")
        print(f"{game.winner} won this round")
        print(f"The score is {game.user_wins} - {game.computer_wins} to you!")
        if game.user_wins == winning_score:
            print(f"User wins the best of {winning_score * 2 - 1} match!")
            break
        elif game.computer_wins == winning_score:
            print(f"Computer wins the best of {winning_score * 2 - 1} match!")
            break

if __name__ == '__main__':
    play()