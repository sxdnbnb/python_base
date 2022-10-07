# _*_coding : utf-8 _*_
# @Time : 2022/7/22 15:26
# @Author : SunShine
# @File : python_解析_jsonpath解析淘票票
# @Project : python基础_爬虫
import urllib.request

url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1658474867570_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers={
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v': '2.2.0',
    'cookie': 't=5ca150328ee2c759d141bd788375b9e4; cookie2=1002c724cfc953d8afc9415ca6fc5276; v=0; _tb_token_=53535ee61786a; l=eBEHHMCRLVGlPDVfBO5Churza77T2IOb8sPzaNbMiInca12F9FsOINCHQ1YeWdtjgt5UUeKrJ6F2hdHWrc4T5FsWHpfuKtyuJppw8e1..; isg=BIOD9CxR5TAQz6nVfmjAfD3KEkct-Bc6EDxq0LVh5OJZdKKWPM3NiKyq7gQ6VG8y',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
    'x-requested-with': 'XMLHttpRequest',
}

request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
# 字符串 split 切割
content = content.split('(')[1].split(')')[0]
# print(content)
with open('taopiaopiao.json','w',encoding='utf-8') as fp:
    fp.write(content)

import json
import jsonpath

obj=json.load(open('taopiaopiao.json','r',encoding='utf-8')) #读文件

city_list=jsonpath.jsonpath(obj,'$..regionName')

print(city_list)