def find_student(students, name):
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None


def add_student(students):
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = []

        for i in range(3):
            m = int(input(f"Enter marks {i+1}: "))
            marks.append(m)

        students.append({
            "name": name,
            "age": age,
            "marks": marks
        })

        print(f"Student '{name}' added successfully!\n")

    except ValueError:
        print("Invalid input! Please enter correct data.\n")


def view_students(students):
    if not students:
        print("No students available.\n")
        return

    print("\n--- Student Records ---")
    for student in students:
        avg = sum(student['marks']) / len(student['marks'])
        print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}, Avg: {avg:.2f}")
    print()


def find_topper(students):
    if not students:
        print("No data available.\n")
        return

    topper = max(students, key=lambda s: sum(s['marks']) / len(s['marks']))
    avg = sum(topper['marks']) / len(topper['marks'])

    print("\n Topper Details")
    print(f"Name: {topper['name']}")
    print(f"Age: {topper['age']}")
    print(f"Marks: {topper['marks']}")
    print(f"Average: {avg:.2f}\n")


def search_student(students):
    name = input("Enter name to search: ")
    student = find_student(students, name)

    if student:
        print("\n Student Found")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Marks: {student['marks']}\n")
    else:
        print(" Student not found.\n")


def update_marks(students):
    name = input("Enter name to update marks: ")
    student = find_student(students, name)

    if student:
        try:
            print(f"Current marks: {student['marks']}")
            new_marks = []

            for i in range(3):
                m = int(input(f"Enter new marks {i+1}: "))
                new_marks.append(m)

            student['marks'] = new_marks
            print(" Marks updated successfully!\n")

        except ValueError:
            print(" Invalid input!\n")
    else:
        print(" Student not found.\n")


def delete_student(students):
    name = input("Enter name to delete: ")
    student = find_student(students, name)

    if student:
        confirm = input(f"Delete '{student['name']}'? (y/n): ")
        if confirm.lower() == 'y':
            students.remove(student)
            print(" Student deleted.\n")
        else:
            print("Cancelled.\n")
    else:
        print(" Student not found.\n")


def menu():
    print("====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Find Topper")
    print("4. Search Student")
    print("5. Update Marks")
    print("6. Delete Student")
    print("7. Exit")


def main():
    students = [
        {"name": "Anshuman", "age": 6, "marks": [30, 40, 50]},
        {"name": "Unisha", "age": 13, "marks": [43, 45, 55]},
        {"name": "Dinesh", "age": 24, "marks": [43, 50, 60]},
        {"name": "Ganesh", "age": 34, "marks": [50, 60, 60]}
    ]

    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print(" Please enter a number.\n")
            continue

        if choice == 1:
            add_student(students)
        elif choice == 2:
            view_students(students)
        elif choice == 3:
            find_topper(students)
        elif choice == 4:
            search_student(students)
        elif choice == 5:
            update_marks(students)
        elif choice == 6:
            delete_student(students)
        elif choice == 7:
            print(" Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()