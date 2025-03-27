def maskify(cc):
    return cc[0] + 'x' * (len(cc) - 2) + cc[-1] if len(cc) > 4 else cc

def remove_the_two_end_elements(arr):
    return arr[1:-1]

def number_of_occurrences(n):
    return str(n).count(str(n))

def high_product_of_three(arr):
    arr.sort()
    return max(arr[-1] * arr[-2] * arr[-3], arr[0] * arr[1] * arr[-1])

def reverse_words(str):
    return ' '.join(word[::-1] for word in str.split())

def is_square(n):
    return n >= 0 and (n ** 0.5).is_integer()

def sum_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def square_numbers(arr):
    return [x ** 2 for x in arr]

def find_average(nums):
    return sum(nums) / len(nums) if nums else 0

def sum_first_n(n):
    return sum(range(1, n + 1))

def reverse_number(n):
    return int(str(n)[::-1])

def reverse_array(arr):
    return arr[::-1]

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def to_binary(n):
    return bin(n)[2:]

def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_palindrome(s):
    return s == s[::-1]

def remove_non_alpha(s):
    return ''.join(char for char in s if char.isalpha())

def find_smallest(arr):
    return min(arr)

def sum_excluding_extremes(arr):
    arr.sort()
    return sum(arr[1:-1]) if len(arr) > 2 else 0
