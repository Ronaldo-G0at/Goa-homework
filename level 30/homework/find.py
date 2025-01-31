def find_GoA_position(sentence):
    return sentence.find("GoA")

text = "ME  miyvarS GoA!! !"
position = find_GoA_position(text)
print(position)




def find_char_index(string, char):
    return string.find(char)

text = "Hello, world!"
character = input("Enter the character to find: ")
index = find_char_index(text, character)
print("The index of the character is:", index)
