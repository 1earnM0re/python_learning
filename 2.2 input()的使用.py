# 从键盘中获取输入——无论输入什么都转化为字符串
name = input("请输入你的名字：")
print(f"{name},类型是：{type(name)}")
num1 = input("请输入你的年龄：")
print(f"{num1},类型是：{type(num1)}")

# 如果想输入整数或者浮点数，需要类型转换
num2 = int(input("请输入你爸爸的年龄："))
print(f"{num2},类型是：{type(num2)}")
