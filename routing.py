# coding=utf-8 

city = ['北京','上海','广州','深圳', '杭州', '南京','重庆']

for i in city:
    print(i)

print('------------------------------------')

i = 0
len = len(city)
while i < len:
    print(city[i])
    i = i + 1
    
print('----------------------------')

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
 
input("点击 enter 键退出")

