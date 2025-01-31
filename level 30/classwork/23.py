def manual_swapcase(input_str):
    result = ""
    for char in input_str:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result


input_str = input("enter string: ")
print(manual_swapcase(input_str))