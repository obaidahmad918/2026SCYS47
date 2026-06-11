def get_gpa(grade_list):
    points_map = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    earned = sum(points_map.get(g, 0) for g in grade_list)
    return earned / len(grade_list)

course_count = int(input("Enter the number of courses: "))
grades = []
for idx in range(course_count):
    g = input(f"Enter the grade for course {idx + 1} (A, B, C, D, F): ")
    grades.append(g)
print("Your GPA for the semester is:", get_gpa(grades))
