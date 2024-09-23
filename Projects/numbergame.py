import random

def number_guessing_game():
    #random number
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        #tell the player to guess
        guess = input("Enter your guess: ")

        # invalid
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("Higher! Try again.")
        elif guess > secret_number:
            print("Lower! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

# Run the game
number_guessing_game()