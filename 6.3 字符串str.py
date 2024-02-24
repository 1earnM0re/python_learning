# 字符串也有下标索引，而且不能改变其中国素，若改变字符串的元素则需要用新字符串接收
my_string = "lin zheng fan"
print(my_string[6])
print(my_string[-7])

# 常用的方法：
# index() 查找指定字符（串）的下标索引
print(f"{my_string}中zheng的下标是{my_string.index("zheng")}")

# replace(str1, str2) 将字符串中的str1替换为str2
my_new_string1 = my_string.replace("zheng fan", "zai feng")
print(my_new_string1)

# strip(str=" ") 删除字符串首尾的str(默认为空格和换行符)
my_new_string2 = my_string.strip("l")
print(my_new_string2)

# split(str) 其中str为分隔符，按照分隔符将字符串分为多个字符串，并存放在列表中
my_list = my_string.split(" ")
print(my_list)

# count()
# len()
