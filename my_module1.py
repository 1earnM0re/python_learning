# __all__变量控制 import * 能导入的方法，用列表以字符串为元素定义
__all__ = ["add"]


def add(x, y):
    print(x + y)


def test():
    print("test函数")


# 测试代码前要加if语句（输入main自动弹出），否则调用模块时也会执行测试代码
if __name__ == '__main__':  # 当运行该文件时才会进入if语句中
    add(5, 6)
