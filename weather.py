#! python3
import requests

req=requests.get('http://www.weather.com.cn/data/sk/101010100.html')
req.encoding='utf-8'
json = req.json()
data = json['weatherinfo']

print("城市: " + data['city'])
print("温度: " + data['temp'])
print("湿度: " + data['SD'])
print("风向: " + data['WD'])
print("风速: " + data['WS'])
print("雨水: " + data['rain'])
