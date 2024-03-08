from pymysql import Connection  # 导入链接

# 创建到mysql数据库的链接
conn = Connection(
    host="localhost",           # 将主机设置为本地主机localhost
    port=3306,                  # 将端口设置为3306
    user="root",                # 用户名
    password="lzf18718316878",  # 密码
    autocommit=True             # 自动确认，设为Ture后修改数据无需手动使用commit()确认
)

# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("world")

# 使用游标对象.execute()执行sql语句
# cursor.execute("create table test_student(id int);")        # 创建表
cursor.execute("select * from city;")                       # 选择表city中的全部数据

# 执行选择语句可以通过fetchall()方法获取返回数据，数据以元组类型返回
"""
res = cursor.fetchall()
for r in res:
    print(r)
    """

# 对表进行插入和修改数据等操作需要进行确认
cursor.execute("insert into test_student values(6);")
# conn.commit()   # 使用commit()方法确认

cursor.close()

# 以下是sql语法
"""
1. 创建数据库：create database 数据库名称
2. 删除数据库|表：drop database|table 数据库|表名称
3. 查看数据库|表：show databases|tables
4. 创建表：create table 表名称(列名称 列类型, 列名称 列类型, ...)
    类型有：int-整数，float-浮点数，varchar-字符串（字符串在sql语句中需要用单引号''包围起来），date-日期类型，timestamp-时间戳类型
5. 插入数据：insert into 表名称[(列1, 列2, ...)] values(值1, 值2, ...)[,(值1, 值2, ...)]
6. 删除数据：delete from 表名称 [where 条件判断]
7. 更新数据：update 表名称 set 列=值 [where 条件判断]
8. 查询数据：select 列名称|* from 表名称 [where 条件判断]
9. 分组聚合：select 列, 聚合函数 from 表名称 [where 条件判断] group by 列
    聚合函数有：sum(列)-求和，avg(列)-求平均值，min(列)-求最小值，max(列)-求最大值，count(列|*)-求数量
10. 结果排序：分组聚合：select 列, 聚合函数 from 表名称 [where 条件判断] group by 列 order by 列 [asc|desc] limit n[,m]
    排序默认为asc升序，desc为降序；limit后一个参数表示只看前n个，两个参数表示只看除去前n个的前m个
"""