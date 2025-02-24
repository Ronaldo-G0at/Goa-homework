import random
#cifris gamocnobis tamashi
def start_game():
    print("Welcome to the Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    max_attempts = 10

    print(f"You have {max_attempts} attempts to guess the number.")

    for attempt in range(1, max_attempts + 1):

        player_guess = input(f"Attempt {attempt}/{max_attempts} - Enter your guess: ")

        if player_guess.isdigit():
            player_guess = int(player_guess)

            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempt} attempts.")
                break
        else:
            print("Please enter a valid number.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")

if __name__ == "__main__":
    start_game()
