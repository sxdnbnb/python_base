# _*_coding : utf-8 _*_
# @Time : 2022/7/21 14:24
# @Author : SunShine
# @File : python_解析_站长素材图片
# @Project : python基础_爬虫

# (1) 请求对象的定制
# （2）获取网页的源码
# （3）下载

# 需求 下载的前十页的图片
# https://sc.chinaz.com/tupian/lizhitupian.html
# https://sc.chinaz.com/tupian/lizhitupian_2.html
# https://sc.chinaz.com/tupian/lizhitupian_3.html

import urllib.request
from lxml import etree

def create_request(page):
    if page==1:
        url='https://sc.chinaz.com/tupian/lizhitupian.html'
    else:
        url='https://sc.chinaz.com/tupian/lizhitupian_'+str(page)+'.html'
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def down_load(content):
    # 下载图片
    # urllib.request.urlretrieve('图片地址','文件的名字')
    tree=etree.HTML(content)
    # // div[ @ id = "container"] // a / img / @ src
    # // div[ @ id = "container"] // a / img / @ alt
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')

    # 一般设计图片的网站都会进行懒加载
    src_list = tree.xpath('//div[@id="container"]//a/img/@src')
    # for name in src_list:
    #     print(name)

    for i in range(len(name_list)):
        name=name_list[i]
        src=src_list[i]
        url='https:'+src
        url=url.replace('_s','')
        # print(name,url)
        urllib.request.urlretrieve(url=url,filename='./picture/'+name+'.jpg')





if __name__ == '__main__':
    start_page=int(input("请输入起始页码"))
    end_page=int(input("请输入终止页码"))
    for page in range(start_page,end_page+1):

        # (1) 请求对象的定制
        request=create_request(page)
        # （2）获取网页的源码
        content=get_content(request)
        # （3）下载
        down_load(content)




