# _*_coding : utf-8 _*_
# @Time : 2022/7/20 15:46
# @Author : SunShine
# @File : python_urllib_代理
# @Project : python基础_爬虫

import urllib.request
import random

url = 'http://www.baidu.com/s?wd=ip'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}

# 请求对象的定制
request = urllib.request.Request(url = url,headers= headers)

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

proxies_pool = [
    {'http':'39.108.156.112'},
    {'http':'132.226.5.252'},
]
# print(type(proxies_pool))     #列表
proxies = random.choice(proxies_pool)

# proxies = {
#     'http':'112.14.40.137'
# }

# handler  build_opener  open

handler = urllib.request.ProxyHandler(proxies = proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应的信息
content = response.read().decode('utf-8')

# 保存
with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)






