# Importing necessary modules for various functionalities
import shopping_list
import to_do_list
import calculate
import guess_number
import guess_word

def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    while True:
        # Displaying the main menu options
        print("\n--- MAIN MENU ---")
        print("1. Shopping List")
        print("2. To-Do List")
        print("3. Calculator")
        print("4. Guess a Number")
        print("5. Guess a Word")
        print("6. Exit")
        
        try:
            # Getting user input
            choice = int(input("Choose an option (1-6): "))
            
            # Handling user choices
            if choice == 1:
                shopping_list.run()  # Running shopping list module
            elif choice == 2:
                to_do_list.run()  # Running to-do list module
            elif choice == 3:
                calculate.run()  # Running calculator module
            elif choice == 4:
                guess_number.run()  # Running "Guess a Number" game
            elif choice == 5:
                guess_word.run()  # Running "Guess a Word" game
            elif choice == 6:
                print("Goodbye! Thank you for using the program.")  # Exiting the program
                break
            else:
                print("Invalid choice. Please select a number between 1 and 6.")  # Handling invalid choices
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")  # Handling non-integer input

# Entry point of the program
if __name__ == "__main__":
    main_menu()
