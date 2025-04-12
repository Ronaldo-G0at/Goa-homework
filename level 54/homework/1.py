# 1. User Input Number Division
def divide_numbers():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")

# 2. List Index Access
def access_list_index():
    my_list = ['apple', 'banana', 'cherry']
    try:
        index = int(input(f"Enter an index (0 to {len(my_list) - 1}): "))
        print(f"Item at index {index}: {my_list[index]}")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# 3. Dictionary Key Access
def access_dict_key():
    my_dict = {'name': 'Alice', 'age': 25}
    key = input("Enter a key to access: ")
    try:
        print(f"Value: {my_dict[key]}")
    except KeyError:
        print("Error: Key not found in dictionary.")

# 4. Convert String to Integer
def convert_to_integer():
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print(f"You entered the integer: {number}")
    except ValueError:
        print("Error: That is not a valid integer.")

# 5. Function as Argument – Greeting
def greet():
    print("Hello! Welcome!")

def call_greeting_function(func):
    func()

# 6. Return a Function – Multiplier
def multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply
