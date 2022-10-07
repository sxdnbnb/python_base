# _*_coding : utf-8 _*_
# @Time : 2022/7/25 16:05
# @Author : SunShine
# @File : python_解析_bs4爬取星巴克数据
# @Project : python基础_爬虫

import urllib.request

url='https://www.starbucks.com.cn/menu/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
# print(content)

from bs4 import BeautifulSoup

soup=BeautifulSoup(content,'lxml')
# //ul[@class="grid padded-3 product"]//strong
name_list=soup.select('ul[class="grid padded-3 product"] strong')
for name in name_list:
    print(name.get_text())

