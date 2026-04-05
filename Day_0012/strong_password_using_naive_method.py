def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    # Check length
    if len(passwd) < 6:
        print('Length should be at least 6')
        val = False
        
    if len(passwd) > 20:
        print('Length should not be greater than 20')
        val = False

    # Check for digits
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    # Check for uppercase letters
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    # Check for lowercase letters
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    # Check for special symbols
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#%')
        val = False

    return val

# Main function
def main():
    passwd = 'Dinesh@4301'
    if password_check(passwd):
        print("Password is valid")
    else:
        print("Invalid Password !!")

if __name__ == '__main__':
    main()