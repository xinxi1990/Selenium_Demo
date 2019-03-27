#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time,os,unittest,subprocess,pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import *



class Demo(unittest.TestCase):

    project_path = os.path.abspath(os.path.dirname(__file__))
    screen_png = os.path.join(project_path,str(time.time()) + "_截图.png")

    def setUp(self):
        print("setUp")
        chrome_options = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-infobars') # 不展示chrome控制导航栏
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path=self.project_path + "/webdriver/chromedriver_mac",chrome_options=chrome_options)
        self.driver.implicitly_wait(5)

    def test_demo(self):
        self.driver.get("https://www.douban.com")
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])
        print("切换frame")
        self.driver.find_element_by_class_name('account-form-link').click()
        handles_list = self.driver.window_handles
        print(handles_list)
        self.driver.switch_to.window(str(handles_list[-1]))
        print("切换窗口")
        if self.driver.current_window_handle == str(handles_list[-1]):
            print("切换窗口成功...")
        self.driver.find_element_by_link_text("帐号注册").click()
        print("点击帐号注册")

    @pytest.mark.parametrize("a,b", [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 42),
    ])
    def test_1(self, a, b):
        print(a)
        print(b)
        assert eval(a) == b


    # @pytest.mark.parametrize("account,pwd", [("18513571170", "1233211")])
    # @pytest.mark.parametrize('username, password',[('********', '*******')])
    # def test_login(self,username,password):
    #     '''
    #     账号密码登录
    #     检查登录是否成功
    #     :return:
    #     '''
    #     print(account)
    #     print(pwd)
    #     assert eval(account) ==pwd
        # self.driver.get("https://www.douban.com")
        # self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])
        # print("切换frame")
        # account_tab_account = self.driver.find_element_by_class_name('account-tab-account')
        # account_tab_account.click()
        # print("点击密码登录...")
        # self.driver.execute_script("arguments[0].style.background = 'rgb(138,43,226 )';", account_tab_account)
        # time.sleep(5)
        # self.driver.find_element_by_class_name('account-form-input').clear()
        # self.driver.find_element_by_class_name('account-form-input').send_keys(user_name)
        # self.driver.find_element_by_id('password').clear()
        # self.driver.find_element_by_id('password').send_keys(pwd)
        # self.driver.find_element_by_class_name("account-form-field-submit").click()
        # print("点击登录")
        # time.sleep(5)
        # if account_name in str(self.driver.page_source).encode("utf-8"):
        #     print("登录成功...")
        #     assert True
        # else:
        #     print("登录失败...")
        #     self.driver.save_screenshot(self.screen_png)
        #     assert False
        # self.driver.save_screenshot(self.screen_png)

    # def test_demo_1(self):
    #     driver.execute_script("return((window.jQuery != null) && (jQuery.active === 0))") == True
    #     # 判断整个页面是否loader完成



    def tearDown(self):
        self.driver.quit()