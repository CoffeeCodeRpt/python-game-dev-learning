# This game is a number guessing game.
# The user has to guess a number between 1 and 20

import random

# The game tracks the number of guesses the user has made. 
user_guesses = 0

# The game needs to address the player by their name. 
# Get the player's name
print("Hello! Welcome to the number guessing game.")
print("What is your name?")
user_name = input()

print(f"Hello {user_name}! Let's play a game.")
print("I'm thinking of a number between 1 and 20. Can you guess what it is?")


guess = int(input())
user_guesses += 1
# The game needs to generate a random number.
answer = random.randint(1, 20)

# The game needs to compare the answer to the guess and provide feedback to the player.
while guess != answer:
    if guess > answer:
        print("You're a little high. Guess again.")
    else:
        print("You're too low. Try again.")
    guess = int(input())
    user_guesses += 1

print(f"Congratulations {user_name}! You guessed the correct number!")
print(f"And it only took you {user_guesses} guesses!")
print("Thanks for playing!")
