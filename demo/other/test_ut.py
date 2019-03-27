#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
'''
headless模式
'''

# from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(executable_path='/root/chromedriver_mac', chrome_options=chrome_options,
#   service_args=['--verbose', '--log-path=/root/chromedriver_mac.log'])
# driver.get("https://www.baidu.com")
sysstr = platform.system()
print(sysstr)