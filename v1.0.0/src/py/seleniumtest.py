#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XXXX"""

import unittest
from selenium import webdriver
from OCR import Login


class LoginCase(unittest.TestCase):
    """XXXX""" 
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.lib = Login(self.driver)
        self.driver.maximize_window()

    def test_login(self):
        """XXXX"""
        self.lib.login_in('test', 'develop')

    def test_login1(self):
        """XXXX"""
        self.lib.login_in('test', 'develop')

    # def test_login_pwd_error(self):
    #     self.login('test', 'develop')
    #     sleep(2)
    #     error_message = self.driver.find_element_by_id('tip_btn').text
    #     self.assertIn('用户名或密码错误', error_message)
    #     self.driver.get_screenshot_as_file('F:\haha\login_pwd_error.png')

    def tearDown(self):
        print('自动测试完毕！')
        self.driver.quit()

if __name__ == '__main__':
    # 1、默认是'test_'开头的测试用例
    # unittest.main()
    
    # 2、单独添加测试用例 非重复
    suite = unittest.TestSuite()
    suite.addTest(LoginCase('test_login'))
    suite.addTest(LoginCase('test_login1'))
    runner = unittest.TextTestRunner()
    runner.run(suite)   

    # 3、
    # loader = unittest.TestLoader()
    # suite1 = loader.discover('test_')
    # suite2 = loader.discover('test_login')
    # alltests = unittest.TestSuite((suite1, suite2))
    # unittest.TextTestRunner(verbosity=2).run(alltests)
