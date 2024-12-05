# Loop to keep asking for username and password until both are correct
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "king123" and password == "password123":
        print("Login successful!")
        break
    print("Incorrect username or password. Try again.")
