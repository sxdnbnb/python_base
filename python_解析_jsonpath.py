# _*_coding : utf-8 _*_
# @Time : 2022/7/21 16:39
# @Author : SunShine
# @File : python_解析_jsonpath
# @Project : python基础_爬虫


import json
import jsonpath

obj = json.load(open('douban.json','r',encoding='utf-8'))

# 书店所有书的作者
# store_list = jsonpath.jsonpath(obj,'$.Table1[*].storeName')
# print(store_list)

# 所有的作者
store_list = jsonpath.jsonpath(obj,'$..title')
# print(type(store_list[0]))
fp=open('douban.txt','w',encoding='utf-8')
for l in store_list:
    fp.write(l+"\n")


# store下面的所有的元素
# tag_list = jsonpath.jsonpath(obj,'$.Table1.*')
# print(tag_list)

# store里面所有东西的price
# price_list = jsonpath.jsonpath(obj,'$.Table1..storeName')
# print(price_list)

# 第三个书
# book = jsonpath.jsonpath(obj,'$..Table1[2]')
# print(book)

# 最后一本书
# book = jsonpath.jsonpath(obj,'$..Table1[(@.length-1)]')
# print(book)

# 	前面的两本书
# book_list = jsonpath.jsonpath(obj,'$..Table1[0,1]')
# book_list = jsonpath.jsonpath(obj,'$..Table1[:2]')
# print(book_list)

# 条件过滤需要在（）的前面添加一个？
# 	 过滤出所有的包含isbn的书。
# book_list = jsonpath.jsonpath(obj,'$..Table1[?(@.cityName)]')
# print(book_list)


# 哪本书超过了10块钱
# book_list = jsonpath.jsonpath(obj,'$..Table1[?(@.rownum>4)]')
# print(book_list)
