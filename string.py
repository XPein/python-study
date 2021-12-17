# -*- codeing =utf-8 -*-
# @Time:2021/12/14 22:22
# @Author:XPein
# @File:string.py
word = '这是一个字符串'
sentence = "这是一个句子"
paragraph = """
    这是一个段落
    是可以换行的
"""
print(paragraph)
print(word[0:3:1])
print(sentence[0:])  # 末尾坐标可以省略

print(word*3)
print(word+",是的没错")

print("hello\nfriends!")
print(r"hello\nfriends") # 当在打印的字符串前面加一个r时不对转译字符进行转译直接输出可以不改变爬取到的内容

