def count_the_occurrences(paragraph):
    return paragraph.lower().split().count("the")

text = "The sun rises in the east and sets in the west. The sky is clear today."
count = count_the_occurrences(text)
print("The word 'the' appears", count, "times.")


def count_char_occurrences(string, char):
    return string.count(char)

text = "Hello, welcome to the world of programming."
character = input("Enter a character to count its occurrences: ")
count = count_char_occurrences(text, character)
print(f"The character '{character}' appears {count} times.")

