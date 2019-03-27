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
from config import *
from page.basepage import BasePage
from driver.wdriver import WDriver
from libs.logger import init_logger
logger = init_logger()  # 初始化日志


class HomePage():

    _pwd_btn = By.CLASS_NAME,'account-tab-account'
    _account = By.CLASS_NAME,'account-form-input'
    _pwd = By.CLASS_NAME, 'password'
    _login_btn = By.CLASS_NAME, 'account-form-field-submit'
    _link_book = By.CLASS_NAME, 'lnk-book'

    def __init__(self):
        logger.info("初始化HomePage")
        self.driver = WDriver().get_driver()
        logger.info("selenum id:{}".format(id(self.driver)))



    def switch_to_login_frame(self):
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])
        logger.info("切换frame")


    def home_pwd_login(self):
        '''
        首页密码登录
        :return:
        '''
        self.switch_to_login_frame()
        account_tab_account = self.driver.find_element(*self._pwd_btn)
        account_tab_account.click()
        self.driver.execute_script("arguments[0].style.background = 'rgb(138,43,226 )';", account_tab_account)
        logger.info("点击密码登录...")
        time.sleep(3)


    def home_serach(self):
        table_source = self.driver.find_element(*self._link_book).get_attribute('innerHTML')
        print(table_source)
        # 获取按钮的文案
        self.driver.find_element(*self._link_book).click()
        print("点击读书")
        handles_list = self.driver.window_handles
        print(handles_list)
        self.driver.switch_to.window(str(handles_list[-1]))
        print("切换窗口")
        if self.driver.current_window_handle == str(handles_list[-1]):
            print("切换窗口成功...")






