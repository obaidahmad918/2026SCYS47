def find_max(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    return z

answer = find_max(20, 69, 67)
print("The largest number will be:", answer)
