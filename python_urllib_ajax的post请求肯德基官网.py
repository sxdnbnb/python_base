# _*_coding : utf-8 _*_
# @Time : 2022/7/15 15:09
# @Author : SunShine
# @File : python_urllib_ajax的post请求肯德基官网
# @Project : python基础

import urllib.request
import urllib.parse
import urllib.error
def create_request(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '青岛',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
    }

    request=urllib.request.Request(url=url,data=data,headers=headers)
    # print(request)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def down_load(page, content):
    fp = open('KFC' + str(page) + '.json', 'w', encoding='utf-8')
    fp.write(content)
    fp.close()



if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页面'))

    for page in range(start_page, end_page + 1):
        try:
            #         每一页都有自己的请求对象的定制
            request = create_request(page)
            #         获取响应的数据
            content = get_content(request)
            # #         下载
            down_load(page, content)

        except urllib.error.HTTPError:
            print('系统正在升级。。。')
        except urllib.error.URLError:
            print('我都说了 系统正在升级。。。')



