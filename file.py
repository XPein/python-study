# -*- codeing =utf-8 -*-
# @Time:2021/12/29 16:39
# @Author:XPein
# @File:file.py
f = open("test.txt", "w")  # 以写的方式打开test.txt 没有的此test.txt文件会新建
f.write("hello world")
f.close()  # 关闭文件
f = open("test.txt", "r")
content = f.read(5)
print(content)
content = f.readlines()  # 一次性读取所有行形成一个列表
print(content)
f.close()


import os
os.rename("test.txt", "test1.txt")  # os的改名操作


