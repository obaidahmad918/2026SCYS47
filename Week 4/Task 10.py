def add(a, b): return a + b
def subtract(a, b): return a - b
def product(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

ops = {1: ("Add", add), 2: ("Subtract", subtract), 3: ("Product", product), 4: ("Divide", divide)}
print("Calculator Menu")
for k, (name, _) in ops.items():
    print(f"{k}. {name}")

choice = int(input("Enter your choice: "))
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
if choice in ops:
    print("Result:", ops[choice][1](n1, n2))
else:
    print("Invalid choice")
