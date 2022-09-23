import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction(prediction):
    predicted_index = np.argmax(prediction)
    choices = ["Rock", "Paper", "Scissors", "Nothing"]
    return choices[predicted_index]

import time

start_time = time.time()

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if time.time() > start_time + 6:
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

import random

def get_computer_choice():
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    return computer_choice

def get_user_choice():
    return get_prediction(prediction)

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
    print(f"You chose {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print(f"The winner is {winner}")

if __name__ == '__main__':
    play()
