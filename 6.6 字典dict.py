# 字典通过大括号{}来进行标识，与集合相同，但是元素是键值对
# {key:value, key:value, ...}
# key不可重复，重复添加将会覆盖原值
dict1 = {"lin": 1, "zheng": 2, "fan": 3}
print(dict1)

# 空字典的定义
em_dict1 = {}
em_dict2 = dict()

# 字典不用下标索引，而是用key值查询对应的value，故不可以while循环
print(f'dict1中key为\"lin\"的value是{dict1["lin"]}')

# key不可为字典，value可为任何类型，可以嵌套字典
dict2 = {
    "张三": {
        "语文": 88,
        "数学": 77,
        "英语": 66
    },
    "李四": {
        "语文": 99,
        "数学": 98,
        "英语": 97
    }
}
print(f'dict2中李四的数学成绩是{dict2["李四"]["数学"]}')

# 字典常用的方法有：

# 1. 字典[key] = value 添加或修改字典的元素
dict1["666"] = 4
print(dict1)

# 2. pop(key) 删除字典中键值为key的元素并将其value返回
ele = dict1.pop('666')
print(f"取出元素后dict1的内容是{dict1}，取出的元素的value是{ele}")

# 3. keys() 获取所有的key
keys = dict1.keys()
print(f"获取到所有的key:{keys}, 类型是{type(keys)}")

# 4. clear() 清空字典
# 5. len() 求字典长度

# 两种for循环：
for key in keys:
    print(dict1[key])
for key in dict1:
    print(dict1[key])
