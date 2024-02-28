# 如果想要做出数据可视化效果图，可以借助pyecharts模块来完成
# 官网是 pyecharts.org 可以查看使用文档
# 网站 gallery.pyecharts.org 可以查看各种图表效果

# 导入模块
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts  # 导入设置选项的包

# 创建折线图对象
line = Line()

# 给对象添加x轴数据
line.add_xaxis(["中国", "美国", "日本"])

# 给对象添加y轴数据，先输入名字再输入数据
line.add_yaxis("GDP", [100, 70, 60])

# 设置set_global_opt()来设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="中美日三国3024年GDP", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 使用render()方法，生成图表
line.render("中美日三国GDP折线图.html")
