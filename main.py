#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,sys,unittest,os
from page_objects import PageObject, PageElement
from selenium import webdriver
from testpage.test_report_screen_shot import TestLogin
from unittest import TestLoader
from HTMLTestRunner_cn.HTMLTestRunner_cn import HTMLTestRunner


if __name__ == '__main__':

    test_suit = TestLoader().loadTestsFromTestCase(TestLogin)

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())

    reportpath = os.path.join(os.getcwd(), 'SeleniumReport')
    if not os.path.exists(reportpath):
        os.mkdir(reportpath)
    filename = os.path.join(reportpath, now + "_result.html")
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(
        stream=fp,
        title=u'SeleniumReport自动化执行报告',
        description=u'用例执行情况:',
        verbosity=2, retry=0, save_last_try=True)
    # verbosity表示报告级别
    # retry表示失败重试机制
    runner.run(test_suit)
    fp.close()