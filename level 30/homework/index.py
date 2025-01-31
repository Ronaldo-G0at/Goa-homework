def find_first_hello(text):
    index = text.lower().find("hello")
    return index

text = "Say hello to the world! Hello there!"
index = find_first_hello(text)
print(f"The first occurrence of 'hello' is at index: {index}")


def find_char_index(text, char):
    # Find the index of the first occurrence of the character
    index = text.find(char)
    
    return index
