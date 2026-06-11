val = int(input("Enter a number: "))
try:
    answer = val / 0
except ZeroDivisionError as err:
    print("Cannot divide by zero!")
    print("Error:", err)
