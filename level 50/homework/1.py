# 1)
try:
    user_input = input("Enter a number: ")
    number = float(user_input)
    print(f"You entered the number: {number}")
except ValueError:
    print("Error: That is not a valid number.")
# 2)
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Tried to access an index that does not exist in the list.")
# 3)
try:
    result = "hello" + 5
except TypeError:
    print("Error: Cannot add a string and an integer.")
