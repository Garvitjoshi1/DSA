from os import *
from sys import *
from collections import *
from math import *


def findStep(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    else:
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)


# Driver code
n = int(input())
print(findStep(n))
