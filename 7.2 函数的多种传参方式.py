# 1. 位置参数
# 按照函数参数位置依次传入参数
def fun1(name, age, gender):
    print(f"{name}, {age}岁, 性别{gender}")
fun1("小明", 11, "男")

# 2. 关键字参数
# 按照"key=value"的形式传入参数，不限传入顺序
# 与位置参数混合使用时，位置参数必须在前面
def fun2(name, age, gender):
    print(f"{name}, {age}岁, 性别{gender}")
fun2("小李", gender="男", age=13)

# 3. 缺省参数
# 不传入参数时使用默认的参数值
# 缺省参数必须定义在最后
def fun3(name, age, gender='女'):
    print(f"{name}, {age}岁, 性别{gender}")
fun3("小红", 18)

# 4. 不定长参数
# 4.1 传入关键字(key=value)之外的参数，用*标记形式参数，以元组的形式接收参数，形式参数一般命名为 args
def fun4(*args):
    print(f"类型是：{type(args)}，内容是：{args}")
fun4(1, 3, 5, 7)

# 4.2 传入关键字类型(key=value)的参数，用**标记形式参数，以字典的形式接收参数，形式参数一般命名为 kwargs
def fun5(**kwargs):
    print(f"类型是：{type(kwargs)}，内容是：{kwargs}")
fun5(name="lin", age=19)
