botanical = {
    "Malus domestica": "Apple",
    "Musa acuminata": "Banana",
    "Vitis vinifera": "Grapes",
    "Mangifera indica": "Mango"
}
print(botanical["Mangifera indica"])
for sci_name, common in botanical.items():
    print(sci_name, ":", common)
