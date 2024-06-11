# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # Check if the user wants another calculation
        next_calculation = input("Let's do the next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid input")


def manage_list(my_list):
    """
    Manages a list by adding, removing, and printing its contents.

    Args:
        my_list (list): The list to manage.

    Returns:
        None
    """
    while True:
        print("\n1. Add an item")
        print("2. Remove an item")
        print("3. Print the list")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            item = input("Enter the item to add: ")
            my_list.append(item)
            print(f"{item} added to the list.")
        elif choice == "2":
            if not my_list:
                print("The list is empty.")
            else:
                item = input("Enter the item to remove: ")
                try:
                    my_list.remove(item)
                    print(f"{item} removed from the list.")
                except ValueError:
                    print(f"{item} not found in the list.")
        elif choice == "3":
            print("Current list:")
            for item in my_list:
                print(item)
        elif choice == "4":
            print("Exiting the list manager.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Example usage:
my_list = []  # Initialize an empty list
manage_list(my_list)
