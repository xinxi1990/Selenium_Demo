#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,sys,unittest,os
from page_objects import PageObject, PageElement
from selenium import webdriver
from page.basepage import BasePage
from HTMLTestRunner_cn.HTMLTestRunner_cn import HTMLTestRunner
from page.newloginpage import LoginPage

class TestLogin(BasePage):

  def setUp(self):
        super(TestLogin,self).setUp()
        self.page = LoginPage(self.driver)
        self.page.get("https://www.douban.com")
        self.driver.implicitly_wait(5)

  def test_login(self):
        self.driver.switch_to.frame(0)
        print("切换frame")
        self.page.logintab.click()
        self.page.username.send_keys("11111")
        self.page.password.send_keys("11111")
        self.page.login.click()
        assert self.page.username.text == 'secret'



