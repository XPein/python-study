import random
computer = random.randint(0, 2)
password = input("输入手势：")

if computer == 0:
    if password is "石头":

        print("平局")
    if password is "剪刀":
        print("你输了")
    if password is "布":
        print("你赢了")
elif computer == 1:
    if password == "石头":
        print("你赢了")
    if password == "剪刀":
        print("平局")
    if password == "布":
        print("你输了")
else:
    if password == "石头":
        print("你赢了")
    if password == "剪刀":
        print("平局")
    if password == "布":
        print("你输了")