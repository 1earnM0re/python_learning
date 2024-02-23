"""
def 函数名(传入参数):
    函数体
    return返回值
"""

# 无返回值时返回None，或者手动return None
def fun1():
    print("fun1调用")
# None相当于false，可结合if语句进行判断
ret = fun1()
if not ret:
    print("返回None")

# 使用global关键字声明，使函数内局部变量影响全局变量
def fun2():
    global num
    num += 10
    return None
num = 10
fun2()
print(num)

# 使用函数说明文档来介绍函数，在函数声明后使用三双引号注释即可,之后在函数调用时将鼠标悬停在传参上可以看到说明文档
def fun3_add(x,y):
    """
    fun3_add用来将两数相加并返回结果
    :param x: 第一个加数
    :param y: 第二个加数
    :return: 相加的结果
    """
    res = x + y
    return res
num = fun3_add(5, 6)
