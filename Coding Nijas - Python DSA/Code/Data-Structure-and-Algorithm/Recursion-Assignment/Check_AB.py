from os import *
from sys import *
from collections import *
from math import *


def checkAB(str):
    if len(str) == 0:
        return True
    if str[0] == 'a':
        if len(str[1:]) > 1 and str[1:3] == 'bb':
            return checkAB(str[3:])
        else:
            return checkAB(str[1:])
    else:
        return False


str = input()
if checkAB(str):
    print("true")
else:
    print("false")
