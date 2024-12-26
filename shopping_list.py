# Importing required modules
import main
import json

# Shopping list data structure
shopping_list = {
    "Fruits": [],
    "Dairy": [],
    "Proteins": [],
    "Drinks": [],
    "Other": []
}

# Dictionary to store item prices
item_price = {}

def show_item():
    """
    Display all items in the shopping list along with their categories and prices.
    """
    if any(shopping_list.values()):
        print("\n--- YOUR SHOPPING LIST ---")
        for category, items in shopping_list.items():
            if items:
                print(f"\n{category}")
                for item in items:
                    price = item_price.get(item, "unknown")
                    print(f"- {item} (${price})")
    else:
        print("Your shopping list is empty!")

def add_item(category, item, price):
    """
    Add an item to the shopping list under a specific category with its price.
    """
    if category in shopping_list:
        shopping_list[category].append(item)
        item_price[item] = price
        print(f"Item '{item}' added to category '{category}' with price ${price:.2f}.")
    else:
        print("Please enter a valid category!")

def remove_item(item):
    """
    Remove an item from the shopping list and its associated price.
    """
    for category, items in shopping_list.items():
        if item in items:
            items.remove(item)
            item_price.pop(item, None)
            print(f"Item '{item}' has been removed from the category '{category}'.")
            return
    print(f"Item '{item}' was not found in your list!")

def search_item(item):
    """
    Search for an item in the shopping list and display its details.
    """
    found = False
    for category, items in shopping_list.items():
        if item in items:
            price = item_price.get(item, "unknown")
            print(f"Item '{item}' found in category '{category}' with price ${price}.")
            found = True
    if not found:
        print(f"Item '{item}' was not found in your list!")

def calculate_item():
    """
    Calculate and display the total price of all items in the shopping list.
    """
    total = sum(item_price.values())
    print(f"Total price of items: ${total:.2f}")

def save():
    """
    Save the shopping list and prices to a JSON file.
    """
    with open('shopping_list.json', 'w') as file:
        json.dump({"items": shopping_list, "prices": item_price}, file)
    print("Shopping list has been saved!")

def load_item():
    """
    Load the shopping list and prices from a JSON file.
    """
    global shopping_list, item_price
    try:
        with open('shopping_list.json', 'r') as file:
            data = json.load(file)
            shopping_list = data["items"]
            item_price = data["prices"]
            print("Shopping list has been loaded!")
    except FileNotFoundError:
        print("File not found! Please save the shopping list first.")

def run():
    """
    Main loop for the shopping list menu, allowing users to interact with the program.
    """
    while True:
        # Display the shopping list menu
        print("\n--- SHOPPING LIST MENU ---")
        print("1. Show item list")
        print("2. Add item")
        print("3. Remove item")
        print("4. Search item")
        print("5. Calculate total price")
        print("6. Save to file")
        print("7. Load from file")
        print("8. Exit")
        
        try:
            # Get the user's choice
            choice = int(input("Choose an option (1-8): "))
            
            # Perform actions based on the user's choice
            if choice == 1:
                show_item()
            elif choice == 2:
                category = input("Enter category (Fruits, Dairy, Proteins, Drinks, Other): ")
                item = input("Enter item name: ")
                try:
                    price = float(input("Enter item price: "))
                    add_item(category, item, price)
                except ValueError:
                    print("Please enter a numeric value for the price!")
            elif choice == 3:
                item = input("Enter the name of the item to remove: ")
                remove_item(item)
            elif choice == 4:
                item = input("Enter the name of the item to search for: ")
                search_item(item)
            elif choice == 5:
                calculate_item()
            elif choice == 6:
                save()
            elif choice == 7:
                load_item()
            elif choice == 8:
                print("Returning to the main menu. Goodbye!")
                break
            else:
                print("Invalid choice! Please select a number between 1 and 8.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")
