#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用自定义报告
"""

import time,sys,unittest,os,shutil
from page_objects import PageObject, PageElement
from selenium import webdriver
from testpage.test_report_screen_shot import TestLogin
from unittest import TestLoader
from AutoReport.MyRunner import HTMLTestRunner
from AutoReport.GenReport import GenReport



if __name__ == '__main__':

    test_suit = TestLoader().loadTestsFromTestCase(TestLogin)
    # now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    # print('All case number')
    # print(test_result.testsRun)
    # print('Failed case number')
    # print(len(test_result.failures))
    # print('Failed case and reason')
    # for case, reason in test_result.failures:
    #     print(case.id())
    #     print(reason)

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
    result = runner.run(test_suit)
    # print(result.total_image)
    test_data = result.gen_totoal_reuslt()
    GenReport(test_data).render_reprot()
    fp.close()

