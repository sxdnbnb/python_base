# _*_coding : utf-8 _*_
# @Time : 2022/7/27 16:18
# @Author : SunShine
# @File : python_selenium_phantomjs的基本使用
# @Project : python基础_爬虫

from selenium import webdriver

path = 'phantomjs.exe'

browser = webdriver.PhantomJS(path)


url = 'https://www.baidu.com'
browser.get(url)

browser.save_screenshot('baidu.png')

import time
time.sleep(2)

input = browser.find_element_by_id('kw')
input.send_keys('昆凌')

time.sleep(3)

browser.save_screenshot('kunling.png')

