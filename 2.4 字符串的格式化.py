# 1.通过占位符来格式化 %s %d %f
year = 2024
print("今年是%s年" % year)
loong = "龙"
print("今年是%d年，是%s年" % (year, loong))

# %d和%f可以添加m.n限制宽度（前面补空格）和精度
num = 11
price = 0.5
print("%d,%f" % (num, price))
print("%5d,%7.2f" % (num, price))
# 如果m比位数要小，则无效
print("%1d" % num)

# 2.通过f{}来格式化，不做精度控制
print(f"今年是{loong}年，年份是{2024}，辣条一包{price}元")

# 以上两种方法也可以格式化表达式
print("1+1 = %d" % (1+1))
print(f"2*2 = {2*2}")

