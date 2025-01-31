name=input("enter your name:  ")
capitalize_name=name.capitalize()
print(capitalize_name)

def capitalize_first_letter(strings):
    return [s.capitalize() for s in strings]

words = ["goa", "vex", "dr"]
capitalized_words = capitalize_first_letter(words)
print(capitalized_words)


def capitalize_first_letter(string):
    return string.capitalize()

text = "hello world"
capitalized_text = capitalize_first_letter(text)
print(capitalized_text)
