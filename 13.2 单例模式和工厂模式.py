# 单例模式
# 对一个类,只获取其唯一的类实例对象，持续复用它
# 优点：节省内存；节省创建对象的开销

from test_tool import tool
# tool是在test_tool中被实例化的对象
"""
class Tool:
    pass
    
tool = Tool()
"""
tool1 = tool
tool2 = tool
print(id(tool1))
print(id(tool2))

# 工厂模式
# 将对象的创建由 使用原生类本身创建 转换到 由特定的工厂方法来创建
# 优点：大批量创建对象的时候有统一的入口，易于代码维护当发生修改，仅修改工厂类的创建方法即可
# 符合现实世界的模式，即由工厂来制作产品(对象)
class Person:
    pass

class Student(Person):
    pass
class Teacher(Person):
    pass
class Worker(Person):
    pass

class PersonFactory:    # 工厂类
    def getperson(self, char):
        if char == "w":
            return Worker()
        elif char == "s":
            return Student()
        else:
            return Teacher()

pf = PersonFactory()
p1 = pf.getperson("w")
p2 = pf.getperson("s")
p3 = pf.getperson("t")
print(type(p1))
print(type(p2))
print(type(p3))
