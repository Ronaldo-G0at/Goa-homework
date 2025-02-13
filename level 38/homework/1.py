
my_tuple = (10, 20, 30, 40, 50)
second_element = my_tuple[1]
last_element = my_tuple[-1]
middle_three_elements = my_tuple[1:4]

print(f"Second Element: {second_element}")
print(f"Last Element: {last_element}")
print(f"Middle Three Elements: {middle_three_elements}")

try:
    my_tuple[1] = 25
except TypeError as e:
    print(f"Error: {e}")

my_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = my_tuple
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")
print(f"e = {e}")

my_tuple = (1, 2, 3, 2, 4, 2)
count_2 = my_tuple.count(2)
index_2 = my_tuple.index(2)

print(f"Count of 2: {count_2}")
print(f"First occurrence of 2: Index {index_2}")