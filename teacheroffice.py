# -*- codeing =utf-8 -*-
# @Time:2021/12/17 16:57
# @Author:XPein
# @File:teacheroffice.py
import random
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
offices = [[], [], []]
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)
length = len(offices)
i = 0
while i < length:
    j = 0
    leng = len(offices[i])
    print("第%d个办公室：" % (i+1))
    while j < leng:
        print(offices[i][j], end=" ")
        j += 1
    print()
    i += 1
