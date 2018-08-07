
from urllib import request,parse

"""
# 爬取拉勾数据

url = 'https://www.lagou.com/jobs/list_java?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=?labelWords=hot'
# 设置请求信息(浏览器身份)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

# headers=headers这样传参可以忽略参数的位置
req = request.Request(url=url,headers=headers)
resp = request.urlopen(req)
print(resp.read())
"""

# 爬取拉勾数据(真正数据),在positionAjax.json中
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
data = {
    'first':'true',
    'pn':1,
    'kd':'java'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_java?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=?labelWords=hot'
}
req = request.Request(url=url,data=parse.urlencode(data).encode('utf-8'),headers=headers,method='POST')
resp = request.urlopen(req)
# decode:将byte解码
print(resp.read().decode('utf-8'))
