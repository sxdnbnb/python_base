# _*_coding : utf-8 _*_
# @Time : 2022/7/7 16:51
# @Author : SunShine
# @File : urllib_使用
# @Project : python基础


# 使用urllib来获取百度首页的源码
# import urllib.request


# (1)定义一个url  就是你要访问的地址
# url = 'http://www.baidu.com'

# (2)模拟浏览器向服务器发送请求 response响应
# response = urllib.request.urlopen(url)

# （3）获取响应中的页面的源码  content 内容的意思
# read方法  返回的是字节形式的二进制数据
# 我们要将二进制的数据转换为字符串
# 二进制-->字符串  解码  decode('编码的格式') charset=utf-8
# content = response.read().decode('utf-8')

# （4）打印数据
# print(content)

# import urllib.request

# url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse的类型
# print(type(response))

# 按照一个字节一个字节的去读
# content = response.read()
# print(content)

# 返回多少个字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# content = response.readlines()
# print(content)

# 返回状态码  如果是200了 那么就证明我们的逻辑没有错
# print(response.getcode())

# 返回的是url地址
# print(response.geturl())

# 获取是一个状态信息
# print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法 read  readline  readlines  getcode geturl getheaders

# import urllib.request
# # 下载网页
# url_page = 'http://www.baidu.com'

# url代表的是下载的路径  filename文件的名字
# 在python中 可以写变量的名字  也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
# url_img = 'https://img1.baidu.com/it/u=3004965690,4089234593&fm=26&fmt=auto&gp=0.jpg'
#
# urllib.request.urlretrieve(url= url_img,filename='lisa.jpg')

# 下载视频
# url_video = 'https://f.video.weibocdn.com/o0/rCYgJPMulx07XoUR3o0E01041203J9FJ0E020.mp4?label=mp4_720p&template=1280x720.25.0&ori=0&ps=1CwnkDw1GXwCQx&Expires=1657269817&ssig=l1OyWnvv71&KID=unistore,video'
#
# urllib.request.urlretrieve(url_video,'vedio.mp4')




import urllib.request

url = 'https://www.baidu.com'

# url的组成
# https://www.baidu.com/s?wd=周杰伦

# http/https    www.baidu.com   80/443     s      wd = 周杰伦     #
#    协议             主机        端口号     路径     参数           锚点
# http   80
# https  443
# mysql  3306
# oracle 1521
# redis  6379
# mongodb 27017

# UA反爬
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
}

# 因为urlopen方法中不能存储字典 所以headers不能传递进去
# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers) #因为参数顺序问题，需要关键字传参

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)






