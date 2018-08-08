
import requests

"""
# 基本POST请求
req = requests.post('http://www.baidu.com')
print(req.content.decode('utf-8'))
"""

# 传入data数据,比如请求拉勾网的数据
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}
data = {
    'first':'true',
    'pn':1,
    'kd':'python'
}
resp = requests.post(url=url,headers=headers,data=data)
print(resp.content.decode('utf-8'))
