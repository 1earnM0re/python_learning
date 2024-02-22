print("hello world!")
print("hello world!!!")

# print语句自动换行，不换行需要通过传参来实现
print("Hello", end='')
print("World!")

# 制表符 \t 可以实现上下行单词对齐
# \t 作用为补全前面字符串的位数到4的整数倍。
# 若\t前面没有字符/字符串，则在前面直接补4个空格；
# 若前面有3个字符\字符串，则补1个空格；
# 若有5个字符\字符串，则补上3个空格；
# 若已经满4个，则补上4个空格

print("hello\tworld!")
print("helloo\tworld!")
