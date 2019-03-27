#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time,os,unittest,subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from page.basepage import BasePage
from driver.wdriver import WDriver
from libs.logger import init_logger
logger = init_logger()  # 初始化日志



class BookPage():


    _search_text = By.ID, 'inp-query'
    _inp_btn = By.CLASS_NAME, 'inp-btn'

    def __init__(self):
        self.driver = WDriver().get_driver()
        logger.info("selenum id:{}".format(id(self.driver)))


    def serach_book(self,keywords):
        '''
        搜索
        :param keywords:
        :return:
        '''
        logger.info("准备搜索的书名:{}".format(keywords))
        if self.driver.find_elements(*self._search_text):
            logger.info("查询到搜索")
        el = self.driver.find_element(*self._search_text)
        el.clear()
        el.send_keys(keywords)
        logger.info("搜索:{}".format(keywords))
        self.driver.back()
        logger.info("返回上一级")