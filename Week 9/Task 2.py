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

num = int(input("Enter number of students: "))
idx = 1
while idx <= num:
    sname = input("Enter student name: ")
    smarks = int(input("Enter student marks: "))
    grades_db.setdefault(sname, []).append(smarks)
    idx += 1

print(grades_db)
