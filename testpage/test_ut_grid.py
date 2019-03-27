#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time,os,unittest,subprocess,pytest,allure
from selenium import webdriver
from multiprocessing.pool import Pool
import logging
logging.getLogger().setLevel("INFO")

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestGrid(unittest.TestCase):

    def __init__(self, methodName='runTest', param=None):
        super(TestGrid, self).__init__(methodName)
        global devicess
        devicess = param
        logging.info("节点地址:" + devicess)


    def init_hub_drvier(self):
        logging.info("init_hub_drvier")
        chromedriver = PATH("../webdriver/chromedriver_mac")
        logging.info(chromedriver)
        os.environ["webdriver.chrome.driver"] = chromedriver
        chrome_capabilities = {
            "browserName": "chrome",  # 浏览器名称
            "version": "",  # 操作系统版本
            "platform": "ANY",  # 平台，这里可以是windows、linux、andriod等等
            "javascriptEnabled": True,  # 是否启用js
            "webdriver.chrome.driver": chromedriver
        }
        self.driver = webdriver.Remote(command_executor=devicess,
                                       desired_capabilities=chrome_capabilities)
        # hub地址
        logging.info(self.driver)
        return self.driver



    def test_ut(self):
        self.driver = self.init_hub_drvier()
        self.driver.get("http://www.douban.com")
        logging.info("test_ut")
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':


    def run(device):
        suite = unittest.TestSuite()
        suite.addTest(TestGrid('test_ut', param=device))
        unittest.TextTestRunner(verbosity=2).run(suite)


    def runner_pool():
        devices_Pool = ["http://192.168.56.1:5555/wd/hub", "http://192.168.56.1:6666/wd/hub"]
        pool = Pool(len(devices_Pool))
        pool.map(run, devices_Pool)
        pool.close()
        pool.join()

    logging.info("********开始测试********")
    runner_pool()
    logging.info("********结束测试********")


