# python中通过空格缩进来判断层次关系
age = int(input("请输入你的年龄："))
if age > 18:
    print("恭喜，你成年了！")
elif age < 7:
    if age < 2:
        print("可爱捏")
    else:
        print("你是小屁孩哈哈！")
else:
    print("好好学习")

# 可以在判断语句中进行输入来简化程序 或者实现某些逻辑
if int(input("请输入你的身高（cm）：")) < 110:
    print("免票！")
elif int(input("请输入你的vip等级：")) > 3:
    print("免票！")
else:
    print("你得买全票")
