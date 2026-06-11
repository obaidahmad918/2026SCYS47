to_upper = lambda s: s.upper()
user_str = input("Enter a string: ")
upper_result = to_upper(user_str)

def reverse_str(s):
    return s[::-1]

reversed_result = reverse_str(upper_result)
print("The uppercased string is:", upper_result)
print("The inverted string is:", reversed_result)
