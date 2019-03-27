#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# import allue
import time,os,unittest,subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import *
from driver.wdriver import WDriver


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("父类setUpClass初始化")

    def setUp(self):
        print("父类初始化")
        self.driver = WDriver().init_driver()
        print("selenum id:{}".format(id(self.driver)))
        self.driver.get("https://www.douban.com")

    # def tearDown(self):
    #     print("父类结束")
    #     self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        print("父类tearDownClass结束")




