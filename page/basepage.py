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
from libs.logger import init_logger
logger = init_logger()  # 初始化日志


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("父类setUpClass初始化")

    def setUp(self):
        logger.info("父类初始化")
        self.driver = WDriver().init_driver()
        logger.info("selenum id:{}".format(id(self.driver)))
        self.driver.get("https://www.douban.com")

    def tearDown(self):
        logger.info("父类结束")
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        logger.info("父类tearDownClass结束")




