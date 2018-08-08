import requests

# get请求
response = requests.get('http://www.baidu.com')

# 获取网页方式1
# print(type(response.text))
# print(response.text)


# 获取网页方式2
# print(type(response.content))
# print(response.content.decode('utf-8'))


# 获取url
print(response.url)

# 获取响应码
print(response.status_code)

# 获取编码
print(response.encoding)