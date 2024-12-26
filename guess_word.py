import random
import time

def run():
    def guess_word_game():
        print('\n --- WELCOME TO THE GUESSING WORD GAME ---')

        while True:
            # Define word lists for different difficulty levels
            levels = {
                "easy": ['sun', 'cat', 'book', 'sky', 'dog'],
                "medium": ['orange', 'compass', 'mountain', 'squirrel', 'flower'],
                "hard": ['dandelion', 'chandelier', 'laboratory', 'microscope', 'umbrella']
            }

            # Ask for difficulty level
            print('\nChoose difficulty: Easy, Medium, Hard.')
            difficulty = input("Enter difficulty: ").lower().strip()

            # Set default difficulty if input is invalid
            if difficulty not in levels:
                print('Invalid difficulty, defaulting to "Easy".')
                difficulty = 'easy'

            word = random.choice(levels[difficulty])  # Random word selection
            hidden_word = ['_'] * len(word)  # Initialize the hidden word
            max_attempts = len(word) + 2  # Set max attempts based on word length
            attempts = 0  # Track incorrect guesses
            guessed_letters = []  # Store guessed letters
            score = 0  # Initialize score
            total_guesses = 0  # Track total number of guesses

            # Set a time limit for the game
            time_limit = 60
            start_time = time.time()

            print(f'\nStart game! You have {time_limit} seconds and {max_attempts} attempts.')
            print(f'Word length: {len(word)}. Word: {" ".join(hidden_word)}.\n')

            # Game loop
            while attempts < max_attempts:
                elapsed_time = time.time() - start_time  # Time passed since game started
                remaining_time = time_limit - elapsed_time  # Remaining time

                # End the game if time is up
                if remaining_time <= 0:
                    print(f"Time's up! The selected word was: {word}. Your attempts: {total_guesses}")
                    break

                print(f'\nRemaining time: {remaining_time:.2f}s. Word: {" ".join(hidden_word)}')

                # Get the player's guess
                guess = input("Enter your guess (letter or full word): ").lower().strip()
                total_guesses += 1

                # Handle letter guesses
                if len(guess) == 1:
                    if guess in guessed_letters:
                        print('You already guessed this letter!')
                    elif guess in word:
                        print('Good job! Letter found in the word.')
                        # Update the hidden word with the guessed letter
                        for index, letter in enumerate(word):
                            if letter == guess:
                                hidden_word[index] = guess
                        guessed_letters.append(guess)  # Add to guessed letters
                        score += 10  # Increase score for correct letter guess
                    else:
                        print('Letter not in the word.')
                        attempts += 1

                # Handle full word guesses
                elif len(guess) == len(word):
                    if guess == word:
                        print(f'Congratulations! You guessed the word: {word}. Your attempts: {total_guesses}.')
                        score += 50  # Increase score for correct full word guess
                        break
                    else:
                        print('Incorrect word guess, please try again.')
                        attempts += 1
                else:
                    print('Invalid input. Please try again!')

                # Check if the player has guessed all the letters
                if '_' not in hidden_word:
                    print(f'You guessed all letters correctly in {total_guesses} attempts!')
                    score += 50  # Bonus score for completing the word
                    break

                # Check if attempts are exhausted
                remaining_attempts = max_attempts - attempts
                if remaining_attempts == 0:
                    print(f'You lost! Attempts over. The correct word was: {word}. Your attempts: {total_guesses}')
                    break

            print(f'\nYour final score: {score}')  # Show final score
            print('Thank you for playing!\n')

            # Ask if the player wants to play again
            play_again = input("Do you want to play again (yes/no)? ").lower().strip()
            if play_again != 'yes':
                print('You are back to the menu!')
                break

    guess_word_game()  # Start the game
