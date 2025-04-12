def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_cat:
        return ""
    result = []
    for cat in list_of_cat:
        total = sum(int(book.split()[1]) for book in list_of_art if book[0] == cat)
        result.append(f"({cat} : {total})")
    return " - ".join(result)

def replace_exclamation(s):
    return ''.join('!' if c.lower() in 'aeiou' else c for c in s)

def correct(s):
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')

def is_uppercase(inp):
    return inp == inp.upper()

def derive(coefficient, exponent):
    return f"{coefficient * exponent}x^{exponent - 1}"

def switcher(arr):
    alpha = 'zyxwvutsrqponmlkjihgfedcba!? '
    return ''.join(alpha[int(i)-1] for i in arr)

def spin_words(sentence):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())
