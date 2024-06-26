# _*_coding : utf-8 _*_
# @Time : 2022/7/13 15:33
# @Author : SunShine
# @File : python_豆瓣电影
# @Project : python基础

#get请求

import urllib.request

url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}

# (1)请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# (2)获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)

# (3) 数据下载到本地
# open方法默认情况下使用的是gbk的编码  如果我们要想保存汉字 那么需要在open方法中指定编码格式为utf-8
fp = open('douban.json','w',encoding = 'utf-8')
fp.write(content)

# with open('douban.json','w',encoding='utf-8')as fp:
#     fp.write(content)


