def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except TypeError:
        print("Error: Invalid data type")


divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "abc")