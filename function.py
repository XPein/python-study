# -*- codeing =utf-8 -*-
# @Time:2021/12/23 17:05
# @Author:XPein
# @File:function.py


def printfun():
    print("人生苦短我用python")


printfun()

# 带参数的函数


def add_my(a, b):
    return a+b


print(add_my(1, 2))

# 多个返回值的函数


def div(a, b):
    return a//b, a % b


sh, yu = div(5, 2)
print(sh, yu)
