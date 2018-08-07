# encoding: utf-8

# 导入urllib中指定的包
from urllib import request

"""
# urlopen函数
resp = request.urlopen('http://www.baidu.top/')
print(resp.readline())
"""

"""
# urlretrieve函数
# 将百度首页下载到本地
request.urlretrieve('http://www.baidu.com','baidu.html')

# 下载图片
request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1533566044817&di=7692eeb3301d0433a8e0f8d73da19b0e&imgtype=0&src=http%3A%2F%2Fu.candou.com%2F2017%2F0613%2F1497342507815.jpg'
    ,'luban.jpg')
"""

"""
# urlencode函数的用法
from urllib import parse
param = {'name':'张三','age':18,'greet':'Hello World'}
result = parse.urlencode(param)
print(result)

# 编码并请求
url = 'https://www.baidu.com/s?ie=UTF-8&'
param = {'wd':'刘德华'}
result = parse.urlencode(param)
result = url + result
ps = request.urlopen(result)
print(ps.read())
"""


# 解码函数：parse_qs
from urllib import parse
param = {'name':'张三','age':18,'greet':'Hello World'}
result = parse.urlencode(param);
qs = parse.parse_qs(result)
print(qs)

