import main
import random

def run():
    def guess_number():
        # Display the game introduction
        print("\n --- WELCOME TO THE GUESS NUMBER GAME ---")
        print("\n I have selected a number between 1 and 100. Try to guess it!")

        while True:
            # Randomly select a number between 1 and 100
            number = random.randint(1, 100)
            max_attempts = 10  # Set the maximum number of attempts
            attempts = 0  # Initialize the attempt counter

            while attempts < max_attempts:
                try:
                    # Ask the user to input their guess
                    guess = int(input("Enter your guess: "))
                    attempts += 1  # Increment the attempts counter

                    # Check if the guess is too high, too low, or correct
                    if guess > number:
                        print("Lower!")  # If the guess is higher than the number, prompt "Lower!"
                    elif guess < number:
                        print("Higher!")  # If the guess is lower than the number, prompt "Higher!"
                    else:
                        # If the guess is correct, display success message and exit loop
                        print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                        break 

                    # Display the remaining attempts
                    remaining_attempts = max_attempts - attempts
                    if remaining_attempts > 0:
                        print(f"Remaining attempts: {remaining_attempts}")
                    else:
                        # If no attempts are left, display the correct number
                        print(f"You lost! The correct number was: {number}")
                        break
                except ValueError:
                    # Handle invalid input (non-numeric values)
                    print("Please enter a valid numeric value!")

            # Ask the user if they want to play again
            repeat = input("Do you want to play again? (yes/no): ").strip().lower()
            if repeat != 'yes':
                print("Exiting the game. Thanks for playing!")  # Exit message
                break

    # Call the guess_number function to start the game
    guess_number()
