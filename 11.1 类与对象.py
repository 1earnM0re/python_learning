"""
class 类名称:   （class是关键字，表示要定义类了）
    类的属性    （即定义在类中的变量(成员变量)）
    类的行为    （即定义在类中的函数(成员方法)）
"""


class Student:
    # 成员变量
    """name = None
    age = None
    score = None"""

    # __init__()方法 可以初始化成员变量（即构造函数），使用后无需单独定义成员变量
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # __str__()方法 可以在输出类对象时输出指定内容，而不是对象的地址
    def __str__(self):
        return f"我的名字是{self.name}，今年{self.age}岁"

    # __lt__()方法 实现判断类对象的大于 小于
    def __lt__(self, other):
        return self.age < other.age

    # __le__()方法 实现判断类对象的大于等于 小于等于
    def __le__(self, other):
        return self.age <= other.age

    # __eq__()方法 实现判断类对象的等于
    def __eq__(self, other):
        return self.age == other.age

    # 成员方法，需要传入self，在方法内部访问成员变量必须使用self。使用时不需要传入self
    def say_hi(self, msg):
        print(f"我是{self.name}，{msg}")


stu1 = Student("小明", 18, 100)    # 构建类对象
stu1.say_hi("你好")
print(stu1)
stu2 = Student("小红", 20, 90)
print(stu1 < stu2)
print(stu1 <= stu2)
print(stu1 == stu2)
