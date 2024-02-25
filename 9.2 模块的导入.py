# 模块就是一个py文件，里面有类、函数、变量等，我们可以导入模块使用它们
# [from 模块名] import[模块名/ 类/ 函数/ 变量/ *] [as 别名]， []表示可加可不加，*表示所有内容
# 一般在文件顶部导入模块

# 常见组合：（导入什么就调用什么）
# import 模块名
"""
import time
print("程序暂停五秒")
time.sleep(5)
print("程序继续运行")
"""
# from 模块名 import 类/ 变量/ 方法等
"""
from time import sleep
print("程序暂停五秒")
sleep(5)
print("程序继续运行")
"""
# from 模块名 import *
"""
from time import *
print("程序暂停五秒")
sleep(5)
print("程序继续运行")
"""
# import 模块名 as 别名
"""
import time as t
print("程序暂停五秒")
t.sleep(5)
print("程序继续运行")
"""
# from 模块名 import 方法 as 别名
"""
from time import sleep as s
print("程序暂停五秒")
s(5)
print("程序继续运行")
"""




