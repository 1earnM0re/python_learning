# 函数作为参数传入函数
# 这是参数已定，逻辑未定，属于函数逻辑的传递
# 之前传入数据是函数体的逻辑已定，参数的数据未定，属于数据的传递
def fun(compute):
    result = compute(4, 3)
    print(result)
def compute(x, y):
    return x + y  # compute也可以是加减乘除各种操作，所以说传递的是未定的逻辑
fun(compute)

# 匿名函数使用lambda关键字标识
# lambda 传入参数: 函数体（一行代码）
# 限制：lambda匿名函数用于临时构建函数，只使用一次的场景；只能执行一行代码，并将结果返回
fun(lambda x, y: x**y)  # x**y 是x的y次方
