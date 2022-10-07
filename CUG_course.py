# _*_coding : utf-8 _*_
# @Time : 2022/9/15 19:35
# @Author : SunShine
# @File : CUG_course
# @Project : python基础_爬虫
import requests
import pandas as pd
# course_url='http://epo.cug.edu.cn/Gstudent/Course/StuCourseWeekQuery.aspx?EID=8idJjMxlDZLU33wqyyoARRgUvGo7Uig40TBsnTzBYfuBUWKrgavO!LCjRVz!yh91zsPu!sEtaaaQAQQqVnwAHw%3d%3d'
# course_url='http://epo.cug.edu.cn/Gstudent/Course/StuCourseWeekQuery.aspx?EID=8idJjMxlDZLU33wqyyoARRgUvGo7Uig40TBsnTzBYfuBUWKrgavO!Iqf2pyaHf6z!JUzQ3MzZPY2YXeVnlHDmg%3d%3d'
course_url='http://epo.cug.edu.cn/Gstudent/Course/StuCourseWeekQuery.aspx?EID=8idJjMxlDZLU33wqyyoARRgUvGo7Uig40TBsnTzBYfuBUWKrgavO!I4-2d65LiH9q7ZlzHCMnPrwdOZWUN1Odw%3d%3d'

for i in range(3,20):
    # cookie = 'KBCX_XQ=35; ASP.NET_SessionId=1x3loy1exyhdsri5sr0kzygt; KBCX_Weeks='+str(i)
    cookie = 'KBCX_XQ=35; DropDownListNd=2024; ASP.NET_SessionId=m3amquh1waw31ewq4vlne02e; KBCX_Weeks='+str(i)
    # print(cookie)
    headers = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    response = requests.get(url=course_url, headers=headers)
    content = response.text
    with open('course.html', 'w', encoding='utf-8') as fp:
        fp.write(str(content))
    # 爬取url中的表格
    course = pd.read_html('course.html')
    dataframe = course[1]
    file_name = '第' + str(i) + '周.xlsx'
    # print(file_name)
    tmp_file_path='./course/' + file_name
    writer = pd.ExcelWriter(tmp_file_path)
    dataframe.to_excel(writer, encoding="utf_8_sig", index=False)
    worksheet = writer.sheets['Sheet1']
    # worksheet.set_row(7,70)
    worksheet.set_column(0,1,5) #指定第3-13列为10像素宽度
    worksheet.set_column(2,8,57) #指定第3-13列为10像素宽度
    writer.save()
