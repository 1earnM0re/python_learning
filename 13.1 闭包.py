# 优点:1.不定义全局变量，也可以让函数持续访问和修改一个外部变量；2.闭包函数引用的外部变量，是外层函数的内部变量，作用域封闭难以被误操作修改
# 缺点:额外的内存占用

def outer(logo):    # logo难以被修改
    def inner(msg):

        # 如果想要在内部函数修改外部函数的变量值，可以使用nonlocal关键字声明
        # nonlocal logo = "linzaifeng"

        print(f"{logo},{msg}")
    return inner    # 返回内部函数，即闭包函数


fn1 = outer("linzhengfan")  # fn1类型是函数
fn1("zhenshuai!")
