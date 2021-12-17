# -*- codeing =utf-8 -*-
# @Time:2021/12/17 15:47
# @Author:XPein
# @File:list.py



# 定义一个空的列表
namelist = ["小a", "小b", "小c"]
testlist = [1, "测试"]  # 列表可以混合数据类型

for name in namelist:  # 循环打印列表
    print(name)

length = len(namelist)  # len可以返回列表的长度
i = 0
while i < length:
    print(namelist[i])
    i += 1
# 列表增
a = [1, 2, 3, 4]
b = [4, 5]
a.append(5)  # 列表追加一个元素
print(a)

a.append(b)  # 列表追加一个列表会把列表当作一个元素追加到列表的末尾
print(a)
a.extend(b)  # 列表a扩展一个列表b会把b中的每一个元素当作一个元素扩展到末尾
print(a)

a.insert(2, 3)  # 把元素3插入到下标为2的位置
print(a)

#  列表删
movie = ["黑客帝国", "阿凡达", "星际迷航", "她"]

del movie[2]   # 删除下标为2的元素
movie.pop()   # 弹出末尾的元素
movie.remove("阿凡达")  # 直接删除指定内容的元素（只删除重复的第一个元素）
print(movie)


# 列表改
movie[0] = "冰雪奇缘"
print(movie)

# 列表查
moviename = input("请输入你要查看的电影：")
if moviename in movie:
    print("马上开始播放")
else:
    print("没有此电影")

print(a.index(3, 1, 5))  # 在a列表的1~5的范围内（不包含5）找3找到了返回找到的位置（有重复元素返回第一个的小标）
# 找不到会报错，后续可以根据错误处理维持程序继续进行
print(a.count(3))  # 计算元素3出现的次数

a.reverse()  # 反转a
print(a)

b.sort()   # 升序排序
print(b)
b.sort(reverse=True)  # 降序排序

