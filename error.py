# -*- codeing =utf-8 -*-
# @Time:2021/12/29 16:58
# @Author:XPein
# @File:error.py
try:
    print("=====1=====")
    f = open("test.txt", "r")  # 用只读模式打开了一个不存在的文件
    print("=====2=====")  # 这句代码不会被执行，发生了异常
except IOError:  # 如果是IOerror 执行 pass
    pass
try:
    print(num)
except (NameError, IOError) as result:  # 捕获所有的异常  except Exception:

    print("发生错误了")
    print(result)

# try...finally

try:
    f = open("...", "r")
except Exception:
    pass
finally:
    f.close()     # finally最后一定都会被执行的代码



