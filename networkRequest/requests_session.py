
"""
# cookie
import requests
url = 'http://www.renren.com/PLogin.do'
data = {
    'email':'970138074@qq.com',
    'password':'pythonspider'
}
resp = requests.get('http://www.baidu.com')
print(resp.cookies)
print(resp.cookies.get_dict())
"""


# #####################################

"""
# session
import requests
url2 = 'http://www.renren.com/PLogin.do'
data2 = {
    'email':'970138074@qq.com',
    'password':'pythonspider'
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
# 登陆
session = requests.session()
session.post(url=url2,data=data2,headers=headers)
resp = session.get('http://www.renren.com/880151247/profile')
print(resp.content.decode('utf-8'))
"""


# ###################################
# 处理不信任的SSL证书
import requests
resp2 = requests.get('http://www.12306.cn/mormhweb/',verify=False)
print(resp2.content.decode('utf-8'))
