# 直接导入创建的py文件即可
"""
import my_module1
my_module1.add(1, 2)
"""

# 当导入多个相同的方法时，后导入的会进行覆盖
"""
from my_module1 import add
from my_module2 import add
add(6, 5)
"""

# 如果模块内定义了"__all__"变量，那import * 时只能导入变量定义的列表中的元素
"""from my_module1 import *
# test()  # 无法调用
add(3, 2)
"""
