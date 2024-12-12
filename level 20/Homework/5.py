start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

sum = 0

for num in range(start, end + 1):
    sum += num

print("The sum of numbers between", start, "and", end, "is:", sum)
