#!/usr/bin/env python
#coding=utf-8
from pyecharts import Bar, Grid

attr = ["一班", "二班", "三班", "四班"]
v1 = [54, 81, 32, 32] 
v2 = [68, 69, 27, 32] 
bar = Bar("赞成票","本图表展示赞成票情况")
bar.add("年纪长", attr, v1, mark_point=["max", "min"])
bar.add("副年纪长", attr, v2, mark_point=["max", "min"])

attr2 = ["一班", "二班", "三班", "四班"]
x1 = [2, 0, 0, 1]
x2 = [1, 3, 0, 2]
bar2 = Bar("反对票","本图表展示反对票情况",title_top='bottom',title_color='#1d12eb')            #title_color是标题颜色，这个跟html的颜色取值一样
bar2.add("年纪长", attr2, x1, mark_point=["max", "min"])
bar2.add("副年纪长", attr2, x2, mark_point=["max", "min"])

attr3 = ["一班", "二班", "三班", "四班"]
y1 = [2, 0, 0, 1]
y2 = [2, 0, 0, 1]
bar3 = Bar("弃权票","本图表展示弃权票情况",title_pos='right',title_color='#eb1212')             #title_pos是标题的位置，如果不特殊说明，会重叠
bar3.add("年纪长", attr3, y1, mark_point=["max", "min"])    
bar3.add("副年纪长", attr3, y1, mark_point=["max", "min"])

grid = Grid()    
grid.add(bar, grid_width="40%", grid_height="30%", grid_bottom="60%", grid_right="55%")        #grid_height和grid_width是每一个小图的大小
grid.add(bar2, grid_width="40%", grid_height="30%", grid_bottom="60%", grid_left="55%")        #grid_bottom和grid_top是垂直位置
grid.add(bar3, grid_width="40%", grid_height="30%", grid_top="60%", grid_right="55%")        #grid_right和grid_left是水平位置
grid.render('./tmp/grid.html')    #在/tmp文件夹里生成一个grid.html文件
