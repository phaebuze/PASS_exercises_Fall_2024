import random

# This function was generated to re-use code
# This is where the main game happens

def guessing_game():
    # Generate a random secret number between 1 and 100

    # Generating an int, float would be to hard to guess
    secret_number = random.randint(1, 100)

    print("Welcome to the Guessing Game!")
    print("I have selected a secret number between 1 and 100.")
    print("Try to guess the secret number!")

    while True:
        try:
            # Get user input for their guess
            user_guess = int(input("Enter your guess: "))

            # if-elif-else will only run 1 code block, based on the user guess compared to the secret number
            # This will save computing time.

            # comparing user guess to secret first, 
            
            # Check if the guess is correct
            if user_guess == secret_number:
                print(f"Congratulations! You guessed the secret number {secret_number}.")
                break
            elif user_guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


guessing_game()
