# 包就是一个文件夹，里面有一个"__init__"文件作为包的标志，包用来包含多个模块
from my_package import my_module3
my_module3.add(1, 2)

import my_package.my_module3
my_package.my_module3.add(5, 6)

from my_package.my_module3 import add
add(3, 4)

# 如果包的"__init__"文件内定义了"__all__"变量，那import * 时只能导入变量定义的列表中的元素
"""
from my_package import *
my_module4.add(1, 2)  # 无法调用
"""
