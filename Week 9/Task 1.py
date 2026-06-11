grades_db = {}

scored = int(input("Enter obtained marks: "))
total = int(input("Enter total marks: "))
if total <= 0 or total > 300:
    print("Invalid marks!")
elif scored > total:
    print("Marks exceed total!")
else:
    pct = (scored / total) * 100
    print("Percentage:", pct)
    if pct >= 90: print("A+")
    elif pct >= 85: print("A-")
    elif pct >= 80: print("B+")
    elif pct >= 75: print("B-")
    elif pct >= 70: print("C+")
    elif pct >= 65: print("C-")
    else: print("F")

num = int(input("Enter number of students: "))
for _ in range(num):
    sname = input("Enter student name: ")
    smarks = int(input("Enter student marks: "))
    grades_db.setdefault(sname, []).append(smarks)

print(grades_db)
