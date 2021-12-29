# -*- codeing =utf-8 -*-
# @Time:2021/12/29 16:16
# @Author:XPein
# @File:functionwork.py
def printline():
    print("-"*30)


def printlines(n):
    i = 0
    while i < n:
        printline()
        i += 1


printlines(3)


def add3num(a, b, c):
    return a+b+c


def avg(a, b, c):
    return add3num(a, b, c)/3


print(avg(1, 1, 1))


