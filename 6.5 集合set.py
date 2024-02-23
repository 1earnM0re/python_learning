# 集合用大括号{}来标识
# {元素1, 元素2, ...}
set1 = {1, 2, 3, 4, 5}
# 空集合的定义
set0 = set()
print(f"set0的内容是{set0}")

# 集合不允许重复元素（自带去重）
set2 = {1, 2, 3, 4, 5, 1, 2, 3}
print(f"set2的内容是{set2}")

# 集合的元素是无序的，所以并不支持下标索引，也不支持while循环，只能for循环
set3 = {"lin", "zheng", "fan"}
print(f"set3的内容是{set3}")

# 集合允许修改
# 常用方法有：

# 1. add(元素) 向集合内添加一个元素
set1.add(6)
print(f"添加元素后set1的内容是{set1}")

# 2. remove(元素) 删除集合内指定元素
set1.remove(6)
print(f"删除元素后set1的内容是{set1}")

# 3. pop() 随机取出集合内的一个元素，并将其返回
ele = set1.pop()
print(f"随机取出元素后set1的内容是{set1}，取出的元素是{ele}")

# 4. clear() 清空集合
set2.clear()
print(f"清空集合后set2的内容是{set2}")

# 5.1 集合1.difference(集合2) 返回集合1对集合2的差集，不改变两个集合
set1 = {1, 2, 3, 4, 5}
set4 = {1, 2, 3, 9, 10}
set5 = set1.difference(set4)
print(f"取差集后得到set5的内容是{set5}")
# 5.2 集合1.difference_update(集合2) 将集合1置为集合1对集合2的差集，不改变集合2
set1.difference_update(set4)
print(f"取差集后set1的内容是{set1}")

# 6. 集合1.union(集合2) 将集合1和集合2合并后返回，不改变两个集合
set1 = {1, 2, 3, 4, 5}
set4 = {1, 2, 3, 9, 10}
set6 = set1.union(set4)
print(f"合并后set6的内容是{set6}")

# 7. len(集合) 求集合长度
