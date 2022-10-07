# _*_coding : utf-8 _*_
# @Time : 2022/7/28 17:16
# @Author : SunShine
# @File : python_selenium_handless
# @Project : python基础_爬虫

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# # path是你自己的chrome浏览器的文件路径
# path = r'C:\Users\12041\AppData\Local\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = path
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
#
# url = 'https://www.baidu.com'
#
# browser.get(url)
#
# browser.save_screenshot('baidu.png')

# 封装的handless


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # path是你自己的chrome浏览器的文件路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

browser = share_browser()

url = 'https://www.baidu.com'

browser.get(url)
import time
time.sleep(2)

# 获取文本框的对象
input = browser.find_element_by_id('kw')

# 在文本框中输入周杰伦
input.send_keys('周杰伦')

time.sleep(2)

# 获取百度一下的按钮
button = browser.find_element_by_id('su')

# 点击按钮
button.click()

time.sleep(2)
browser.save_screenshot('baidu.png')
