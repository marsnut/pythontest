#coding=utf-8
from pyecharts import Bar

attr = ["Mon", "Feb", "Wed", "Thu", "Fri", "Sat", "Sun"]
v1 = [1.49, 2.09, 4.03, 2.23, 5.26, 7.71, 7.56]
v2 = [0.3, 0.9, 0.2, 0.4, 0.7, 0.7, 0.6]
v3 = [18.15, 13.22, 11.28, 17.99, 18.7, 19.7, 15.6]

bar = Bar("XXX情况总览", "本图表展示过去一周的ABC情况")
bar.add("A值", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.add("B值", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.add("C值", attr, v3, mark_line=["average"], mark_point=["max", "min"])    
bar.render('./tmp/111.html')        #在/tmp文件夹里生成一个111.html文件
