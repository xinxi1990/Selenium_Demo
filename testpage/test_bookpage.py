#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time, os, unittest, subprocess,pytest,unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import *
from page.basepage import BasePage
from driver.wdriver import WDriver
from page.homepage import HomePage
from page.bookpage import BookPage
from page.functionpage import FunctionPage as func
from parameterized import parameterized

@allure.feature("读书")
class TestBookPage(BasePage):

    @classmethod
    def setUpClass(cls):
        print("子类setUpClass")


    def setUp(self):
        super(TestBookPage, self).setUp()
        print("TestBookPage")
        self.home_page = HomePage()
        self.book_page = BookPage()


    # @func.screen_shot()
    @allure.story("读书-搜索")
    @parameterized.expand([["java"], ["python"], ["php"], ])
    def test_book_serach(self, arg1):
        '''
        首页参数化搜索
        :param arg1:
        :param arg2:
        :return:
        '''
        print("test_book_serach")
        self.home_page.home_serach()
        self.book_page.serach_book(arg1)