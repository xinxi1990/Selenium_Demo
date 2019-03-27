from selenium import webdriver
import time
def capture(url, filename="capture.png"):
  browser = webdriver.Chrome(executable_path="/Users/xinxi/PycharmProjects/selenium_demo/webdriver/chromedriver_mac")
  # browser.set_window_size(1200, 900)
  browser.get(url) # Load page
  browser.execute_script("""
  (function () {
   var y = 0;
   var step = 100;
   window.scroll(0, 0);
   function f() {
    if (y < document.body.scrollHeight) {
     y += step;
     window.scroll(0, y);
     setTimeout(f, 50);
    } else {
     window.scroll(0, 0);
     document.title += "scroll-done";
    }
   }
   setTimeout(f, 1000);
  })();
 """)
  for i in range(30):
    if "scroll-done" in browser.title:
      break
    time.sleep(1)
  beg = time.time()
  for i in range(10):
    browser.save_screenshot(filename)
  end = time.time()
  print(end - beg)
  browser.close()
capture("https://www.jb51.net")