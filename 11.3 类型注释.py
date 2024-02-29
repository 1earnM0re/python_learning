# 1. 变量的类型注解
# 一般对无法直接看出变量类型的变量添加类型注解
# 可对变量、类对象、容器进行注解
"""
变量: 类型
"""
import random   # 可通过 alt + 回车 快捷键导包
from typing import Union    # 使用Union需要先导包

num1: int = 10
class Student:
    pass
stu: Student = Student()
list1: list = [1, 2, 3]
# 容器类型详细注解
list2: list[int] = [1, 2, 3]
tuple1: tuple[str, int, bool] = ("hi", 23, True)            # 元组类型设置类型详细注解，需要将每一个元素都标记出来
dict1: dict[str, int] = {"lin": 5, "zheng": 6, "fan": 7}    # 字典类型设置类型详细注解，需要2个类型，一个是key一个是value

# 也可以在注释中进行类型注解
"""
# type: 类型
"""
num2 = random.randint(1, 10)  # type: int


# 2. 函数（方法）的类型注解
"""
def 函数名(形参1: 类型, 形参2: 类型, ...) -> 返回值类型:
    函数体
"""
def add(a: int, b: int) -> int:
    return a + b
add(5, 6)


# 使用Union类型进行混合类型注解
list3: list[Union[str, int]] = [1, 2, "haha"]   # 表示list里面既有字符串又有整数
dict2: dict[str, Union[str, int]] = {"name": "linzhf", "age": 19}   # 表示字典里面key都是str，value既有str又有int
