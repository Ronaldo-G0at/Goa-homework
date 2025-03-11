# 3) Create a dictionary with at least five key-value pairs and print all the keys using the keys() method.
person = {'name': 'Alice', 'age': 25, 'city': 'Los Angeles', 'job': 'Engineer', 'hobby': 'Reading'}
print(person.keys())

# 4) Create a dictionary and print all the values using the values() method.
person = {'name': 'Alice', 'age': 25, 'city': 'Los Angeles', 'job': 'Engineer', 'hobby': 'Reading'}
print(person.values())

# 5) Create a dictionary and print all key-value pairs using the items() method.
person = {'name': 'Alice', 'age': 25, 'city': 'Los Angeles', 'job': 'Engineer', 'hobby': 'Reading'}
print(person.items())

# 6) Iterate over a dictionary using the items() method and print each key with its corresponding value.
for key, value in person.items():
    print(f"{key}: {value}")

# 7) Create a dictionary and check if a specific key exists using the in operator.
person = {'name': 'Alice', 'age': 25, 'city': 'Los Angeles', 'job': 'Engineer', 'hobby': 'Reading'}
print('name' in person)  # True
print('salary' in person)  # False

# 8) Retrieve a value from a dictionary using the get() method and handle cases where the key does not exist.
age = person.get('age', 'Not Found')
print(age)
salary = person.get('salary', 'Not Found')
print(salary)

# 9) Add a new key-value pair to an existing dictionary and print the updated dictionary.
person['salary'] = 70000
print(person)

# 10) Remove a key-value pair from a dictionary using the pop() method and print the updated dictionary.
person.pop('hobby')
print(person)

# 11) Update an existing dictionary with another dictionary using the update() method.
new_info = {'city': 'San Francisco', 'country': 'USA'}
person.update(new_info)
print(person)

# 12) Create a dictionary and print its length using the len() function.
print(len(person))

# 13) Write a function that returns the sum of all numeric values in a dictionary.
def sum_of_values(d):
    return sum(value for value in d.values() if isinstance(value, (int, float)))

person = {'age': 25, 'salary': 70000, 'years_of_experience': 5}
print(sum_of_values(person))  # Sum of numeric values (25 + 70000 + 5)

# 14) Clear all elements from a dictionary using the clear() method and print the result.
person.clear()
print(person)  # Will print an empty dictionary: {}

# 15) Create a dictionary about your information, use at least 10 key-value pairs.
my_info = {
    'name': 'shio',
    'age': 14,
    'developer': 'Goa',
    'language': 'Python',
    'city': 'kibeebi roa',
    'country': 'georgia',
    'role': 'student',
    'hobbies': ['reading', 'coding', 'learning'],
}
print(my_info)