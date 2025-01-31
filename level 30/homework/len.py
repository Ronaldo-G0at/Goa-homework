def string_length(string):
    return len(string)

text = input("Enter a string: ")
length = string_length(text)
print("The length of the string is:", length)


def strings_lengths(strings):
    return [len(s) for s in strings]

words = ["goa", "hello"]
lengths = strings_lengths(words)
print(lengths)
