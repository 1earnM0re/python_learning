# 1. 封装 表示的是将现实世界事物的:属性、行为封装到类中，描述为：成员变量、成员方法
class Phone:
    time = None
    # 私有变量，在变量名前加"__"，私有变量无法被类对象赋值，也无法访问。可以被类成员访问、赋值
    __current_vol = None
    owner = "human"

    def __init__(self, time, __current_vol):    # 可以在构造函数中给私有变量赋初值
        self.time = time
        self.__current_vol = __current_vol

    # 私有方法，在函数名前加"__"，私有方法无法被类对象使用。可以被类成员使用
    def __keep_single_core(self):
        print("保持单核运行")

    def call_by_5g(self):
        if self.__current_vol >= 20:
             print("5g通话")
        else:
            print("电量低，无法5g通话，为保证通话质量，开启单核运行")
            self.__keep_single_core()
    def show_v(self):
        return self.__current_vol


phone1 = Phone("10:40", 30)
phone1.call_by_5g()

# 继承
# 多继承时，如果父类中有同名的方法、成员，先继承的优先级高于后继承的（从左到右）
"""
class 类名(父类1, 父类2, ...):
    类内容
"""

# 2. 继承
# 子类构建的类对象，可以有自己的成员变量和成员方法，并可以使用父类的成员变量和成员方法
# 子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写。即:在子类中重新定义同名的属性或方法即可。
class Xiaomi(Phone):
    owner = "LeiJun"
    def nfc(self):
        print("nfc功能")

    def __keep_single_core(self):
        print("保持小米专业单核运行")

    def call_by_5g(self):
        if self.show_v() >= 20:
             print("5g通话")
        else:
            print("电量低，无法5g通话，为保证通话质量，开启单核运行")
            self.__keep_single_core()

    # 复写父类方法|成员后，可以通过 父类.方法|成员或者super().方法|成员 来调用父类的方法|成员
    def show_owner(self):
        print(f"手机的创始人是{super().owner}，Xiaomi的创始人是{self.owner}")


xiaomi1 = Xiaomi("11:37", 10)
xiaomi1.call_by_5g()
xiaomi1.show_owner()


# 3. 多态，即完成同样的行为时，不同的对象会得到不同的状态
class Animal:   # 抽象类
    def speak(self):    # 抽象方法
        pass    # 空实现，pass作用是满足语法
class Dog(Animal):
    def speak(self):
        print("汪汪汪！")
class Cat(Animal):
    def speak(self):
        print("喵喵喵！")


def make_sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()
make_sound(dog)
make_sound(cat)

