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

I then put these functions into a class which allows the game to be played in a best of format:

```python

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
```

## Milestone 3

I changed the "get_user_choice" method from a manual input to an input using the camera and keras_model for image recognition (which required the previously made virtual environment to be enabled). Combining it with the get_prediction function allows the camera to constantly make a "best guess" at which signal is being shown on camera: Rock, Paper, Scissors, or Nothing. I then added a countdown into the While loop, which prints a countdown from 6 in the terminal before the camera's latest prediction is taken to be the user's input.

```python
    def get_user_choice(self):

        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        total_duration = 6
        time_passed = 0
        start_time = time.time()

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press p to close the window and input the answer on camera
            if cv2.waitKey(1) & 0xFF == ord('p'):
                break
            if time.time() - start_time >= time_passed:
                time_passed += 1
                print(total_duration - time_passed)
            if time_passed == total_duration:
                break
                    
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        return get_prediction(prediction)
```

## Conclusion

In this project I combined a trained machine learning model for image recognition with my own game code to make RPS fully playable with the computer. If I were to improve this project, I would consider making the countdown timer display in the camera feed for better viewability, rather than being printed in the terminal.