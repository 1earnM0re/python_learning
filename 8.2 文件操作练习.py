"""
我们现在要做的就是:
读取文件
将文件写出到bill.txt.bak文件作为备份
同时，将文件内标记为测试的数据行丢弃

实现思路:
open和r模式打开一个文件对象，并读取文件
open和w模式打开另一个文件对象，用于文件写出
for循环内容，判断是否是测试，不是测试就write写出，是测试就continue跳过
将2个文件对象均close()
"""

fr = open("D:/PyCharm Community Edition 2023.3.3/bill.txt", "r", encoding="UTF-8")
fw = open("D:/PyCharm Community Edition 2023.3.3/bill.txt.bak", "w", encoding="UTF-8")
for line in fr:
    # line = line.strip()  # 若if处没有\n，那么加上注释的两句代码
    line_list = line.split(",")
    if line_list[4] == "测试\n":
        continue
    fw.write(line)
    # fw.write("\n")
fr.close()
fw.close()



