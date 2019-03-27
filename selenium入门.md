# selenium介绍

官方文档:https://www.seleniumhq.org

![image](http://note.youdao.com/yws/res/21128/986223E08AF94210875C9DBA99D1066C)

简单来说就是做web自动化测试框架,可测试不同的浏览器.


# webdriver系统架构
![selenium.jpg](http://note.youdao.com/yws/res/21119/WEBRESOURCEa43b08b4fab01df66e558e2a584ffcd1)


# 环境搭建

- python2.7或者3.6
- pycharm编辑器
- chrome浏览器
- chrome webdriver


## 安装selenium
https://pypi.org/project/selenium/
```
pip install selenium
```
## chrome webdriver选择版本
查看chrom浏览器的版本,需要下载其对应版本的chrome webdriver.

![image](https://note.youdao.com/src/9AE20746709C4358BD52042F2D665A5D)

下载对照表<br>
https://sites.google.com/a/chromium.org/chromedriver/downloads

![image](http://note.youdao.com/yws/res/21148/FDB4D5C8156647FDBF405DBB93572448)


## 不同浏览器的driver


- browser = webdriver.Chrom()
- browser = webdriver.Firefox()
- browser = webdriver.Safari()
- browser = webdriver.Ie()

# 第一个demo

使用chrome浏览器打开百度

```
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
```

![image](http://note.youdao.com/yws/res/21155/4EDB3F7B8F4F4B4BA180D4560DA76CB1)

报错提示需要指定"chromedriver"路径.

解决方案下载对应版本的chromedriver,代码改动如下:
```
from selenium import webdriver
browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac")
# executable_path来指定chromedirver路径
browser.get('https://www.baidu.com')
```
指定代码,会启动一个chrome浏览器并且打开百度首页.


# 元素定位

web页面所有的元素最终都是以html格式展示.

使用chrome浏览器,右键查看页面元素.把鼠标定位到元素上,页面会自动定位到页面上.

![image](https://note.youdao.com/src/7DAE78FA4C5443099CB54328608277F3)

所以做web自动化的关键点是如何操作这些元素,模拟点击、滑动、长按等操作.

selenium提供了八种元素定位方式

# name定位

![image](https://note.youdao.com/src/5C2BF305C6FF4B85A6A47488D63586A9)

```
browser.find_element_by_name("tj_trnews").click()
```

# id定位

![image](https://note.youdao.com/src/0C055A47DD7348F9AAD3C9365D1424EF)
```
browser.find_element_by_id("result_logo").click()
```

# class定位

![image](https://note.youdao.com/src/66A698F7EC3D455C899CB18DAEE29CD6)
```
browser.find_element_by_class_name("mnav").click()
```

# link text定位

![image](https://note.youdao.com/src/A2DD77139A7240D99AC59D88ACD1A9E4)
```
browser.find_element_by_link_text("地图").click()
```

xpath定位
```
browser.find_element_by_xpath('//*[@id="result_logo"]').click()
```

css定位
```
browser.find_element_by_css_selector('#form').click()
```

partial link text定位

通过链接文本的部分匹配来标识元素

```
browser.find_element_by_partial_link_text("地").click()
```

tag name定位

使用h1、a、span这种标签定位.

![image](https://note.youdao.com/src/7EE94B60BB3A44C882A39B47C5963F22)
```
browser.find_element_by_tag_name("span").click()
```

## 定位选择顺序

id > class > name > link_text > xpath > csss

# frame切换
<frame> 是HTML元素，它定义了一个特定区域，另一个HTML文档可以在里面展示.

```
<html>
<frameset cols="25%,50%,25%">
<frame src="/example/html/frame_a.html"> <frame src="/example/html/frame_b.html"> <frame src="/example/html/frame_c.html">
</frameset> </html> 
```
![image](http://note.youdao.com/yws/res/21235/7B34CFA244EF41E6BDB3E736374B1F10)
# 

由此可见不同的frame包含不用的元素里里边. douban⽹⾸⻚为例例,通过元素检查登录区域是一个frame区域

![image](http://note.youdao.com/yws/res/21243/C9B590C851724DBE9883E0F8F7513C14)

那⽤⾃动化脚本点击"密码登录"按钮,代码如下:

```
from selenium import webdriver
browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac") # executable_path来指定chromedirver路路径
browser.get("https://www.douban.com")
print("登录douban")
browser.find_element_by_class_name('account-tab-account').click()
print("点击密码登录")
```
错误提示如下:

```
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element:
{"method":"class name","selector":"account-tab-account"}
```
修改代码如下:
```
browser.switch_to.frame(browser.find_elements_by_tag_name("iframe")[0]) print("切换frame") browser.find_element_by_class_name('account-tab-account').click() print("点击密码登录")
```
此时代码运行正常,说明点击"元素"之前说明需要切换到该frame上. selenium提供了了switch_to.frame方法
用法如下:
```
driver.switch_to.frame('frame_name') # 使⽤用名字
driver.switch_to.frame(0) # 使⽤用名字 # 使⽤用位置序号 driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0]) # 使⽤用标签序号
```

# windows切换
在web⻚页⾯面上经常有点击一个页⾯后,另外打开一个新窗口.是因为html中target参数是"_bank"控制.

![image](https://note.youdao.com/src/BCFEE1866CDF4B8AA4901DE3C56F366F)

所以在做⾃动化测试过程中,点击跳转以后.页⾯句柄还在当⻚面,所以不能点击跳转以后的页面元素. 所以此时需要切换windows,selenium提供了了switch_to.frame⽅法
⽤法如下:
```
driver.switch_to.window('main') window的名字
```
代码如下:
```
from selenium import webdriver
browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac") # executable_path来指定chromedirver路路径
browser.get("https://www.douban.com")
print("登录douban")
browser.find_element_by_class_name("lnk-book").click() print("点击读书")
handles_list = browser.window_handles print(handles_list) browser.switch_to.window(str(handles_list[-1])) print("切换窗⼝口")
if browser.current_window_handle == str(handles_list[-1]): print("切换窗⼝口成功...")
```

# 等待
等待的⽬目的主要是为了页面加载完成才点击元素,避免找不到元素的现象. 一共有三种等待:

## 硬编码等待
```
time.sleep(1) ,不不推荐
```

## 全局隐示等待
```
browser.get("https://www.douban.com") print("登录douban")
browser.implicitly_wait(10) # 会等待每个元素最⼤大时间10s browser.find_element_by_class_name("lnk-book").click() print("点击读书")
```
## 显示等待
```
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "lnk-book"))).click() # 显示等待lnk-book 5s
```
使⽤用⽅方式:显示等待 > 全局隐示等待 > 硬编码等待

# 常用方法

## 获取窗口大小
```
print browser.get_window_size() # 获取窗⼝口⻚页⾯面当前⾼高和宽
```

## 获取cookies
```
print(browser.get_cookies())
```
## 设置网络
```
print(browser.set_network_conditions(
                offline=False,
                latency=5,  # additional latency (ms)
                download_throughput=500 * 1024,  # maximal throughput
                upload_throughput=500 * 1024)  # maximal throughput)
            )
```

## 获取title
```
print(browser.title)
```
## 获取页面元素
```
print(browser.page_source)
```

## 获取页面url
```
print(browser.current_url)
```

## 页面放大
```
browser.maximize_window()
```

## 页面缩小
```
browser.minimize_window()
```
## 设置页面大小
```
browser.set_window_size(300,300)
```

## 向前
```
browser.forward()
```
## 后退
```
browser.back()
```

## 滑动

```
#滑到底部 js="window.scrollTo(0,document.body.scrollHeight)" browser.execute_script(js)
```

```
#滑动到顶部 js="window.scrollTo(0,0)" browser.execute_script(js)
```

## 滑动解锁

https://www.helloweba.net/demo/2017/unlock/

![image](https://note.youdao.com/src/7E3ACE2AD68F42E7A6D5AC63FA931AD5)

```
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
```
![image](https://note.youdao.com/src/EBA16BEFA31F4E7CA5441C985D25AFAA)


## 关闭弹框

![image](https://note.youdao.com/src/BFC05B6D653240BD9C7CB46C19C50590)

```
time.sleep(10)
try:
    tt = browser.switch_to_alert()
    print("打印警告框提示...")
except Exception as e:
    print("faild")
success_text = tt.text
print(success_text)
tt.accept()
```


# 截图
## 保存截图
```
browser.save_screenshot("/Users/xinxi/PycharmProjects/selenium_demo/screen_folder/截图.png")
```
## 图片流截图
```
sc_str = browser.get_screenshot_as_png()
sc_path = "/Users/xinxi/PycharmProjects/selenium_demo/screen_folder/截图.png"
with open(sc_path,"w") as f:
    f.write(sc_str)
```
## base64截图
```
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
```

![image](http://note.youdao.com/yws/res/21339/720E7015B8D14CB299C769778EC3B632)



# 断言

# PO模式

# 报告

# jenkins持续集成


# linux下执行

离线安装:setuptools、selenium


安装allure
```
wget https://github.com/allure-framework/allure-core/releases/download/allure-core-1.5.2/allure-commandline.tar.gz

tar -xvf allure-commandline.tar.gz

cd bin/
ls
allure  allure.bat

vi /etc/profile 

export allure_home=/root
export PATH=${allure_home}/bin:${PATH}

 source /etc/profile

```

# 学习贴
linux下执行<br>
https://blog.csdn.net/qq_41963758/article/details/80320309


