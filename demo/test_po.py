#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,sys,unittest,os
from page_objects import PageObject, PageElement
from selenium import webdriver


class LoginPage(PageObject):
        '''
        登录页面
        '''
        logintab = PageElement(class_name='account-tab-account')
        username = PageElement(id_='username')
        password = PageElement(name='password')
        login = PageElement(link_text='登录豆瓣')



class TestLogin(unittest.TestCase):

  def setUp(self):
        PATH = lambda p: os.path.abspath(
                     os.path.join(os.path.dirname(__file__), p)
        )
        chromedriver = PATH("../webdriver/chromedriver_mac")
        print(chromedriver)
        driver = webdriver.Chrome(
                     executable_path=chromedriver)
        page = LoginPage(driver)
        page.get("https://www.douban.com")
        driver.implicitly_wait(5)
        global driver,page

  def test_login(self):
        driver.switch_to.frame(0)
        print("切换frame")
        page.logintab.click()
        page.username.send_keys("11111")
        page.password.send_keys("11111")
        page.login.click()
        assert page.username.text == 'secret'

  def main(self):
      print("aaaaa")


if __name__ == '__main__':
    unittest.main()