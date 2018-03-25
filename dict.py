#! python3
# coding=utf-8

import urllib.request

url = 'http://120.77.214.194:8090/xwtools/dict.php?word=%s'

word = input("请输入单词：")

url = url % (word)
res = urllib.request.urlopen(url)
data = res.read().decode('utf-8', 'ignore')
print(data)

