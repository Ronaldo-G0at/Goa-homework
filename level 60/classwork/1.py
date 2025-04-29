#Exclusive "or" (xor) Logical Operator
def xor(a,b):
    return a!= b

#What's the real floor?
def get_real_floor(n):
    if n < 1:
        return n
    elif n < 13:
        return n-1
    elif n > 13:
        return n-2

#Filter out the geese
def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [bird for bird in birds if bird not in geese]

#Name Shuffler
def name_shuffler(s):
    parts = s.split()
    return f"{parts[1]} {parts[0]}"

#Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]

#Lario and Muigi Pipe Problem
def pipe_fix(nums):
    return list(range(min(nums), max(nums) + 1))

#Plural
def plural(n):
    return n == 0 or n > 1

#Multiplication table for number
def multi_table(number):
    res = ""
    for i in range(1,11):
        res += f"{i} * {number} = {i*number}\n"
    return res[0:-1]

#Super duper easy
def problem(a):
    if isinstance(a, str):
        return "Error"
    return a * 50 + 6

#Grasshopper - If/else syntax debug
def check_alive(health):
    if health > 0:
        return True
    else:
        return False
    