'''
# Mini Data Analysis Project (Like Data Science 🔥)
You are given student marks data:
students = [
    {"name": "A", "marks": [80, 70, 90]},
    {"name": "B", "marks": [60, 50, 65]},
    {"name": "C", "marks": [95, 85, 92]},
    {"name": "D", "marks": [40, 45, 50]}
]

i) Requirements:
ii) Calculate:
- Average marks of each student
- Class average

iii) Find:
- Topper
- Failed students (avg < 50)

iv) Grade system:
A: 80+
B: 60–79
C: 50–59
F: <50

v) Output:
- Print structured report

vi) Bonus:
- Sort students by marks
'''

students = [
    {"name": "A", "marks": [80, 70, 90]},
    {"name": "B", "marks": [60, 50, 65]},
    {"name": "C", "marks": [95, 85, 92]},
    {"name": "D", "marks": [40, 45, 50]}
]

class_total = 0
failed_students = []

# Calculate average of each student
for student in students:
    avg = sum(student["marks"]) / len(student["marks"])
    student["average"] = avg
    class_total += avg

    # Grade system
    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"
        failed_students.append(student["name"])

    student["grade"] = grade

# Class average
class_average = class_total / len(students)

# Find topper
topper = max(students, key=lambda x: x["average"])

# Sort students by average marks
students.sort(key=lambda x: x["average"], reverse=True)

# Print report
print("----- Student Report -----")
for student in students:
    print(f"Name: {student['name']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {student['grade']}")
    print()

print(f"Class Average: {class_average:.2f}")
print(f"Topper: {topper['name']} ({topper['average']:.2f})")
print("Failed Students:", failed_students)