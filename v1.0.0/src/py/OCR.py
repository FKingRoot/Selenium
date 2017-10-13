#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import pytesser3
import datetime
from time import sleep
from PIL import Image
# import urllib
# import urllib.request


def acquire_file_dir():
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    elif __file__:
        return os.path.dirname(__file__)


class Login():
    def __init__(self, driver):
        self.driver = driver

    def login_in(self, username, password):
        driver = self.driver
        driver.get('http://192.168.9.14:80/')
        sleep(2)
        driver.find_element_by_id('loginNo').send_keys(username)
        driver.find_element_by_id('passWord').send_keys(password)

        # 1、验证码图片每刷新一次都会变 此方法暂不采用
        # image = self.driver.find_element_by_id('d').get_attribute('src')
        # request = urllib.request.Request(image)
        # response = urllib.request.urlopen(request)
        # get_img = response.read()
        # with open('F:\haha\Code.png', 'wb') as fp:
        #    fp.write(get_img)
        # code = pytesser3.image_file_to_string('F:\haha\Code.png')
        # print(code)

        # 2、对验证码进行区域截图
        driver.get_screenshot_as_file(acquire_file_dir() + '\pic_log\login_code.png')
        Image.open(acquire_file_dir() + '\pic_log\login_code.png').crop((615, 383, 683, 403)).save(acquire_file_dir() + '\pic_log\login_code.png')
        code = pytesser3.image_file_to_string(acquire_file_dir() + '\pic_log\login_code.png')
        driver.find_element_by_id('code').send_keys(code)
        driver.find_element_by_id('c').click()

        strPath = acquire_file_dir() + '\pic_log\\' \
            + str(datetime.datetime.now().date()) + '-' \
            + str(datetime.datetime.now().time())[0:2] + '-' \
            + str(datetime.datetime.now().time())[3:5] + '-' \
            + str(datetime.datetime.now().time())[6:8] \
            + '.png'
        self.driver.get_screenshot_as_file(strPath)

if __name__ == "__main__":
    print(str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time())[0:8])


