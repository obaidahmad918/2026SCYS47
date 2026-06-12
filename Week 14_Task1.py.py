def square(n):
    print(n * n)

num = int(input("Enter a number: "))
num1 = int(input("Enter another number: "))
square(num)

sum_func = lambda x, y: x + y  # Renamed to avoid conflict with built-in sum
print(sum_func(num, num1))
lambda_square = lambda x: x * x
print(lambda_square(num))

num_list = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x * x, num_list))
print(squared_list)