# 列表list使用中括号[]进行标识
# [元素1, 元素2, ...]
name_list = ["lin", "zheng", "fan"]

# 定义空列表
em_list1 = []
em_list2 = list()

# 可以通过下标索引来取出列表中的元素,索引超出取值范围便会报错
# 正向索引:0,1,2,3,...(从第一个元素开始)
# 逆向索引:-1,-2,-3,...(从最后一个元素开始)
print(name_list[0])
print(name_list[-1])
# 嵌套列表的元素的取出
double_list = [[1, 2, 3], [4, 5, 6]]
print(double_list[0][2])


# 列表的常用方法

# 1. 找到指定元素的下标,找不到就报错, list.index(元素)
print(name_list.index("lin"))

# 2. 修改列表中的元素
# 2.1 list.insert(位置, 元素), 将元素插入到列表的指定位置
name_list.insert(0, "nb")
print(name_list)
# 2.2 list.append(元素), 将元素追加到列表的末尾
name_list.append("666")
print(name_list)
# 2.3 list.extend(数据容器), 将数据容器中的元素依次取出插入到列表的指定位置
name_list.extend(["好好学习", "天天向上"])
print(name_list)

# 3. 删除列表中的元素
# 3.1 del list[下标], 删除指定下标元素
del name_list[0]
print(name_list)
# 3.2 list.pop(下标), 删除指定下标元素，并返回该元素
ret = name_list.pop(3)
print(f"{name_list}, 取出的元素是{ret}")
# 3.3 list.remove(元素), 从前往后寻找第一个匹配的元素，并将其删除
name_list.remove("好好学习")
print(name_list)
# 3.4 list.clear(), 清空列表
tmp_list = [1, 2, 3]
tmp_list.clear()
print(tmp_list)

# 4. 统计列表中某元素出现的次数, list.count(元素)
print(name_list.count("lin"))

# 5. 列表的长度, len(list)
print(len(name_list))

# 6. sort(key=选择排序依据的函数 ,reverse=True/False)方法
# 参数key，是要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据
# 参数reverse，是否反转排序结果，True表示降序，False表示升序
test_list = [['a', 1], ['b', 2], ['c', 4]]
def my_sort_order(element):
    return element[1]
test_list.sort(key=my_sort_order, reverse=True)
print(test_list)
# 传入lambda匿名函数
test_list.sort(key=lambda ele: ele[1], reverse=False)
print(test_list)

# 列表的遍历
# 利用while，可操作性高
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
# 利用for，简单高效
for x in name_list:
    print(x)
