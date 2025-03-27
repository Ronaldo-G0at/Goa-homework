# 2) Generate a list of numbers from 1 to 10
numbers = [x for x in range(1, 11)]
print("Numbers from 1 to 10:", numbers)

# 3) Generate a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print("Squares of numbers from 1 to 5:", squares)

# 4) Create a list of all even numbers between 1 and 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers between 1 and 20:", even_numbers)

# 5) Generate a list of the first letters of each word in a given list of words
words = ['apple', 'banana', 'cherry', 'date']
first_letters = [word[0] for word in words]
print("First letters of each word:", first_letters)

# 6) Create a list comprehension that converts all words in a given list to uppercase
uppercase_words = [word.upper() for word in words]
print("Words in uppercase:", uppercase_words)

# 7) Generate a list of numbers from 1 to 50 that are divisible by 3
divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print("Numbers divisible by 3 between 1 and 50:", divisible_by_3)

# 8) Create a list comprehension that extracts words with more than 4 letters from a given list of words
long_words = [word for word in words if len(word) > 4]
print("Words with more than 4 letters:", long_words)

# 9) Create a list comprehension that converts a list of temperature values in Celsius to Fahrenheit
celsius_values = [0, 10, 20, 30, 40]
fahrenheit_values = [(c * 9/5) + 32 for c in celsius_values]
print("Temperature in Fahrenheit:", fahrenheit_values)

# 10) Create a list comprehension that finds all prime numbers between 1 and 100
primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print("Prime numbers between 1 and 100:", primes)

# 11) Create a list comprehension that extracts all words from a given sentence that contain at least one vowel and are longer than 5 characters
sentence = "This is a simple sentence with some longer words"
vowels = "aeiou"
long_vowel_words = [word for word in sentence.split() if len(word) > 5 and any(v in word for v in vowels)]
print("Words with vowels and longer than 5 characters:", long_vowel_words)

# 12) Create a list comprehension that generates a sequence of Fibonacci numbers up to the 20th term
fib_sequence = [0, 1]
[fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) for _ in range(2, 20)]
print("Fibonacci sequence up to the 20th term:", fib_sequence)
