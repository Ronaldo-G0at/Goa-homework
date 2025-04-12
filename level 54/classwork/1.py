try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    if denominator == 0:
        raise ValueError("Cannot divide by zero!")

    result = numerator / denominator
    print("Result:", result)

except ValueError as ve:
    print("ValueError:", ve)

except Exception as e:
    print("Invalid input:", e)

finally:
    print("Operation complete.")