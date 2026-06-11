get_larger = lambda a, b: a if a > b else b
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
bigger = get_larger(num1, num2)

def print_table(n, limit):
    for x in range(1, limit + 1):
        print(n, "x", x, "=", n * x)

print_table(bigger, 10)
