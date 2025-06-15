# https://classroom.codingninjas.com/app/classroom/me/18891/content/375607/offering/5315772/problem/43
from os import *
from sys import *
from collections import *
from math import *


def string(s):
    if len(s) == 1:
        return s
    x = string(s[1:])
    for i in range(len(s)):
        if s[i] == s[i + 1]:
            x = s[:i], '*', s[i + 1:]
            return x


s = str(input())
print(string(s))
