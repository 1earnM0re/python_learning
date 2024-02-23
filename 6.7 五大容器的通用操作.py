# 都支持for循环

# len()、max()、min()，求长度、最大值、最小值
# 字符串的大小比较：比较ASCII码：A-65, a-97, 0-48

# 容器相互转化：list(), tuple(), str(), set(), 字典转其他容器会丢失value

# sorted(容器, [reverse = True]), 从小到大排序容器, 传入reverse = True时将倒序排序，将排序好的元素存储在列表中返回
# 排序字典会丢失value
tuple1 = (1, 2, 5, 4, 3)
ordered_tuple = sorted(tuple1)
print(f"正序排序为：{ordered_tuple}")
ordered_tuple = sorted(tuple1, reverse=True)
print(f"逆序排序为：{ordered_tuple}")
