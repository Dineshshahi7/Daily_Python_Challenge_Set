import re
def main():
    passwd = 'Dinesh@4301'

    # Regex pattern for password validation
    reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$#%]{6,20}$"

    # Compile regex
    pat = re.compile(reg)

    # Search pattern in password
    mat = re.search(pat, passwd)

    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")

if __name__ == '__main__':
    main()