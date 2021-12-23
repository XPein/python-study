# -*- codeing =utf-8 -*-
# @Time:2021/12/23 15:23
# @Author:XPein
# @File:shop.py

products = [["iphone", 6888], ["MacPro", 148000], ["小米11", 2499], ["coffee", 31], ["Book", 60], ["Nike", 699]]
i = 0
for product in products:

    print(i, product[0], "\t", product[1])
    i += 1
price = 0
shopcar = []
while 1:
    index = input("你想购买商品的编号：")
    if index == 'q':
        break
    index = int(index)                     # index 不强行规定数据类型会报错的
    shopcar.append(products[index])
for shop in shopcar:
    print(shop[0])
    price += shop[1]
print("total price = ", price)

