incorrect_count = 0
incorrect_count = 0
correct_password = "Goa best"

while True:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Password correct!")
        break
    else:
        incorrect_count += 1
        print("Incorrect password. You have entered the wrong password (incorrect_count) times")
