# 2) დაბეჭდეთ თქვენი სრული სახელი
print("brbr pataim")

# 3) დაბეჭდეთ საყვარელი ციტატა
print("I don’t pay for suits. My suits are on the house or the house burns down.")

# 4) დაბეჭდეთ 3-ხაზიანი მოკლე ლექსი, თითოეული ხაზი ცალ-ცალკე
print("Roses are red")
print("Violets are blue")
print("Coding is fun, and so are you!")

# 5) დაბეჭდეთ მარტივი მათემატიკური შედეგი (2 + 3)
print(2 + 3)

# 6) დაბეჭდეთ სიმბოლოებით დახატული ფორმა (სამკუთხედი # გამოყენებით)
print("   #")
print("  ###")
print(" #####")
print("#######")

# 7) სტრინგის რიცხად ქცევა და ბეჭდვა
num_str = "42"
num_int = int(num_str)
print(num_int)  # შედეგი: 42

# 8) ორი (float) რიცხვის ჯამი
a = 3.5
b = 2.5
print(a + b)

# 9) ორი სიტყვა ერთად, ერთი ელემენტია
greeting = "Hello"
subject = "World"
print(greeting + " " + subject)  # Hello World

# 10) საყვარელი ტიპების ნახვა ტიპების მიხედვით
x = 10
y = "Python"
z = 3.14
print(type(x))  # პასუხი int
print(type(y))  # პასუხი str
print(type(z))  # პასუხი float

# 11) მომხმარებლისგან ასაკის მიღება და მომდევნო წლის ასაკის გამოთვლა
age_str = input("Enter your age: ")
age = int(age_str)
print(f"Next year you will be {age + 1} years old.")

# 12) მომხმარებლის სახელის კითხვა და მისალოცი ტექსტის ყრა
your_name = input("What is your name? ")
print(f"Hello, {your_name}!")

# 13) ისევ ასაკი და მომდევნო წლის გამოტანა
age_str = input("Enter your age: ")
age = int(age_str)
print(f"Next year you will be {age + 1} years old.")

# 14) კალკულატორი: ორი რიცხვის ჯამი
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The sum is {num1 + num2}")

# 15) ჰკითხეთ საყვარელი ფერი და შეინახეთ
fav_color = input("What is your favorite color? ")
print(f"Your favorite color is {fav_color}!")

# 16) სიმაღლის შემოწმება (> 150 სმ ?)
height_cm = int(input("Enter your height in cm: "))
if height_cm > 150:
    print("You are tall enough.")
else:
    print("You might need a little boost!")

# 17) ბეჭდეთ 1–დან 5-მდე for-ციკლით
for i in range(1, 6):
    print(i)

# 18) სტრინგში თითოეული ასო ახალ ხაზზე for-ით
word = "Python"
for letter in word:
    print(letter)

# 19) ჯამი for-ით 1–დან 10-მდე და დაბეჭდვა
total = 0
for i in range(1, 11):
    total += i
print(total)  # 55

# 20) გამრავლების ცხრილი 2-ისთვის (1–5)
for i in range(1, 6):
    print(f"2 x {i} = {2 * i}")

# 21) დაბეჭდეთ ყველა წყვილი რიცხვი 2–დან 20-მდე
for i in range(2, 21, 2):
    print(i)

# 22) while-ით 1–დან 5-მდე ბეჭდვა
i = 1
while i <= 5:
    print(i)
    i += 1

# 23) same but ჯამიც while-ით
i = 1
sum_5 = 0
while i <= 5:
    sum_5 += i
    i += 1
print(sum_5)

# 24) ჩათვალეთ 10–დან 1-მდე უკან while-ით
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) ბეჭდეთ კენტები 1–დან 10-მდე while-ით
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

# 26) loop until 'exit' მომხმარებლისგან
while True:
    text = input("Enter something (type 'exit' to quit): ")
    if text.lower() == "exit":
        print("Bye!")
        break
    print(f"You entered: {text}")

# 27) გამოტანეთ ელემენტები სიიდან for-ით
items = ["apple", "banana", "cherry"]
for item in items:
    print(item)

# 28) len() რომ ზომა გავიგოთ სიაზე
print(f"List has {len(items)} items.")

# 29) წაახალისეთ მეორე ელემენტი
numbers = [10, 20, 30, 40]
print(f"Second element is {numbers[1]}")

# 30) ახალ ელემენტს მივუწეროთ და ვბეჭდოთ სიაში
numbers.append(50)
print("After appending:", numbers)

# 31) მოაშორეთ 20 და დააბეჭდეთ
numbers.remove(20)
print("After removal:", numbers)

# 32) კუბები list comprehension-ით 1–5
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# 33) წყვილი რიცხვები list comprehension-ით
evens = [x for x in range(2, 11) if x % 2 == 0]
print("Evens:", evens)

# 34) odd-ების ფილტრი list comprehension-ით
mixed = [1, 2, 3, 4, 5, 6]
odds = [x for x in mixed if x % 2 != 0]
print("Odds:", odds)

# 35) ყველა სიტყვა დიდ ასოებად list comprehension-ით
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)

# 36) მხოლოდ even-ების კვადრატი list comprehension-ით
nums = [1, 2, 3, 4, 5]
squared_evens = [x**2 for x in nums if x % 2 == 0]
print("Squared evens:", squared_evens)

# 37) ფუნქცია მისალმებისთვის
def greet(name):
    print(f"Hi, {name}! Nice to meet you.")

greet("Alice")

# 38) ორი რიცხვის დამატება ფუნქციით
def add(a, b):
    return a + b

print("5 + 7 =", add(5, 7))

# 39) even თუ odd ფუნქციით
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print("10 არის", even_or_odd(10))
print("7 არის", even_or_odd(7))

# 40) მართკუთხედის ფართობი
def rectangle_area(length, width):
    return length * width

print("Area:", rectangle_area(5, 3))

# 41) სტრინგის გადატრიალება
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

# 42) ტუპლის შექმნა და ბეჭდვა
tuple_example = (1, "two", 3.0)
print("Tuple:", tuple_example)

# 43) ტუპლიდან მეორე ელემენტი
print("Second:", tuple_example[1])

# 44) ტუპლის ზომა
print("Tuples length:", len(tuple_example))

# 45) ორი ტუპლის გაერთობა
print("Combined:", (1, 2) + (3, 4))

# 46) ტუპლში ძებნა
print("Has 'two'?:", "two" in tuple_example)

# 47) ნაკრების შექმნა და ნახვა
set_example = {1, 2, 3}
print("Set:", set_example)

# 48) ნაკრებში membership
print("2 არის ნაკრებში?", 2 in set_example)

# 49) ახალ ელემენტს ვუმატებთ ნაკრებს
set_example.add(4)
print("After add:", set_example)

# 50) წაშლა ნაკრებიდან
set_example.remove(2)
print("After remove:", set_example)

# 51) ორი set-ის გაერთიანება
print("Union:", {1,2,3} | {3,4,5})

# 52) dictionary შექმნა და ნახვა
dict_example = {"name": "Alice", "age": 30}
print("Dict:", dict_example)

# 53) dict-იდან მნიშვნელობის გამოწერა
print("Name is", dict_example["name"])

# 54) ახალი key-value წყვილი და შენახვა
dict_example["city"] = "Tbilisi"
print("Updated dict:", dict_example)
