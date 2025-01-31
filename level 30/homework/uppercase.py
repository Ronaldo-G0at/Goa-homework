name="shio"
name_upper = name.upper()
print(name_upper)

user_name=input("enter your name:  ")
user_name_upper = user_name.upper()
print(user_name_upper)

def convert_to_uppercase(strings):
    return [s.upper() for s in strings]

lowercase_list = ["goa", "martial_arts", "python"]
uppercase_list = convert_to_uppercase(lowercase_list)
print(uppercase_list)
