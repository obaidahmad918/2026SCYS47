rows = 5
for r in range(1, rows + 1):
    spaces = rows - r
    stars = 2 * r - 1
    print(" " * spaces + "*" * stars)
