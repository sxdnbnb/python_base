from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time
import re
import requests
from io import BytesIO
from PIL import Image
import random


class SlipCaptcha(object):
    def __init__(self):
        """
        初始化界面,初始化了driver对象和wait对象,以及传入了一个url地址
        """
        self.url = 'https://www.huxiu.com/'
        option = Options()
        option.add_argument('--window-size=1332,700')
        option.add_argument('--disable-infobars')
        # option.add_argument('headless')
        option.add_argument('incognito')
        self.driver = webdriver.Chrome(chrome_options=option)
        self.wait = WebDriverWait(self.driver, 10)

    def home_page(self):
        """
        主要流程实施的函数
        1:driver.get函数先到达虎嗅首页面
        2:点击登陆按钮
        3:获取验证码的图片,图片有两份,一份是有缺口的,一份没有缺口
        4:获得的两份图片是被打乱,需要我们根据坐标信息,重新裁剪拼接
        5:拼接后,比较两份图片的区别,得到缺口的x方向的距离
        6:依据得到的距离,滑动滑块,由于存在对滑块轨迹的限制.随意我们还要设置如何活动,即以什么样的速度,加速度来滑动.
        :return:
        """
        self.driver.get(self.url)
        login_button = self.driver.find_element_by_xpath('//a[@class="js-login"]')
        login_button.click()
        gap_image_position, nogap_image_position, gap_image_url, nogap_image_url = self.get_image_info()
        new_gapimage, new_nogapimage = self.get_image_complete(gap_image_position, nogap_image_position, gap_image_url,
                                                               nogap_image_url)
        distance = self.get_move_distance(new_gapimage, new_nogapimage)
        self.slid_button(distance)

    def get_image_info(self):
        """
        获得图片的信息，如图片的url，图片的坐标信息。
        共获得两份图片，一份是有缺口的，一份没有缺口。
        :return:
        """
        gap_image_list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                              '//div[@class="user-login-box"]//div[@class="gt_cut_bg gt_show"]/div[@class="gt_cut_bg_slice"]')))
        nogap_image_list = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                '//div[@class="user-login-box"]//div[@class="gt_cut_fullbg gt_show"]/div[@class="gt_cut_fullbg_slice"]')))
        gap_image_url = re.findall(r'url\("(.*?)"\)', gap_image_list[0].get_attribute('style'))[0]
        nogap_image_url = re.findall(r'url\("(.*?)"\)', nogap_image_list[0].get_attribute('style'))[0]
        gap_image_position = [re.findall(r'background-position: -(.*?)px -?(.*?)px;', i.get_attribute('style'))[0] for i
                              in gap_image_list]
        nogap_image_position = [re.findall(r'background-position: -(.*?)px -?(.*?)px;', i.get_attribute('style'))[0] for
                                i in nogap_image_list]
        return gap_image_position, nogap_image_position, gap_image_url, nogap_image_url

    def get_image_complete(self, gap_image_position, nogap_image_position, gap_image_url, nogap_image_url):
        """
        将获得混乱的图片，用获得的信息，拼接成正常的图片。
        :param gap_image_position:
        :param nogap_image_position:
        :param gap_image_url:
        :param nogap_image_url:
        :return:
        """
        gap_image_file = BytesIO(requests.get(gap_image_url).content)
        nogap_image_file = BytesIO(requests.get(nogap_image_url).content)
        old_gapimage = Image.open(gap_image_file)
        new_gapimage = Image.new('RGB', (260, 116))
        old_nogapimage = Image.open(nogap_image_file)
        new_nogapimage = Image.new('RGB', (260, 116))
        up_count = 0
        down_count = 0
        # 拼接缺口图片
        for i in gap_image_position[:26]:
            cut_image = old_gapimage.crop((int(i[0]), 58, int(i[0]) + 10, 116))  # 左上顶点，右下顶点
            new_gapimage.paste(cut_image, (up_count, 0))
            up_count = up_count + 10
        for i in gap_image_position[26:]:
            cut_image = old_gapimage.crop((int(i[0]), 0, int(i[0]) + 10, 58))  # 左上顶点，右下顶点
            new_gapimage.paste(cut_image, (down_count, 58))
            down_count = down_count + 10
        # 拼接无缺口图片
        up_count = 0
        down_count = 0
        for i in nogap_image_position[:26]:
            cut_image = old_nogapimage.crop((int(i[0]), 58, int(i[0]) + 10, 116))  # 左上顶点，右下顶点
            new_nogapimage.paste(cut_image, (up_count, 0))
            up_count = up_count + 10
        for i in gap_image_position[26:]:
            cut_image = old_nogapimage.crop((int(i[0]), 0, int(i[0]) + 10, 58))  # 左上顶点，右下顶点
            new_nogapimage.paste(cut_image, (down_count, 58))
            down_count = down_count + 10
        return new_gapimage, new_nogapimage

    def get_move_distance(self, new_gapimage, new_nogapimage):
        def compare_image(p1, p2):
            """
            比较图片的像素
            由于RGB图片一个像素点是三维的，所以循环三次
            :return:
            """
            for i in range(3):
                if abs(p1[i] - p2[i]) >= 50:
                    return False
                return True

        for i in range(260):
            for j in range(116):
                gap_pixel = new_gapimage.getpixel((i, j))
                nogap_pixel = new_nogapimage.getpixel((i, j))
                if not compare_image(gap_pixel, nogap_pixel):
                    return i

    def slid_button(self, distance):
        """
        根据缺口位置，移动滑块特定的距离distance
        :param diatance:
        :return:
        """
        # 获取滑块元素
        button = self.driver.find_element_by_xpath(
            '//div[@class="user-login-box"]//div[@class="gt_slider_knob gt_show"]')
        ActionChains(self.driver).click_and_hold(button).perform()
        time.sleep(0.5)
        track_list = self.track(distance - 3)
        # print(track_list)
        for i in track_list:
            ActionChains(self.driver).move_by_offset(i, 0).perform()
        time.sleep(1)
        ActionChains(self.driver).release().perform()

    def track(self, distance):
        """
        规划移动的轨迹
        加速度用到random模块,随机选择给定的加速度
        :param distance:
        :return:
        """
        # 匀速移动
        # for i in range(distance):
        #     ActionChains(self.driver).move_by_offset(1, 0).perform()
        # ActionChains(self.driver).move_by_offset(distance-5, 0).perform()
        t = 0.1
        speed = 0
        current = 0
        mid = 3 / 5 * distance
        track_list = []
        while current < distance:
            if current < mid:
                a = random.choice([1, 2, 3])
                # a = 3
            else:
                a = random.choice([-1, -2, -3])
                # a = -4
            move_track = speed * t + 0.5 * a * t ** 2
            track_list.append(round(move_track))
            speed = speed + a * t
            current += move_track
        # 模拟人类来回移动了一小段
        end_track = [1, 0] * 10 + [0] * 10 + [-1, 0] * 10
        track_list.extend(end_track)
        offset = sum(track_list) - distance
        # 由于四舍五入带来的误差,这里需要补回来
        if offset > 0:
            track_list.extend(offset * [-1, 0])
        elif offset < 0:
            track_list.extend(offset * [1, 0])
        return track_list

    def run(self):
        """
        运行函数,在主函数中执行该函数即可
        :return:
        """
        try:
            self.home_page()
        finally:
            time.sleep(0.5)
            self.driver.quit()


if __name__ == '__main__':
    S = SlipCaptcha()
    S.run()