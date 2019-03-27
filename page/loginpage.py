#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
reload(sys)
sys.setdefaultencoding('utf8')
from selenium.webdriver.common.by import By
from page.basepage import BasePage
from driver.wdriver import WDriver
from configread import ConfigParser
from libs.logger import init_logger
from configread import user_name,pwd
logger = init_logger()  # 初始化日志


class LoginPage():

    _account = By.CLASS_NAME, 'account-form-input'
    _pwd = By.CLASS_NAME, 'password'
    _login_btn = By.CLASS_NAME, 'account-form-field-submit'
    _link_book = By.CLASS_NAME, 'lnk-book'

    def __init__(self):
        logger.info("初始化LoginPage")
        self.driver = WDriver().get_driver()
        logger.info("selenum id:{}".format(id(self.driver)))
        # ConfigParser.read_config()
        # self.user_name = ConfigParser.get_config('username', 'user_name')
        # logger.info("账号:{}".format(self.user_name))
        # ConfigParser.config_dic = {}
        # self.pwd = ConfigParser.get_config('pwd', 'pwd')
        # logger.info("密码:{}".format(self.pwd))


    def login(self):
        self.driver.find_element(*self._account).clear()
        self.driver.find_element(*self._account).send_keys(user_name)
        self.driver.find_element(*self._pwd).clear()
        self.driver.find_element(*self._pwd).send_keys(pwd)
        self.driver.find_element(*self._login_btn).click()
        logger.info("点击登录")
