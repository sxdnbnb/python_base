# _*_coding : utf-8 _*_
# @Time : 2022/8/18 16:58
# @Author : SunShine
# @File : milk_淘宝
# @Project : python基础_爬虫

import requests
from lxml import etree

url = 'https://s.taobao.com/search'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': 't=4375fd8380514898c7817ecb0f9e9e68; cna=S+2EG6MERU0CAXuoBAqB9lhb; sgcookie=E100VTMRro6dnCmUV7uUuZpzbSufhmTq4qViQzzBMz3FfVpjmIU7Z2Eey2v4skEW2%2Fq5dyykVjGB2rZJtlEBcHSjEoWYmFlNHeU3Uo4bTp8Ikxg%3D; uc3=vt3=F8dCv4COYYj%2FJ5m%2F2UE%3D&id2=UUBZEYf3A7zAZA%3D%3D&nk2=F6k3HMWzuBZtphrPSai0PEA%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; lgc=t_1478750685773_0; uc4=nk4=0%40FbMocpOBNfLlvi1xoG5BWDosSJZtDK%2BG9CfbDg%3D%3D&id4=0%40U2LLElWJ4HLDkcMwNE0benQaMpfN; tracknick=t_1478750685773_0; _cc_=W5iHLLyFfA%3D%3D; enc=mWPrFYaGdBpz79KiRW4uV23j%2BKrJCc21CWwGufBXrxzl2AB3qFB6008IULFcOMvKXN6VnPD%2BieENmui%2BpSwANg%3D%3D; cookie2=19c33a292f01469ab5e20fd3a59b407a; v=0; _tb_token_=e1b6efa83e7ab; ariaDefaultTheme=default; ariaFixed=true; ariaReadtype=1; ariaoldFixedStatus=false; ariaStatus=false; x5sec=7b227365617263686170703b32223a223631313861636335393630626334613539613631303262623033666565336131434b722f2f4a63474549506f722b7a372b61624152686f4d4d6a67784d4459344d7a41794e6a73784d4b6546677037382f2f2f2f2f77464141773d3d227d; JSESSIONID=BEAC74D6E19F87667E7EA2C4108F9F24; tfstk=czL5Bpsn2825UYkf3gGqYsBPt4QFZmylgrXDNxA6QzGUEwO5iu4NCqlFN-QF9s1..; l=eBIz75-nLqz4NNhQBOfZourza77O_IRYYuPzaNbMiOCP_f5H5Yh1W6Yh-3TMCn1Vh6B9J35Wn1oBBeYBqCmWfdW22j-laODmn; isg=BIGB-JPwhy_PuusZrN_XxxnPkM2brvWg53TwvuPWXAjnyqGcKv69cKTArL6MWY3Y',    'referer': 'https://s.taobao.com/search?q=%E4%B8%89%E5%85%83&cps=yes&cat=51160012',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
}
# data = {
#     'q':'三元',
#     'cps':'yes',
#     'cat':'51160012'
# }
data={
    'data-key': 's,ps',
    'data-value': '0,1',
    'ajax': 'true',
    '_ksTS': '1660897170974_1240',
    'callback': 'jsonp1241',
    'q': '三元',
    'cps': 'yes',
    'cat': '51160012',
    'bcoffset': '0',
    'ntoffset': '4',
    'p4ppushleft': '2,48',
    's': '44',

    'data-key': 's',
    'data-value': '88',
    'ajax': 'true',
    '_ksTS': '1660897348003_724',
    'callback': 'jsonp725',
    'q': '三元',
    'cps': 'yes',
    'cat': '51160012',
    'bcoffset': '0',
    'ntoffset': '4',
    'p4ppushleft': '2,48',
    's': '44',
}


# url  请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url=url,params=data,headers=headers)

content = response.content.decode('utf-8')

content=response.text
# with open('milk.json','w',encoding='utf-8')as fp:
#     fp.write(content)
# print(content)
import re
product_title=re.findall('"raw_title":"(.*?)"',content)
product_price=re.findall('"view_price":"(.*?)"',content)
product_sales=re.findall('"view_sales":"(.*?)"',content)
# print(product_title)
with open('milk.txt','w',encoding='utf-8')as fp:
    for i in range(len(product_title)):
        fp.write(product_title[i])
        fp.write('    ')
        fp.write(product_price[i])
        fp.write('    ')
        fp.write(product_sales[i])
        fp.write('\n')
        # print(i)
        # print(product_title[i],product_price[i],product_sales[i])
fp.close()
# tree = etree.HTML(content)
#
#
# result = tree.xpath('//div[@class="row row-2 title"]/a/text()')
# result = tree.xpath('//span[@class="bg s_btn_wr"]/input/@value')[0]
# print(result)
