''' File-Based Password Manager (File Handling + Security Logic)

- Build a simple password manager.
i) Requirements:
- Store data in a file (passwords.txt)

ii) Each record:
 website | username | password
 
iii) Features:
- Add new password
- View all passwords
- Search password by website
- Delete entry
iv) Logic:
- Do NOT duplicate website entries
- Mask passwords when displaying (e.g., ****123)

v) Bonus:
- Use functions + exception handling
'''

file_name = "passwords.txt"

def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open(file_name, "r") as f:
            data = f.readlines()
        
            for line in data:
                if line.split('|')[0].strip().lower() == website.lower():
                    print("Website already exist!")

    except FileNotFoundError:
        pass

    with open(file_name, "a") as f:
        f.write(f"{website} | {username} | {password}\n")
        print("Password saved successfully!\n")
        
        
def view_passwords():
    try:
        with open(file_name, "r") as f:
            for line in f:
                website, username, password = line.strip().split("|")

                password = password.strip()
                masked = "*" * (len(password) - 3) + password[-3:]

                print(f"{website.strip()} | {username.strip()} | {masked}")
    except FileNotFoundError:
        print("No data found.\n")
        
        
def search_password():
    website = input("Enter website to search: ")

    try:
        with open(file_name, "r") as f:
            found = False
            for line in f:
                w, u, p = line.strip().split("|")

                if w.strip().lower() == website.lower():
                    p = p.strip()
                    masked = "*" * (len(p) - 3) + p[-3:]

                    print(f"Found: {w.strip()} | {u.strip()} | {masked}")
                    found = True
                    break

            if not found:
                print("Website not found.\n")

    except FileNotFoundError:
        print("No data found.\n")
        
        
        
def delete_password():
    website = input("Enter website to delete: ")

    try:
        with open(file_name, "r") as f:
            lines = f.readlines()

        new_lines = []
        found = False

        for line in lines:
            if line.split("|")[0].strip().lower() != website.lower():
                new_lines.append(line)
            else:
                found = True

        with open(file_name, "w") as f:
            f.writelines(new_lines)

        if found:
            print("Deleted successfully.\n")
        else:
            print("Website not found.\n")

    except FileNotFoundError:
        print("No file found.\n")
        
        
def menu():
    while True:
        print("----- Password Manager -----")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            break
        else:
            print("Invalid choice\n")


menu()