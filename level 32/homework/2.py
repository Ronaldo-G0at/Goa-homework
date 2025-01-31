def reverse_string(sentence):
    reversed_sentence = sentence[::-1]
    return f"The reversed string is: {reversed_sentence}"

input_string = "Hello, world!"
result = reverse_string(input_string)
print(result)
