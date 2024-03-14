# 闭包
# 优点:1.不定义全局变量，也可以让函数持续访问和修改一个外部变量；2.闭包函数引用的外部变量，是外层函数的内部变量，作用域封闭难以被误操作修改
# 缺点:额外的内存占用

def outer1(logo):    # logo难以被修改
    def inner(msg):

        # 如果想要在内部函数修改外部函数的变量值，可以使用nonlocal关键字声明
        # nonlocal logo = "linzaifeng"

        print(f"{logo},{msg}")
    return inner    # 返回内部函数，即闭包函数


fn1 = outer1("linzhengfan")  # fn1类型是函数
fn1("zhenshuai!")


# 装饰器就是使用创建一个闭包函数，在闭包函数内调用目标函数。可以达到不改动目标函数的同时，增加额外的功能。
# 写法1：
def outer2(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner

def sleep():
    import time
    import random
    time.sleep(random.randint(1, 4))

fn = outer2(sleep)
fn()


# 写法2：（装饰糖）
def outer3(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner

@outer3     # @后直接调用函数就不用定义函数对象
def sleep2():
    import time
    import random
    time.sleep(random.randint(1, 4))

sleep2()
