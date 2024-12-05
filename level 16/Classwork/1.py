correct_password = "password"
attempts = 0
user_password = ""

while user_password != correct_password:
    user_password = input("enter password: ")
    attempts += 1

print("Access granted")
print(f"u entered password {attempts} ჯერ.")
