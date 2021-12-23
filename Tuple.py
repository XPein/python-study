# -*- codeing =utf-8 -*-
# @Time:2021/12/23 15:57
# @Author:XPein
# @File:Tuple.py

tup1 = ()  # 创建一个空的元组
tup2 = (1)  # 这不是一个元组是一个int它把括号解析成一个运算了。
tup3 = (1, )
print(type(tup2))
tup4 = (1, 2, 3, 4, 5, 6)
# 增
tup5 =('a', 'b')
tup = tup4 + tup5   # 不是在原有的元组上面加是连接了两个元组
print(tup)
# 删
del tup
print(tup)  # 会报错del 是删掉了 tup 而不是元组的 数据
# 改
tup4[0] = 100  # 这是错误的会报错不可修改元组元素
# 查
print(tup4[0])
print(tup4[-1])
print(tup4[1:3])  # 同样的步进区间是左开右闭的
