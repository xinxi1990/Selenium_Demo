#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time,os,unittest,subprocess,pytest,allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from page.basepage import BasePage
from page.loginpage import LoginPage
from page.homepage import HomePage
from driver.wdriver import WDriver
from configread import account_name
from libs.logger import init_logger
logger = init_logger()  # 初始化日志

@allure.feature("登录")
class TestLoginPage(BasePage):

    def setUp(self):
        super(TestLoginPage, self).setUp()
        self.home_page = HomePage()
        self.login_page = LoginPage()

    @pytest.mark.run(order=1)
    @allure.story('测试-登录')
    def test_login(self):
        self.home_page.home_pwd_login()
        self.login_page.login()
        assert  account_name in str(self.driver.page_source).encode("utf-8")
        logger.info("登录成功...")

