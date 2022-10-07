# _*_coding : utf-8 _*_
# @Time : 2022/7/8 16:25
# @Author : SunShine
# @File : python_urllib_get请求
# @Project : python基础


# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

# 需求 获取 https://www.baidu.com/s?wd=周杰伦的网页源码

# import urllib.request
# import urllib.parse
#
# url = 'https://www.baidu.com/s?wd='
#
# # 请求对象的定制为了解决反爬的第一种手段
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
# }
#
# # 将周杰伦三个字变成 unicode编码 的格式
# # 我们需要依赖于urllib.parse
# name = urllib.parse.quote('周杰伦')  # quote用于只有一个参数
#
# url = url + name
#
# # 请求对象的定制
# request = urllib.request.Request(url=url,headers=headers)
#
# # 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(request)
#
# # 获取响应的内容
# content = response.read().decode('utf-8')
#
# # 打印数据
# print(content)



# urlencode应用场景：多个参数的时候


# https://www.baidu.com/s?wd=周杰伦&sex=男

# import urllib.parse
#
# data = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾省'
# }
#
# a = urllib.parse.urlencode(data)
# print(a)


#获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7的网页源码

import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url + new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码的数据
content = response.read().decode('utf-8')

# 打印数据
print(content)










