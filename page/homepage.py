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
from page.functionpage import FunctionPage
from driver.wdriver import WDriver
from libs.logger import init_logger
logger = init_logger()  # 初始化日志


class HomePage():

    _home_serach = By.XPATH,'//*[@id="anony-nav"]/div[2]/form/span[1]/input'
    _home_serach_submit = By.XPATH,'//*[@id="anony-nav"]/div[2]/form/span[2]/input'
    _pwd_btn = By.CLASS_NAME,'account-tab-account'
    _account = By.CLASS_NAME,'account-form-input'
    _pwd = By.CLASS_NAME, 'password'
    _login_btn = By.CLASS_NAME, 'account-form-field-submit'
    _link_book = By.CLASS_NAME, 'lnk-book'
    _link_movie = By.CLASS_NAME, 'lnk-movie'
    _link_app = By.CLASS_NAME, 'lnk-app'
    _page = "#fp-nav > ul > li:nth-child({}) > a"



    def __init__(self):
        logger.info("初始化HomePage")
        self.driver = WDriver().get_driver()
        self.func = FunctionPage()
        # logger.info("selenum id:{}".format(id(self.driver)))



    def switch_to_login_frame(self):
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])
        logger.info("切换frame")



    def home_serach(self,keywords):
        '''
        首页搜索
        :return:
        '''
        self.driver.find_element(*self._home_serach).send_keys(keywords)
        self.driver.find_element(*self._home_serach_submit).send_keys(keywords)
        logger.info("首页搜索:{}".format(keywords))


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


    def go_book(self):
        table_source = self.driver.find_element(*self._link_book).get_attribute('innerHTML')
        logger.info(table_source)
        # 获取按钮的文案
        self.driver.find_element(*self._link_book).click()
        logger.info("点击读书")
        self.func.switch_window()


    def go_movie(self):
        table_source = self.driver.find_element(*self._link_movie).get_attribute('innerHTML')
        logger.info(table_source)
        # 获取按钮的文案
        self.driver.find_element(*self._link_movie).click()
        logger.info("点击电影")
        self.func.switch_window()



    def download_app(self):
        self.driver.find_element(*self._link_app).click()
        logger.info("点击下载app")
        for n in range(1,5):
            page = self._page.format(n)
            self.driver.find_element(By.CSS_SELECTOR,page).click()



