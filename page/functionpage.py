#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time,os,unittest,subprocess,allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import *
from driver.wdriver import WDriver
from functools import wraps
from allure.constants import AttachmentType
from PIL import Image


class FunctionPage():

    @staticmethod
    def screen_shot():
        print("screen_shot")
        def decorator(func):
            def wrapper(*args, **kw):
                # print('%s():' % (func.__name__))
                with allure.step('添加截图'):
                    allure.attach('添加截图', WDriver().get_driver().get_screenshot_as_png(), type=AttachmentType.PNG)
                f = func(*args, **kw)
                with allure.step('添加截图'):
                    allure.attach('添加截图', adb_screen_shot(), type=AttachmentType.PNG)
                return f
            return wrapper
        return decorator


    def screen_full_shot():
        '''
        全屏截图
        :return:
        '''
        pass