scored = float(input("Enter obtained marks: "))
total = float(input("Enter total marks: "))
if total <= 0:
    print("Total marks must be greater than 0.")
elif scored < 0 or scored > total:
    print("Obtained marks must be between 0 and total marks.")
else:
    pct = (scored / total) * 100
    print("Percentage =", pct, "%")
