# 异常具有传递性，捕获最高层的异常即可
# 1. 常规捕获异常，可以捕获所有异常，但不推荐
try:
    1/0
except:
    print("出现异常")

# 2. 捕获特定异常。如果出现的异常类型和指定的异常不一致，则无法捕获
try:
    print(a)
except NameError as e:
    print(f"出现异常，具体为：{e}")

# 3. 捕获多个异常。如果出现的异常类型和指定的异常不一致，则无法捕获
try:
    print(a)
except (NameError, ZeroDivisionError):
    print("出现NameError或ZeroDivisionError")

# 4. 捕获所有异常
try:
    1/0
except Exception as e:
    print(f"出现异常，具体是：{e}")

# 异常else语句，表示没有异常时执行的语句
try:
    num = 1
except Exception as e:
    print(f"出现异常，具体是：{e}")
else:
    print("没有异常")

# 异常finally语句，标识无论有没有异常都会执行的语句，常关闭文件
fr = None
try:
    fr = open("D:/PyCharm Community Edition 2023.3.3/test.txt", "r", encoding="UTF-8")
except Exception as e:
    print(f"出现异常，具体是：{e}")
finally:
    if fr:
       fr.close()
