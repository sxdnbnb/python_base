# _*_coding : utf-8 _*_
# @Time : 2022/7/26 17:38
# @Author : SunShine
# @File : python_爬虫_selenium_元素信息和交互
# @Project : python基础_爬虫

from selenium import webdriver
from PIL import Image
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=1600000527&daid=6&s_url=https%3A%2F%2Fdnf.gamebbs.qq.com%2Fmember.php%3Fmod%3Dlogging%26amp%3Baction%3Dloginsucc&style=20&border_radius=1&target=self&maskOpacity=40&'
browser.get(url)
browser.get_cookies()
# input = browser.find_element_by_id('su')
#
# # 获取标签的属性
# print(input.get_attribute('class'))
# # 获取标签的名字
# print(input.tag_name)
#
# # 获取元素文本
# a = browser.find_element_by_link_text('图片')
# print(a.text)

import time
time.sleep(2)

# 获取按钮
button=browser.find_element_by_xpath('//div[@id="bottom_qlogin"]//a[@id="switcher_plogin"]')

# 点击按钮
button.click()

time.sleep(2)
# 获取账号文本框的对象
input_1 = browser.find_element_by_class_name('inputstyle')

# 在文本框中输入账号
input_1.send_keys('859211803')

time.sleep(2)
# 获取密码文本框的对象
input_2 = browser.find_element_by_class_name('inputstyle.password')
# 在密码文本框中输入密码
input_2.send_keys('12345678zzzz')

#获取登录按钮
time.sleep(2)
button2=browser.find_element_by_xpath('//div[@class="submit"]//input[@id="login_button"]')
button2.click()



# time.sleep(2)

# 滑到底部
# js_bottom = 'document.documentElement.scrollTop=100000'
# browser.execute_script(js_bottom)

# time.sleep(2)

# 获取下一页的按钮
# next = browser.find_element_by_xpath('//a[@class="n"]')

# # 点击下一页
# next.click()

# time.sleep(2)

# 回到上一页
# browser.back()
#
# time.sleep(2)

# 回去
# browser.forward()
#
# time.sleep(3)

# 退出
# browser.quit()

def get_geetest_image(self):  # 获取验证码图片
    gapimg = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tc-bg-img unselectable')))
    sleep(2)
    gapimg.screenshot(r'./captcha1.png')
    # 通过js代码修改标签样式 显示图片2
    js = 'var change = document.getElementsByClassName("geetest_canvas_fullbg");change[0].style = "display:block;"'
    self.driver.execute_script(js)
    sleep(2)
    fullimg = self.wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_slice')))
    fullimg.screenshot(r'./captcha2.png')


def is_similar(self, image1, image2, x, y):
    '''判断两张图片 各个位置的像素是否相同
    #image1:带缺口的图片
    :param image2: 不带缺口的图片
    :param x: 位置x
    :param y: 位置y
    :return: (x,y)位置的像素是否相同
    '''
    # 获取两张图片指定位置的像素点
    pixel1 = image1.load()[x, y]
    pixel2 = image2.load()[x, y]
    # 设置一个阈值 允许有误差
    threshold = 60
    # 彩色图 每个位置的像素点有三个通道
    if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
            pixel1[2] - pixel2[2]) < threshold:
        return True
    else:
        return False


def get_diff_location(self):  # 获取缺口图起点
    captcha1 = Image.open('captcha1.png')
    captcha2 = Image.open('captcha2.png')
    for x in range(self.left, captcha1.size[0]):  # 从左到右 x方向
        for y in range(captcha1.size[1]):  # 从上到下 y方向
            if not self.is_similar(captcha1, captcha2, x, y):
                return x  # 找到缺口的左侧边界 在x方向上的位置


def get_move_track(self, gap):
    track = []  # 移动轨迹
    current = 0  # 当前位移
    # 减速阈值
    mid = gap * 4 / 5  # 前4/5段加速 后1/5段减速
    t = 0.2  # 计算间隔
    v = 0  # 初速度
    while current < gap:
        if current < mid:
            a = 5  # 加速度为+5
        else:
            a = -5  # 加速度为-5
        v0 = v  # 初速度v0
        v = v0 + a * t  # 当前速度
        move = v0 * t + 1 / 2 * a * t * t  # 移动距离
        current += move  # 当前位移
        track.append(round(move))  # 加入轨迹
    return track


def move_slider(self, track):
    slider = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_slider_button')))
    ActionChains(self.driver).click_and_hold(slider).perform()
    for x in track:  # 只有水平方向有运动 按轨迹移动
        ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        sleep(0.2)
    sleep(1)
    ActionChains(self.driver).release().perform()  # 松开鼠标

get_geetest_image(browser)
gap = get_diff_location(browser)  # 缺口左起点位置
gap = gap - 6  # 减去滑块左侧距离图片左侧在x方向上的距离 即为滑块实际要移动的距离
track = get_move_track(browser,gap)
move_slider(browser,track)