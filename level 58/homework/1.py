# -----------------------
# 2–6: Lambda Functions
# -----------------------

add_five = lambda x: x + 5
multiply = lambda x, y: x * y
is_even = lambda x: x % 2 == 0
c_to_f = lambda c: (c * 9/5) + 32
starts_with_a = lambda s: s.startswith('A')

# -----------------------
# 7–16: map() Examples
# -----------------------

numbers = [5, 10, 15, 20, 25]
strings = ['apple', 'banana', 'cherry']
names = ['Alice', 'Bob', 'Andrew']
temps_c = [0, 20, 37, 100]

add_10 = list(map(lambda x: x + 10, numbers))
uppercased = list(map(lambda s: s.upper(), strings))
lengths = list(map(lambda s: len(s), strings))
squared = list(map(lambda x: x**2, numbers))
as_strings = list(map(lambda x: str(x), numbers))
greetings = list(map(lambda name: "Hello " + name, names))
subtracted = list(map(lambda x: x - 5, numbers))
tripled = list(map(lambda x: x * 3, numbers))
fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_c))
greater_than_50 = list(map(lambda x: x > 50, numbers))

# -----------------------
# 17–26: filter() Examples
# -----------------------

mixed_numbers = [3, 8, 12, 45, 60, 75]
mixed_strings = ['apple', '', 'banana', '', 'cherry']
more_names = ['Alice', 'Bob', 'Anna', 'Charlie']
words = ['tree', 'sky', 'elephant', 'cloud']
mixed_list = [None, 45, None, 'text', '', 0, 5]

evens = list(filter(lambda x: x % 2 == 0, mixed_numbers))
greater_than_10 = list(filter(lambda x: x > 10, mixed_numbers))
long_strings = list(filter(lambda s: len(s) > 5, strings))
non_empty = list(filter(lambda s: s != '', mixed_strings))
positives = list(filter(lambda x: x > 0, mixed_numbers))
a_names = list(filter(lambda name: name.startswith('A'), more_names))
div_by_3 = list(filter(lambda x: x % 3 == 0, mixed_numbers))
has_e = list(filter(lambda word: 'e' in word, words))
no_none = list(filter(lambda x: x is not None, mixed_list))
less_equal_50 = list(filter(lambda x: x <= 50, mixed_numbers))

# -----------------------
# Output Example Results
# -----------------------

if __name__ == "__main__":
    print("Add 5 to 10:", add_five(10))
    print("Multiply 3 and 4:", multiply(3, 4))
    print("Is 8 even?:", is_even(8))
    print("25°C in Fahrenheit:", c_to_f(25))
    print("Starts with 'A' ('Apple'):", starts_with_a("Apple"))

    print("\nAdd 10 to each number:", add_10)
    print("Uppercased strings:", uppercased)
    print("Lengths of strings:", lengths)
    print("Squares:", squared)
    print("As strings:", as_strings)
    print("Greetings:", greetings)
    print("Subtracted by 5:", subtracted)
    print("Tripled:", tripled)
    print("Fahrenheit:", fahrenheit)
    print("Greater than 50:", greater_than_50)

    print("\nEven numbers:", evens)
    print("Greater than 10:", greater_than_10)
    print("Strings > 5 chars:", long_strings)
    print("Non-empty strings:", non_empty)
    print("Positive numbers:", positives)
    print("Names starting with A:", a_names)
    print("Divisible by 3:", div_by_3)
    print("Words with 'e':", has_e)
    print("Without None:", no_none)
    print("≤ 50:", less_equal_50)
