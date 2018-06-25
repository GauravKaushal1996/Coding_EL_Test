from string import ascii_uppercase, ascii_lowercase, digits

'''
Check and suggest if a password is strong or not. 
The password is considered to be strong if it satisfies the following criteria:
● Its length is at least 8. .{8,}
● It contains at least one digit. (?=.*?[0-9])
● It contains at least one lowercase English character. (?=.*?[a-z])
● It contains at least one uppercase English character. (?=.*?[A-Z])
● It contains at least one special character. The special characters are: !@#$%^&*()-+  (?=.*?[!@#$%^&*()-+])
'''

# ((?=.*\d)(?=.*[A-Z])(?=.*\W).{8,})
# ^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#$%^&*()-+]).{8,}

def check(conditionPasswd, s): # check the condition needed
    return any(c in conditionPasswd for c in s)

def checkUpperCase(s): # check for uppercase using the check function
    return check(ascii_uppercase, s)

def checklowerCase(s): # check for lowercase using the check function
    return check(ascii_lowercase, s)

def checkDigits(s): # check for digits in the password using check function
    return check(digits, s)

def checkSpecialCharacter(s): # check for the special character using the check function
    return check(r"""!@#$%^&*()-+""", s)

def checkLength(s): # check the length of the password using the len() keyword
    return len(s) >= 8

def validatePassword(password): # password validation
    conditions = ( # List of validation checks
        (checkUpperCase, 'At least one UPPERCASE English character needed.'),
        (checklowerCase, 'At least one lowercase English character needed.'),
        (checkDigits, 'At least one digit needed.'),
        (checkSpecialCharacter, 'At least one special character needed.'),
        (checkLength, 'Length needs to be at least 8'),
    )
    failMessage = [ # print the message if the Password is not proper or satisfy the proper condition
        returnMessage for validator, returnMessage in conditions if not validator(password)
    ]
    if not failMessage:
        return True
    else:
        print("Password is not valid! Check the conditions for Password."),
        print(" ")
        for returnMessage in failMessage:
            print(returnMessage)
        return False


if __name__ == '__main__': # initiate the python code
    while True:
        password = input("Enter Password For Checking: ")
        if validatePassword(password):
            print("Password is correct.")
            break
