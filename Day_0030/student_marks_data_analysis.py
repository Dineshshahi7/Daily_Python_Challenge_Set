'''
Problem

You are given student marks:

students = [
    {"name": "A", "math": 80, "science": 70, "english": 90},
    {"name": "B", "math": 60, "science": 65, "english": 55},
    {"name": "C", "math": 90, "science": 85, "english": 88},
    {"name": "D", "math": 50, "science": 45, "english": 60},
]
🎯 Tasks
✅ 1. Add:
👉 total and average for each student

✅ 2. Find:
👉 Top student (highest average)

✅ 3. Find:
👉 Pass/Fail

Pass if average ≥ 60
✅ 4. Subject-wise average:
👉 Average marks for:

Math
Science
English
✅ 5. Find:
👉 Students who scored below 50 in any subject
'''

students = [
    {"name": "A", "math": 80, "science": 70, "english": 90},
    {"name": "B", "math": 60, "science": 65, "english": 55},
    {"name": "C", "math": 90, "science": 85, "english": 88},
    {"name": "D", "math": 50, "science": 45, "english": 60},
]

# 1. Add total and average
for s in students:
    s["total"] = s["math"] + s["science"] + s["english"]
    s["average"] = s["total"] / 3

# 2. Top student
top_student = max(students, key=lambda x: x["average"])
print("Top Student:", top_student["name"])

# 3. Pass/Fail
for s in students:
    s["status"] = "Pass" if s["average"] >= 60 else "Fail"

# 4. Subject-wise average
math_avg = sum(s["math"] for s in students) / len(students)
science_avg = sum(s["science"] for s in students) / len(students)
english_avg = sum(s["english"] for s in students) / len(students)

print("Math Avg:", math_avg)
print("Science Avg:", science_avg)
print("English Avg:", english_avg)

# 5. Students below 50 in any subject
print("Students below 50 in any subject:")
for s in students:
    if s["math"] < 50 or s["science"] < 50 or s["english"] < 50:
        print(s["name"])

# Final output
print("\nFinal Data:")
for s in students:
    print(s)