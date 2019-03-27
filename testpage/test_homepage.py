#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time, os, unittest, subprocess,pytest,unittest,allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import *
from page.basepage import BasePage
from driver.wdriver import WDriver
from page.homepage import HomePage
from parameterized import parameterized
from libs.logger import init_logger
logger = init_logger()  # 初始化日志


@allure.feature("首页")
class TestHomePage(BasePage):

    def setUp(self):
        super(TestHomePage, self).setUp()
        logger.info("TestHomePage")
        self.home_page = HomePage()


    @allure.story("首页-搜索")
    @parameterized.expand([[u"绿皮书", "Two"], [u"流浪地球", "Four"], [u"阿丽塔", "Six"], ])
    def test_home_serach(self, arg1,arg2):
        '''
        首页参数化搜索
        :param arg1:
        :param arg2:
        :return:
        '''
        logger.info(arg1)
        self.home_page.home_serach(arg1)

    @allure.story("首页-下载app")
    def test_home_downlod_app(self):
        self.home_page.download_app()
