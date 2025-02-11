def greet():
    print("Hello, World!")


def add_numbers(num1, num2):
    print(num1 + num2)


def multiply_by_10(number):
    return number * 10


def greet(name="Guest"):
    print(f"Hello, {name}!")


def outer_function():
    def inner_function():
        print("Hello from the inner function!")
    
    print("Hello from the outer function!")
    inner_function()  


outer_function()


def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")



def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num