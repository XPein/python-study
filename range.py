# -*- codeing =utf-8 -*-
# @Time:2021/12/29 16:28
# @Author:XPein
# @File:range.py
a = 200


def test1():
    a = 100
    print(a)    # 默认使用局部的a，要使用全局的那么在函数内要加入 global a


def test2():
    print(a)    # 没有局部a 默认使用全局的a
