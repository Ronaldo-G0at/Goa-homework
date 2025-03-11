student_info = {
    'name': 'John',
    'age': 22,
    'city': 'New York',
    'major': 'Computer Science',
    'graduation_year': 2024
}

# 1) 
print("Keys in the dictionary:")
print(student_info.keys())

# 2) 
print("\nValues in the dictionary:")
print(student_info.values())

# 3) 
print("\nKey-Value pairs in the dictionary:")
print(student_info.items())

# 4) 
print("\nFormatted key-value pairs:")
for key, value in student_info.items():
    print(f"The {key} is {value}")
