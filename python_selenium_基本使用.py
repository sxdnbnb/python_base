# _*_coding : utf-8 _*_
# @Time : 2022/7/25 16:50
# @Author : SunShine
# @File : python_selenium_基本使用
# @Project : python基础_爬虫


# （1）导入selenium
from selenium import webdriver

# (2) 创建浏览器操作对象

path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

# （3）访问网站
url = 'https://www.baidu.com'

browser.get(url)

# url = 'https://www.jd.com/'
#
# browser.get(url)
#
# # page_source获取网页源码
# content = browser.page_source
# print(content)

# 元素定位

# 根据id来找到对象
button = browser.find_element_by_id('su')
print(button)

# 根据标签属性的属性值来获取对象的
# button = browser.find_element_by_name('wd')
# print(button)

# 根据xpath语句来获取对象
# button = browser.find_elements_by_xpath('//input[@id="su"]')
# print(button)

# 根据标签的名字来获取对象
# button = browser.find_elements_by_tag_name('input')
# print(button)

# 使用的bs4的语法来获取对象
# button = browser.find_elements_by_css_selector('#su')
# print(button)

# button = browser.find_element_by_link_text('图片')
# print(button)


