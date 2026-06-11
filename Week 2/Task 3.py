begin = int(input("Enter the starting number: "))
finish = int(input("Enter the ending number: "))
total = 0
print("Prime numbers in the range are: ")
for num in range(begin, finish + 1):
    if num > 1:
        is_prime = True
        for d in range(2, num):
            if num % d == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
            total += num
print("The sum of prime numbers in the range is: ", total)
