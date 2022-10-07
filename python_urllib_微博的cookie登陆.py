# _*_coding : utf-8 _*_
# @Time : 2022/7/19 16:17
# @Author : SunShine
# @File : python_urllib_微博的cookie登陆
# @Project : python基础

# 适用的场景：数据采集的时候 需要绕过登陆 然后进入到某个页面
# 个人信息页面是utf-8  但是还报错了编码错误  因为并没有进入到个人信息页面 而是跳转到了登陆页面
# 那么登陆页面不是utf-8  所以报错

# 什么情况下访问不成功？
# 因为请求头的信息不够，所以访问不成功

import urllib.request

url = 'https://weibo.com/'

headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'cache-control': 'max-age=0',
'cookie': 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5S0wQfh1qcJsuMPdn16CPJ5JpX5KMhUgL.Fo-4SK-0eKn7SK52dJLoIEBLxKqL1-2LB--LxK-L1hqLB-eLxKqLBo-L1h-LxK-LBKBL12qt; SINAGLOBAL=4817193609491.492.1657266237410; WBPSESS=yZ9_LikvsGfkaRtL7jSDr6exjd0hC6ccSVIT2lLTGlgwpF41ksqfZGkEuNeS8wPsJgYRtVWUVLd2LZbIkZ-fS8rfDNBB7JN79E3OrbK8klvN_-CAODjC4XNsYCGyUAAVPMpGJEHnYCj3NVm9icMQIg==; ULV=1658200133586:2:2:1:5391819351600.844.1658200133495:1657266237432; ALF=1689749422; SSOLoginState=1658213423; SCF=AqSTOBl90_AiEN-qHw0hU1YfRkRBVv0djgytMEqLx-6MS-200dU-Ej4LaJ9_BBO5ePwoCyAWxyazPQqti8VAH60.; SUB=_2A25P0iR_DeRhGeNH7lcS8SbMzjyIHXVsphK3rDV8PUNbmtB-LVTwkW9NSrTmQDhQLj4_5wOuvSZd0OVNh8C8xN59; XSRF-TOKEN=J2isYWDKJB-LHPgqqoc730SP; _s_tentry=weibo.com; Apache=9575935644234.684.1658220042571',
'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
}
# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')

# 将数据保存到本地
with open('weibo.html','w',encoding='utf-8')as fp:
    fp.write(content)
