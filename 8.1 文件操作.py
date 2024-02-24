# 1. 打开文件 open(name, mode, encoding = "UTF-8"), 返回一个文件对象
# name是打开文件名字或路径的字符串, mode是打开文件的方式（读"r"，写"w"，追加"a"）, encoding是编码格式

# 2. 读写文件 read() readline() readlines() write()

# 3. 关闭文件 close()

# flush() 刷新文件，使修改保存到硬盘中; close()内置flush()
# 在 with open语句中进行文件操作可以自动关闭文件，避免遗忘关闭文件
# with open(name, mode, encoding="UTF-8") as f:
with open("D:/PyCharm Community Edition 2023.3.3/test.txt", "r", encoding="UTF-8") as f:
    content = f.readlines()
    print(content)

# 以只读方式打开test.txt
fr = open("D:/PyCharm Community Edition 2023.3.3/test.txt", "r", encoding="UTF-8")

# 1. read(num), 读取文件中前num个字符并返回，不传入num则读取文件全部内容
"""
content = fr.read(6)
print(content)
content = fr.read()
print(content)
"""
# 2. readlines(), 读取文件全部内容，并以列表类型返回，每行字符是一个元素
"""
content = fr.readlines()
print(content)
"""
# 3. readline(), 读取文件一行内容并返回
"""
line1 = fr.readline()
line2 = fr.readline()
line3 = fr.readline()
print(line1)
print(line2)
print(line3)
"""
# 不管调用什么方法，每次读取都会从上次读取结束的位置开始
# \n也会被读取到

# for循环读取line
"""
for line in fr:
    print(f"这一行是：{line}")
"""

# 以写的方式打开文件。如果文件不存在，则会创建新文件；如果文件已存在，则会清空内容
fw = open("D:/PyCharm Community Edition 2023.3.3/test.txt", "w", encoding="UTF-8")

# write(content) 将字符串content写入文件中
"""
fw.write("你好林政帆！")
fw.close()  # 刷新文件，以让改写保存
"""

# 以追加的方式打开文件。如果文件不存在，则会创建新文件；如果文件已存在，则会追加内容到已有内容后
fa = open("D:/PyCharm Community Edition 2023.3.3/test.txt", "a", encoding="UTF-8")

# write(content) 将字符串content写入文件中
"""
fw.write("你好林政帆！")
fw.close()  # 刷新文件，以让改写保存
"""
