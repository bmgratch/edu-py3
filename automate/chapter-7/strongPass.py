#! python3
# strongPass.py
# testing strength of password detection.

# import pyperclip to get from clipboard.
# import re for regex use
import pyperclip, re

# Regex formulas here. Thinking about this, I noticed that the it is kind of easy to do with string checks too.
lengthRegex = re.compile(r'(\w){8}')# Password must be 8 characters in length
capsRegex = re.compile(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')     # PW must contain uppercase
lowerRegex = re.compile(r'[abcdefghijklmnopqrstuvwxyz]')    #  and lowercase characters
digitRegex = re.compile(r'\d')  # PW must contain at least one digit


# Get the clipboard to text. Commented out for testing.
#password = str(pyperclip.paste())

# Test the Clipboard
def passwordTest(pw):
    passfail = 0    # this is a counter to make sure it passes all the checks.

    if lengthRegex.search(pw) == None:
        print("Your password is too short! Please make it 8 or more characters.")
    else:
        passfail += 1
    if capsRegex.search(pw) == None:
        print("Your password needs to have a capitalized letter!")
    else:
        passfail += 1
    if lowerRegex.search(pw) == None:
        print("Your password needs to have a lowercase letter.")
    else:
        passfail += 1
    if digitRegex.search(pw) == None:
        print("Your password needs to have a number AND letters.")
    else:
        passfail += 1
    if passfail < 4:    # Check to make sure it passed each check
        print("Your password \'" + pw +"\' is too weak to continue. Please try again.")
        return False
    else:
        print('Congrats! Your password \'' + pw +'\' passes muster, carry on.')
        return True
    
# TODO Reply based on pass/fail for password strength


# Sample tests:
print(passwordTest('alPhA9'))
print(passwordTest('NINETEE9'))
print(passwordTest('alpha9'))
print(passwordTest('SuperD00per'))
