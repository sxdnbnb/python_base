# _*_coding : utf-8 _*_
# @Time : 2022/8/1 17:05
# @Author : SunShine
# @File : python_requests_基本使用
# @Project : python基础_爬虫

import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)

# 一个类型和六个属性
# Response类型
# print(type(response))

# 设置响应的编码格式
# response.encoding = 'utf-8'

# 以字符串的形式来返回了网页的源码
# print(response.text)

# 返回一个url地址
# print(response.url)

# 返回的是二进制的数据
content=response.content.decode('utf-8')
print(content)

# 返回响应的状态码
# print(response.status_code)

# 返回的是响应头
# print(response.headers)
