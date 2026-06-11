def convert_f_to_c(temp_f):
    return (temp_f - 32) * 5 / 9

def convert_c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

option = int(input("1,F to C\n2,C to F\nEnter your choice: "))
if option == 1:
    f_val = float(input("Enter temperature in Fahrenheit: "))
    print(f_val, "F is equal to", convert_f_to_c(f_val), "C")
elif option == 2:
    c_val = float(input("Enter temperature in Celsius: "))
    print(c_val, "C is equal to", convert_c_to_f(c_val), "F")
else:
    print("Invalid choice")
