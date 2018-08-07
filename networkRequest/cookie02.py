
# 将cookie信息保存到本地文件
from urllib import request
from http.cookiejar import MozillaCookieJar

# # 指定保存到cookie.txt文件中
cookiejar = MozillaCookieJar('cookie.txt')

handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://www.baidu.com')

# ignore_discard=True 将过期的cookie信息也保存
cookiejar.save(ignore_discard=True)





# ######################################

# 从本地文件中读取cookie信息
cookiejar2 = MozillaCookieJar('cookie.txt')
# 导入cookie(包含过期的)
cookiejar2.load(ignore_discard=True)
handler2 = request.HTTPCookieProcessor(cookiejar2)
opener2 = request.build_opener(handler2)
# 循环打印cookie信息
for cookie in cookiejar2:
    print(cookie)
