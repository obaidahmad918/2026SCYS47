x = 25
y = "Obaid"
print(y)

def welcome():
    x = 15
    # Using globals() safely
    if 'x' in globals() and 'y' in globals():
        print(globals()['x'], globals()['y'])
    else:
        print("Global variables not found")

welcome()
print(x)