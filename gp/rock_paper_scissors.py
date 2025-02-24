import random
#archeva 
def start_game():
    while True:
        print("Enter your choice: Rock, Paper, or Scissors")
        user_choice = input().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid input. Please choose 'Rock', 'Paper', or 'Scissors'.")

#kompiuteris archeva
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

#vin moigo gamoaq
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

#gamotanebi
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = start_game()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}")
        print(f"The computer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        print("\nDo you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    play_game()
