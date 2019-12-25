#! python3
# regStrip.py - simulating the strip() command with regex.
import re

def regStrip(text, mod=r'\w'):
    stripRegex = re.compile(r'(^' + mod + r'+)|(' + mod + r'+$)')
    return(stripRegex.sub('xxx', text))

test1 = '   ehyhey!  Lets play tag!   '

print(regStrip(test1))
