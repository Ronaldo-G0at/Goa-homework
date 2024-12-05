my_num = 4

attempts = 0

while True:
    user_guess = int(input("Guess the number (1-10): "))
    attempts += 1
    
    if user_guess == my_num:
        print(f"you guessed it! Number of attempts: {attempts}")
        break
    else:
        print("Incorrect! Try again.")