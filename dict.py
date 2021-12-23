# -*- codeing =utf-8 -*-
# @Time:2021/12/23 16:22
# @Author:XPein
# @File:dict.py

info = {"name": "吴彦祖", "age": 18}
# 字典的访问
print(info["name"])
print(info["age"])
# 访问不存在的键
# print(info("gender"))  # 会报错
print(info.get("gender", "m"))  # 找不到gender用默认值 m
# 增
ID = input("please input id:")
info["ID"] = ID
print(info)
# 删
# del
del info["name"]  # 删除的是name 键值对
del info  # 删除整个字典从内存中全部清除
# clear
info = {"name": "吴彦祖", "age": 18}
info.clear()  # 清空键值 info这个字典还是存在的
print(info)
# 改
info["age"] = 20

# 查
info.keys()  # 得到所有的键值（列表# ）
info.values()  # 的到所有的值 （列表）
info.items()  # 的到所有的项（列表）,每个键值对是一个元组

# 遍历
for key in info.keys():
    print(key)
for value in info.values():
    print(value)
for key,value in info.items():
    print("key=%s ,value =%s" % (key, value))
mylist = [1, 2, 3, 4, 5]
for i, x in enumerate(mylist):   # enmurate() 将列表改成一个下标和值的枚举
    print(i+1, x)



