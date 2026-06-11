def get_grade(pct):
    if pct >= 90: return "A+"
    elif pct >= 85: return "A"
    elif pct >= 80: return "B+"
    elif pct >= 75: return "B"
    elif pct >= 70: return "C+"
    elif pct >= 65: return "C"
    elif pct >= 60: return "D"
    else: return "F"

records = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("\nEnter student name: ")
    while True:
        total = int(input("Enter total marks: "))
        if total <= 0:
            print("Total marks must be greater than 0")
        else:
            break
    while True:
        obtained = int(input("Enter obtained marks: "))
        if obtained > total:
            print("Obtained marks cannot be greater than total marks")
        else:
            break
    pct = (obtained / total) * 100
    records[name] = {"Obtained Marks": obtained, "Total Marks": total, "Percentage": pct, "Grade": get_grade(pct)}

print("\nStudent Records:")
for s, d in records.items():
    print(s, ":", d)
