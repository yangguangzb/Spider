
# 使用requests添加代理
import requests

url = 'http://httpbin.org/get'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
proxy = {
    'http':'115.223.193.70:9000'
}
resp = requests.get(url=url,headers=headers,proxies=proxy)
print(resp.content.decode('utf-8'))
