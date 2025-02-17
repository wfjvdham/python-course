---
def calculate(a: float, b: float, operation: str):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
    else:
        return "Error: Invalid operation."

---
def process_data(data):
    if isinstance(data, int):
        return data ** 2  # Square of an integer
    elif isinstance(data, float):
        return data / 2  # Half of a float
    elif isinstance(data, str):
        return data[::-1]  # Reverse the string
    elif isinstance(data, list):
        return sorted(data)  # Sort the list
    elif isinstance(data, dict):
        return list(data.keys())  # Return dictionary keys as a list
    else:
        return "Unsupported data type"

---
count = 1
while count <= n:
    print(count, end=" ")
    count += 1

---
import random

def guess_the_number():
    """
    A number guessing game where the user has to guess a random number between 1 and 100.
    The program provides hints if the guess is too high or too low.
    """
    secret_number = random.randint(1, 100)  # Generate a random number
    attempts = 0

    print("Guess the number (between 1 and 100)!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))  # Take user input
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Out of bounds! Guess a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop when the correct number is guessed

        except ValueError:
            print("Invalid input! Please enter a number.")

---
def shopping_list():
    """
    A simple shopping list program where users can add, remove, and view items.
    """
    items = []  # Initialize an empty shopping list

    while True:
        print("\nShopping List Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter item to add: ").strip()
            if item:
                items.append(item)
                print(f'"{item}" added to the shopping list.')
            else:
                print("Item cannot be empty.")
        
        elif choice == "2":
            item = input("Enter item to remove: ").strip()
            if item in items:
                items.remove(item)
                print(f'"{item}" removed from the shopping list.')
            else:
                print(f'"{item}" is not in the shopping list.')
        
        elif choice == "3":
            if items:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(items, start=1):
                    print(f"{i}. {item}")
            else:
                print("\nYour shopping list is empty.")
        
        elif choice == "4":
            print("Goodbye!")
            break  # Exit the loop
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

---
def phonebook():
    """
    A simple phonebook program that allows users to store names with numbers
    and retrieve a number by entering a name.
    """
    contacts = {}  # Initialize an empty dictionary

    while True:
        print("\nPhonebook Menu:")
        print("1. Add contact")
        print("2. Get number by name")
        print("3. View all contacts")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter name: ").strip()
            number = input("Enter phone number: ").strip()
            if name and number:
                contacts[name] = number
                print(f"Contact '{name}' added.")
            else:
                print("Name and number cannot be empty.")
        
        elif choice == "2":
            name = input("Enter name to search: ").strip()
            if name in contacts:
                print(f"{name}'s number: {contacts[name]}")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == "3":
            if contacts:
                print("\nContacts List:")
                for name, number in contacts.items():
                    print(f"{name}: {number}")
            else:
                print("\nNo contacts saved.")

        elif choice == "4":
            print("Goodbye!")
            break  # Exit the loop

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

