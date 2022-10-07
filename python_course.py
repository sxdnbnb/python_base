# _*_coding : utf-8 _*_
# @Time : 2022/9/13 14:44
# @Author : SunShine
# @File : python_course
# @Project : python基础_爬虫

import pandas as pd
import requests
import tencent_orc
from lxml import etree

# http://epo.cug.edu.cn/Gstudent/Course/StuCourseWeekQuery.aspx?


# 这是登陆页面的url地址
# url='http://epo.cug.edu.cn/UserLogin.aspx'
# headers = {
#     # 'Cache-Control': 'no-cache',
#     # 'Connection': 'keep-alive',
#     # 'Content-Length': '5368',
#     # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Cookie': 'KBCX_XQ=35; ASP.NET_SessionId=n13jzdidtcrpfaq1exp24awk; KBCX_Weeks=4; LoginType=1',
#     'Host': 'epo.cug.edu.cn',
#     'Origin': 'http://epo.cug.edu.cn',
#     'Referer': 'http://epo.cug.edu.cn/Gstudent/Course/StuCourseWeekQuery.aspx?EID=8idJjMxlDZLU33wqyyoARRgUvGo7Uig40TBsnTzBYfuBUWKrgavO!H1WIPfbj6pW3DMOqq5se2-e38aPwtdzTQ==',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#     # 'X-MicrosoftAjax': 'Delta=true',
#     # 'X-Requested-With': 'XMLHttpRequest',
# }
#
# # 获取页面的源码
# response=requests.get(url=url,headers=headers)
# print(response.text)
# tree=etree.HTML(response.content)
#
# # 解析页面源码  然后获取_VIEWSTATE   __VIEWSTATEGENERATOR
# # 获取_VIEWSTATE
# viewstate=tree.xpath('//input[@id="__VIEWSTATE"]/@value')
# # print(viewstate[0])
# # 获取__VIEWSTATEGENERATOR
# viewstategenerator = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')
# # print(viewstategenerator[0])
# eventvalidation= tree.xpath('//input[@id="__EVENTVALIDATION"]/@value')
# # print(eventvalidation[0])
#
# # 获取验证码图片
# code=tree.xpath('//input[@type="image"]/@src')
# # print(code)
#
# code_url='http://epo.cug.edu.cn/'+str(code[0])
# # print(code_url)
# session = requests.session()
# response_code = session.get(code_url)
# content_code = response_code.content
# with open('code.png','wb')as fp:
#     fp.write(content_code)
# # 获取了验证码的图片之后 下载到本地 识别后就可以将这个值给code的参数 就可以登陆
# code_picture='code.png'
# code_name = tencent_orc.tencent_orc(code_picture)
# # print(code_name)
# data_post = {
#     'ScriptManager1': 'UpdatePanel2|btLogin',
#     'UserName': '1202221586',
#     'PassWord': '6446530Sun',
#     'ValidateCode': code_name,
#     # 'drpLoginType': 1,
#     '__EVENTTARGET': 'btLogin',
#     # '__EVENTARGUMENT': '',
#     # '__LASTFOCUS': '',
#     '__VIEWSTATE': viewstate[0],
#     '__VIEWSTATEGENERATOR': viewstategenerator[0],
#     '__EVENTVALIDATION':eventvalidation[0],
#     # '__ASYNCPOST': 'true',
#     # '':'',
# }
# #
# response_post=session.post(url=url,data=data_post,headers=headers)
# content_post=response_post.text
# with open('course.html','w',encoding='utf-8') as fp:
#     fp.write(content_post)


course_url='http://epo.cug.edu.cn/Gstudent/Course/StuCourseWeekQuery.aspx?EID=8idJjMxlDZLU33wqyyoARRgUvGo7Uig40TBsnTzBYfuBUWKrgavO!LCjRVz!yh91zsPu!sEtaaaQAQQqVnwAHw%3d%3d'
headers={
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '5368',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'KBCX_XQ=35; ASP.NET_SessionId=lglc03acsqz1ju5hvhomy3jp; KBCX_Weeks=5',
    # 'Cookie': 'KBCX_XQ=35; ASP.NET_SessionId=lglc03acsqz1ju5hvhomy3jp; KBCX_Weeks=8',
    # 'Host': 'epo.cug.edu.cn',
    # 'Origin': 'http://epo.cug.edu.cn',
    # 'Referer': 'http://epo.cug.edu.cn/Gstudent/Course/StuCourseWeekQuery.aspx?EID=8idJjMxlDZLU33wqyyoARRgUvGo7Uig40TBsnTzBYfuBUWKrgavO!H1WIPfbj6pW3DMOqq5se2-e38aPwtdzTQ==',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    # 'X-MicrosoftAjax': 'Delta=true',
    # 'X-Requested-With': 'XMLHttpRequest',
}
# 获取页面的源码
# response=requests.get(url=course_url,headers=headers)
# tree=etree.HTML(response.content)
# # 获取_VIEWSTATE
# viewstate=tree.xpath('//input[@id="__VIEWSTATE"]/@value')
# # print(viewstate[0])
# eventvalidation= tree.xpath('//input[@id="__EVENTVALIDATION"]/@value')
# print(eventvalidation[0])
# EID=tree.xpath('//form[@id="Form1"]/@EID')
# print(EID)
# data={
#     'EID':'8idJjMxlDZLU33wqyyoARRgUvGo7Uig40TBsnTzBYfuBUWKrgavO!LCjRVz!yh91zsPu!sEtaaaQAQQqVnwAHw==',
#     # 'ctl00$ScriptManager1': 'ctl00$contentParent$UpdatePanel1|ctl00$contentParent$drpWeek',
#     # 'ctl00$contentParent$drpXq': 35,
#     # 'ctl00$contentParent$drpWeek': 4,
#     # '__EVENTTARGET': 'ctl00$contentParent$drpWeek',
#     # # '__EVENTARGUMENT': '',
#     # # '__LASTFOCUS': '',
#     # '__VIEWSTATE': viewstate,
#     # '__VIEWSTATEGENERATOR': 'E3B308FE',
#     # '__EVENTVALIDATION': eventvalidation,
#     # '__VIEWSTATEENCRYPTED': '',
#     # '__ASYNCPOST': 'true',
# }
response=requests.get(url=course_url,headers=headers)
content=response.text
with open('course1.html','w',encoding='utf-8') as fp:
    fp.write(str(content))
# 爬取url中的表格
# course = pd.read_html('course.html')
# dataframe = course[1]
# dataframe.to_excel('course.xls',encoding="utf_8_sig",index=False)

