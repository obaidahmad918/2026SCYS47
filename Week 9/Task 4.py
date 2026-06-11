for x in range(1, 4):
    for y in range(2, 5):
        print(f"{x} and {y}")

for row in range(1, 8):
    print("*" * row)

n = 8
for line in range(n):
    pad = n - line - 1
    stars = 2 * line + 1
    print(" " * pad + "*" * stars)
