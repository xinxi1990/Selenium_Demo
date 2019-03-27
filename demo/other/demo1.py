#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac")
# executable_path来指定chromedirver路径
browser.get('https://www.baidu.com')





# browser.find_element_by_id("result_logo").click()

# browser.find_element_by_name("tj_trnews").click()

# browser.find_element_by_class_name("mnav").click()
#
# browser.find_element_by_link_text("地图").click()


# browser.find_element_by_xpath('//*[@id="result_logo"]').click()

# browser.find_element_by_css_selector('#form').click()

# browser.find_element_by_partial_link_text("地").click()

browser.find_element_by_tag_name("span").click()