
# urlparse函数(有params)与urlsplit函数

from urllib import request,parse

url = 'http://www.baidu.com/s?username=zhiliao'
result1 = parse.urlsplit(url)
result2 = parse.urlparse(url)
print(result1)
print(result2)
print('scheme:',result1.scheme)
print('netloc:',result1.netloc)
print('path',result1.path)
print('query',result1.query)