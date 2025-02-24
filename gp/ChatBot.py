import time
import random
import rpg_game
import number_guessing
import rock_paper_scissors

# ჩატბოტის მთავარი ფუნქცია
def chatbot():
    print("Hello! I'm your chatbot. What's your name?")
    user_name = input("You: ")  # მომხმარებლის სახელის მიღება
    print(f"Chatbot: Nice to meet you, {user_name}! Type 'exit' to stop.")
    
    # ხუმრობების სია
    jokes = [
        "Why don’t skeletons fight each other? Because they don’t have the guts!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t some couples go to the gym? Because some relationships don’t work out!",
        "Why couldn’t the bicycle stand up by itself? It was two-tired!",
        "I told my wife she should embrace her mistakes. She gave me a hug!"
    ]
    
    # კომანდების სია
    print("\nCommands you can use:")
    print("- how are you")
    print("- what's your name")
    print("- tell me a joke")
    print("- play number guessing")
    print("- play rock paper scissors")
    print("- start rpg game")
    print("- what's the weather")
    print("- who made you")
    print("- what can you do")
    print("- favorite color")
    print("- favorite food")
    print("- do you have friends")
    print("- what time is it")
    print("- can you dance")
    print("- can you sing")
    print("- do you sleep")
    print("- do you like humans")
    print("- what do you dream about")
    print("- where are you from")
    print("- can you help me")
    print("- what's your purpose")
    
    while True:
        user_input = input(f"{user_name}: ").lower() # მომხმარებლის შეტანის მიღება
        
        if user_input == "exit":
            print(f"Chatbot: Goodbye, {user_name}!")
            break # პროგრამის შეჩერება
        elif "how are you" in user_input:
            print(f"Chatbot: I'm just a bot, but I'm doing great, {user_name}!")
        elif "what's your name" in user_input:
            print(f"Chatbot: I'm just a simple chatbot, but I remember your name, {user_name}!")
        elif "tell me a joke" in user_input:
            print(f"Chatbot: {random.choice(jokes)}")  # შემთხვევითი ხუმრობის არჩევა
        elif "play number guessing" in user_input:
            print(f"Chatbot: Starting Number Guessing Game... Good luck, {user_name}!")
            number_guessing.start_game() # number guessing თამაშის დაწყება
        elif "play rock paper scissors" in user_input:
            print(f"Chatbot: Starting Rock Paper Scissors Game... Let's play, {user_name}!")
            rock_paper_scissors.start_game() # rock paper scissors თამაშის დაწყება
        elif "start rpg game" in user_input:
            print(f"Chatbot: Starting RPG game... Have fun, {user_name}!")
            rpg_game.start_game()  # RPG თამაშის დაწყება
        elif "what's the weather" in user_input:
            print(f"Chatbot: I can't check the weather yet, but I hope it's nice, {user_name}!")
        elif "who made you" in user_input:
            print(f"Chatbot: A curious mind like yours, {user_name}!")
        elif "what can you do" in user_input:
            print(f"Chatbot: I can chat with you and will have games soon, {user_name}!")
        elif "favorite color" in user_input:
            print("Chatbot: I like blue, but I don't see colors like you do.")
        elif "favorite food" in user_input:
            print("Chatbot: I don't eat, but I hear pizza is great!")
        elif "do you have friends" in user_input:
            print(f"Chatbot: You're my friend, {user_name}!")
        elif "what time is it" in user_input:
            print("Chatbot: I don't have a watch, but you do!")
        elif "can you dance" in user_input:
            print(f"Chatbot: Only in my dreams, {user_name}!")
        elif "can you sing" in user_input:
            print("Chatbot: La la la... I'm not the best singer!")
        elif "do you sleep" in user_input:
            print(f"Chatbot: Nope! I'm always awake to chat with you, {user_name}.")
        elif "do you like humans" in user_input:
            print("Chatbot: Of course! Humans are fascinating!")
        elif "what do you dream about" in user_input:
            print(f"Chatbot: I dream of having more conversations with you, {user_name}!")
        elif "where are you from" in user_input:
            print("Chatbot: I'm from the digital world!")
        elif "can you help me" in user_input:
            print(f"Chatbot: I'll try my best! What do you need help with, {user_name}?")
        elif "what's your purpose" in user_input:
            print(f"Chatbot: To chat with you and make your day better, {user_name}!")
        else:
            print(f"Chatbot: I don't understand that yet, {user_name}.")
        
        time.sleep(1)  # პასუხის მოცემამდე პაუზა

if __name__ == "__main__":
    chatbot()