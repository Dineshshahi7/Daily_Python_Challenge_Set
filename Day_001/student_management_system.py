''' 1. Student Management System (Core Logic + Data Structures)

- Create a menu-driven program for managing students.

- Requirements:
i. Store student data in a list of dictionaries:
- name
- age
- marks (list of 3 subjects)
ii. Menu options:
- Add student
- View all students
- Find topper
- Search student by name
- Update marks
- Delete student
iii. Logic:
- Calculate average marks
- Topper = highest average
- Handle invalid input
 '''

def main_fun():
    students = [
        {
            'name': 'Anshuman',
            'age' : 6,
            'marks': [30, 40, 50]
        },
        {
            'name': 'Unisha',
            'age' : 13,
            'marks': [43, 45, 55]
        },
        {
            'name': 'Dinesh',
            'age' : 24,
            'marks': [43, 50, 60]
        },
        {
            'name': 'Ganesh',
            'age' : 34,
            'marks': [50, 60, 60]
        }
    ]
    
    print("----------------- Menu ------------------")
    print("1. for Add student")
    print("2.for View all students")
    print("3. for Find topper")
    print("4. for Search student by name")
    print("5. Update marks")
    print("6. for Delete student")
    
    n = int(input("Enter one number for above task"))
    
    match n:
        case 1:
            print("Enter the record of student")
            name = input("Enter name")
            age = int(input("Enter age"))
            m1 = int(input("Enter first marks"))
            m2 = int(input("Enter second marks"))
            m3 = int(input("Enter third marks"))
            
            new_student = {
                "name" : name,
                "age" : age,
                "marks" : [m1, m2, m3]
            }
            students.append(new_student)
            print(f"Record for {name} added successfully")
            
        case 2:
            print("--------------- Complete record of all students ------------")
            for student in students:
                print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
        case 3:
            topper = max(students, key=lambda s: sum(s['marks']))
        
            # Calculate their average
            total_marks = sum(topper['marks'])
            average = total_marks / len(topper['marks'])
        
            print(f"--- The Topper is {topper['name']} ---")
            print(f"Age: {topper['age']}")
            print(f"Total Marks: {total_marks}")
            print(f"Average: {average:.2f}")
                
        case 4:
            search_name = input("Enter the name of the student to search: ")
            found = False
            
            for student in students:
                # .lower() makes the search case-insensitive (e.g., "ansh" matches "Ansh")
                if student['name'].lower() == search_name.lower():
                    print("\n--- Student Found ---")
                    print(f"Name:  {student['name']}")
                    print(f"Age:   {student['age']}")
                    print(f"Marks: {student['marks']}")
                    
                    
                    found = True
                    break  # Stop the loop once the student is found
            
            if not found:
                print(f"No student found with the name '{search_name}'.")
        case 5:
            update_name = input("Enter the student name to update marks: ")
            found = False
            
            for student in students:
                if student['name'].lower() == update_name.lower():
                    print(f"Current marks for {student['name']}: {student['marks']}")
                    
                    # Option A: Replace all marks at once
                    new_m1 = int(input("Enter new Mark 1: "))
                    new_m2 = int(input("Enter new Mark 2: "))
                    new_m3 = int(input("Enter new Mark 3: "))
                    
                    # This updates the list inside the dictionary
                    student['marks'] = [new_m1, new_m2, new_m3]
                    
                    print(f"Marks updated successfully for {student['name']}!")
                    found = True
                    break
            
            if not found:
                print("Student name not found.")
        case 6:
            delete_name = input("Enter the name of the student to delete: ")
            found = False
            
            for student in students:
                # Use .lower() to ensure it matches even if typing in lowercase
                if student['name'].lower() == delete_name.lower():
                    # Confirm before deleting
                    confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ")
                    
                    if confirm.lower() == 'y':
                        students.remove(student) # Removes the dictionary from the list
                        print(f"Record for {delete_name} has been deleted.")
                    else:
                        print("Deletion cancelled.")
                        
                    found = True
                    break # Stop searching once handled
            
            if not found:
                print(f"No student found with the name '{delete_name}'.")
                
        case _:
                print("Invalid choice, please try again.")
                
                
                
                
if __name__ == "__main__":
    main_fun()