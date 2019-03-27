#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time,os,unittest,subprocess,pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException


# browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac")
# executable_path来指定chromedirver路径

# browser = webdriver.Firefox(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/geckodriver")

browser = webdriver.Safari()

browser = webdriver.Ie()

# browser.set_network_conditions(
#                 offline=False,
#                 latency=5,  # additional latency (ms)
#                 download_throughput=1 * 1024,  # maximal throughput
#                 upload_throughput=1 * 1024)  # maximal throughput)


# browser.get("https://www.douban.com")

browser.get("https://www.helloweba.net/demo/2017/unlock/")
# print("登录douban")
#
# print(browser.get_window_size())
# # 获取窗口页面当前高和宽
#
# print(browser.get_window_position())
#
# print(browser.get_cookies())

print(browser.set_network_conditions(
                offline=False,
                latency=5,  # additional latency (ms)
                download_throughput=500 * 1024,  # maximal throughput
                upload_throughput=500 * 1024)  # maximal throughput)
            )
# print(browser.get_network_conditions())
#
# print(browser.set_page_load_timeout(10))

# print(browser.title)

# print(browser.page_source)

# print(browser.forward())
#
# print(browser.forward())
#
# print(browser.back())

# print(browser.name)
#
# print(browser.current_url)
#
# print(browser.maximize_window())
#
# print(browser.minimize_window())

# print(browser.set_window_size(300,300))


# app = browser.find_element(By.CLASS_NAME,"lnk-app")
# atcion.click(app)

# atcion.send_keys("11111")
# browser.save_screenshot("/Users/xinxi/PycharmProjects/selenium_demo/screen_folder/截图.png")

sc_str = browser.get_screenshot_as_png()
sc_path = "/Users/xinxi/PycharmProjects/selenium_demo/screen_folder/截图.png"
with open(sc_path,"w") as f:
    f.write(sc_str)



#获取拖动条
dragger = browser.find_elements_by_class_name("slide-to-unlock-handle")[0]
#获取拖动条进度条长度
dragger_text = browser.find_elements_by_class_name("slide-to-unlock-bg")[0]
x = dragger_text.location["x"]
action = ActionChains(browser)
 #鼠标左键按下不放
action.click_and_hold(dragger).perform()
#平行移动大于解锁的长度的距离
try:
    action.drag_and_drop_by_offset(dragger,x, 0).perform()
    print("滑动...")
except Exception as e:
    print("faild")
#
# #等待2秒，方便捕捉弹框
#
# 打印警告框提示

time.sleep(10)
try:
    tt = browser.switch_to_alert()
    print("打印警告框提示...")
except Exception as e:
    print("faild")
success_text = tt.text
print(success_text)
tt.accept()


sc_str = browser.get_screenshot_as_base64()
html_tmp = """
<html>
<body>

<h1>这是一个截图</h1>
<img src="data:image/png;base64,{}"/>
</body>
</html>
""".format(sc_str)
html_path = "/Users/xinxi/PycharmProjects/selenium_demo/screen_folder/截图.html"
with open(html_path,"w") as f:
    f.write(html_tmp)



time.sleep(5)

# browser.quit()





# #滑到底部
# js="window.scrollTo(0,document.body.scrollHeight)"
# browser.execute_script(js)
#
# time.sleep(3)
#
# #滑动到顶部
# js="window.scrollTo(0,0)"
# browser.execute_script(js)