# _*_coding : utf-8 _*_
# @Time : 2022/8/8 14:53
# @Author : SunShine
# @File : python_用腾讯云识别验证码
# @Project : python基础_爬虫

# _*_coding : utf-8 _*_
# @Time : 2022/8/3 17:34
# @Author : SunShine
# @File : python_requests_验证码登陆古诗文网
# @Project : python基础_爬虫


import tencent_orc
# 通过登陆  然后进入到主页面

# 通过找登陆接口我们发现 登陆的时候需要的参数很多
# __VIEWSTATE: lEslFFJ+MDqQejt0XiXLM0mqjtPLvWjIZVA0X2bfjCY1ijhD+HpTtgJ06gTshswPEu8axqTSL9hF7295YeDWkE3sPzJ0a04l330Pzs24s0W+kICa1NQ8sM1gyNlKF3K/GD8jzacjkwa8dxYQ+UNIGLBrfpo=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 15584664617
# pwd: 12345678
# code: 1111
# denglu: 登录

# 我们观察到_VIEWSTATE   __VIEWSTATEGENERATOR  code是一个可以变化的量

# 难点:(1)_VIEWSTATE   __VIEWSTATEGENERATOR  一般情况看不到的数据 都是在页面的源码中
#     我们观察到这两个数据在页面的源码中 所以我们需要获取页面的源码 然后进行解析就可以获取了
#     (2)验证码

import requests

# 这是登陆页面的url地址
url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}
# 获取页面的源码
response=requests.get(url=url,headers=headers)
content=response.text

# 解析页面源码  然后获取_VIEWSTATE   __VIEWSTATEGENERATOR
from bs4 import BeautifulSoup

soup = BeautifulSoup(content,'lxml')

# 获取_VIEWSTATE
viewstate=soup.select('#__VIEWSTATE')[0].attrs.get('value')
# print(viewstate)

# 获取__VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# print(viewstategenerator)

# 获取验证码图片
code=soup.select('#imgCode')[0].attrs.get('src')
# print(code)
code_url='https://so.gushiwen.cn'+code
# print(code_url)


# 有坑
# 下载到本地
# import urllib.request
# urllib.request.urlretrieve(url=code_url,filename='code.jpg')

# requests里面有一个方法 session（）  通过session的返回值 就能使用请求变成一个对象
session = requests.session()
# 注意此时要使用二进制数据  因为我们要使用的是图片的下载
response_code = session.get(code_url)
content_code = response_code.content
# wb的模式就是将二进制数据写入到文件
with open('code.png','wb')as fp:
    fp.write(content_code)

# 获取了验证码的图片之后 下载到本地 识别后就可以将这个值给code的参数 就可以登陆
code_picture='code.png'
code_name = tencent_orc.tencent_orc(code_picture)
# print(code_name)

# 点击登陆
# url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '15584664617',
    'pwd': '12345678',
    'code': code_name,
    'denglu': '登录',
}

response_post=session.post(url=url,data=data_post,headers=headers)
# content_post=response_post.text
# with open('gushiwen.html','w',encoding='utf-8') as fp:
#     fp.write(content_post)
from lxml import etree
my_url='https://so.gushiwen.cn/user/collect.aspx?type=s&id=3156762&sort=t'
my_response=session.get(url=my_url,headers=headers)
tree = etree.HTML(my_response.content)
poet_list=tree.xpath('//div[@class="sons"]//a[@style=" float:left;"]/text() ')
poet_content=tree.xpath('//div[@class="sons"]//a/@href')
fp=open('gushiwen_李白.txt','w',encoding='utf-8')
for i in range(len(poet_list)):
    fp.write(poet_list[i]+'\n')
#     https://so.gushiwen.cn/
    poet_url='https://so.gushiwen.cn/'+poet_content[i]
    # print(poet_content[i])
    fp.write(poet_url+'\n')
    poet_response = session.get(poet_url)
    poet_tree = etree.HTML(poet_response.content)
    p_content=poet_tree.xpath('//div[@class="sons"]//div[@class="contson"]/p/text()')
    if not p_content:
        p_content=poet_tree.xpath('//div[@class="sons"]//div[@class="contson"]/text()')
    # //div[@class="sons"]//div[@class="contson"]/text()
    for con in p_content:
        fp.write(con+ '\n')
    fp.write('\n')
fp.close()
# with open('gushiwen.html','w',encoding='utf-8') as fp:
#     fp.write(content_post)
# print(poet_list)
# my_content=my_response.text
# print(my_content)
# with open('gushiwen.html','w',encoding='utf-8') as fp:
#     fp.write(my_content)
    # https://so.gushiwen.cn/user/collect.aspx?type=s&id=3156762&sort=t
    # https://so.gushiwen.cn/shiwens/default.aspx?astr=%e6%9d%8e%e7%99%bd
    # //div[@class="sons"]//a[@style=" float:left;"]/text()  收藏里古诗的名字
    # //div[@class="sons"]//a/@href         收藏里古诗的内容
    # //div[@class="sons"]//b/text()   古诗名字
    # //div[@class="sons"]//div[@class="contson"]/text()  内容
