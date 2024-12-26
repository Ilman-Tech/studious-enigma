import main

# Functions for basic calculations
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"

def run():
    """
    Run the calculator program.
    """
    while True:
        print('\n --- SIMPLE CALCULATOR --- ')
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (÷)")
        print("5. Exit.")

        try:
            choice = int(input('Choose an option: '))
            
            if choice == 5:
                print('Exiting the calculator. Goodbye!')
                break

            # Input numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform calculation based on the user's choice
            if choice == 1:
                result = add_numbers(num1, num2)
            elif choice == 2:
                result = subtract_numbers(num1, num2)
            elif choice == 3:
                result = multiply_numbers(num1, num2)
            elif choice == 4:
                result = divide_numbers(num1, num2)
            else:
                print("Invalid option. Please choose a valid operation!")
                continue

            print(f"The result is: {result}")
        except ValueError:
            print("Please enter a valid number or option!")
