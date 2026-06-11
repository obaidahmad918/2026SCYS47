bin_num = input("Enter a binary number: ")
result = 0
power = 0
for bit in reversed(bin_num):
    result += int(bit) * (2 ** power)
    power += 1
print("The decimal equivalent of", bin_num, "is", result)
