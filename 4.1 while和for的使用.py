# while 条件:
#     执行内容
i = 0
while i < 2:
    print("这是while循环")
    i += 1

# for 临时变量 in 待处理数据集:
#     执行内容
name = "python"
for x in name:
    print(x)

# range()语句能获得一个数字序列，常与for组合
# 1.range(num1) 产生一个从0到num1的序列（不包括num1)，步长为1
for x in range(3):
    print(x)

# 2.range(num1,num2) 产生一个从num1到num2的序列（不包括num2)，步长为1
for x in range(1, 3):
    print(x)

# 1.range(num1,num2,step) 产生一个从num1到num2的序列（不包括num1)，步长为step
for x in range(1, 10, 2):
    print(x)
