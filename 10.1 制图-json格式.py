# json就是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互，
# 本质上是一个带有特定格式的字符串
# 语法：1.字典； 2.元素是字典的列表。
"""
{‘name':'Tom', 'age':10}
[{‘name':'Tom', 'age':10}, {‘name':'John', 'age':12}, {‘name':'Mary', 'age':18}]
"""
# 导入json模块
import json
# 准备符合json格式的数据
data = [{'name': 'Tom', 'age': 10}, {'name': 'John', 'age': 12}, {'name': 'Mary', 'age': 18}]
# 使用dumps()方法将python数据转化为json数据
data_json = json.dumps(data)
print(type(data_json))
# 使用loads()方法将json数据转化为python数据
data_python = json.loads(data_json)
print(data_python)
