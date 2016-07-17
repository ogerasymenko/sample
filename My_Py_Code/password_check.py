'''
program to check is password enought good
'''

import re

__author__ = 'sashko'


def pwd_check(data):
    x = False
    p = re.compile("[a-zA-Z0-9.,!?<>@#$%&*(){}_+=]+")
    # does password contain char in upper register
    a = any(x.isupper() for x in data)
    # lower
    b = any(x.islower() for x in data)
    # digit
    c = any(x.isdigit() for x in data)
    # and if len gt 9
    if a and b and c and 64 >= len(data) >= 10:
        # good password
        print("Good password:", ''.join(p.findall(data)))
        x = True
    return x


assert pwd_check('A1213pokl') == False, "1st example"
assert pwd_check('bAse730onE4@') == True, "2nd example"
assert pwd_check('asasasasasasasaas') == False, "3rd example"
assert pwd_check('QWERTYqwerty') == False, "4th example"
assert pwd_check('123456123456') == False, "5th example"
assert pwd_check('QwErTy911poqqqq') == True, "6th example"
