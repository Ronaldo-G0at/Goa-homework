import time
import random

# თამაშის დაწყება
def start_game():
    print("Welcome to the RPG game!")
    time.sleep(1)
    
    # ინვენტორის სია
    inventory = []
    
    # გზის არჩევა
    while True:
        print("\nYou are in a dark forest. Choose your path:")
        time.sleep(1)
        print("1. Go left into the cave.")
        print("2. Go right towards the river.")
        print("3. Climb the tall tree to get a better view.")
        print("4. Follow a mysterious path with glowing mushrooms.")
        print("Type 'exit' to return to the chatbot.")
        
        # შენი არჩევნის ჩასმა
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("You enter the cave and find a treasure chest!")
            time.sleep(1)
            item = random.choice(["magical sword", "gold coins", "ancient book"])
            print(f"Inside, you find {item}!")
            inventory.append(item)
        elif choice == "2":
            print("You walk towards the river and meet a friendly fisherman.")
            time.sleep(1)
            print("He gives you some food for your journey.")
            inventory.append("food")
        elif choice == "3":
            print("You climb the tree and see a distant village.")
            time.sleep(1)
            print("This could be a safe place to rest.")
        elif choice == "4":
            print("You follow the glowing mushrooms and discover a hidden portal!")
            time.sleep(1)
            print("Do you want to enter the portal? (yes/no)")
            portal_choice = input().lower()
            if portal_choice == "yes":
                print("You step into the portal and arrive in a mystical land!")
            else:
                print("You decide to stay in the forest.")
        elif choice.lower() == "exit":
            print("Returning to the chatbot...")
            break
        else:
            print("Invalid choice. Try again.")
        
        print(f"Current Inventory: {', '.join(inventory)}")
        time.sleep(1) # პასუხის მოცემამდე პაუზა

if __name__ == "__main__":
    
    # თამაშის გაშვება
    start_game()