#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 代码->selenium库->webdriver—>浏览器

driver = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac")
driver.get("https://www.baidu.com")
# time.sleep(5)
# driver.quit()
time.sleep(3)
driver.find_element()
# driver.find_element_by_name("tj_trnews").click()
# driver.find_element_by_id("kw").send_keys("test.....")
# driver.find_element_by_class_name("mnav").click()

# driver.find_element_by_link_text("学术").click()

#driver.find_element_by_xpath('//*[@id="kw"]').click()

# driver.find_element_by_partial_link_text("地").click()

driver.find_element_by_tag_name("span").click()

time.sleep(3)


