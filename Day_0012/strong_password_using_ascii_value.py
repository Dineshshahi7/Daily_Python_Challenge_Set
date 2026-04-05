def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('Length should be at least 6')
        val = False
    if len(passwd) > 20:
        print('Length should not be greater than 20')
        val = False

    # Flags for each condition
    has_digit = has_upper = has_lower = has_sym = False

    for char in passwd:
        if 48 <= ord(char) <= 57:
            has_digit = True
        elif 65 <= ord(char) <= 90:
            has_upper = True
        elif 97 <= ord(char) <= 122:
            has_lower = True
        elif char in SpecialSym:
            has_sym = True

    if not has_digit:
        print('Password should have at least one numeral')
        val = False
    if not has_upper:
        print('Password should have at least one uppercase letter')
        val = False
    if not has_lower:
        print('Password should have at least one lowercase letter')
        val = False
    if not has_sym:
        print('Password should have at least one of the symbols $@#%')
        val = False

    return val

# Test cases
print(password_check('Dinesh@4301'))          
print(password_check('helloWORLD123@'))   
print(password_check('HelloWORLD123'))