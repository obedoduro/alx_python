#validate pasword
def validate_password(password):
    # Check for password length first
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase letters, and digits
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check for spaces in password
    if ' ' in password:
        return False

    return True
