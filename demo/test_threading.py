# coding:utf-8
import threading
import time


def test(value):
    print('start test')
    time.sleep(3)  # 休息3秒
    print('input %s' % value)



class Test(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value

    # 继承Thread类需要显示run方法，线程在开启后运行
    def run(self):
        print('start test')
        time.sleep(3)  # 休息3秒
        print('input %s' % self.value)


# if __name__ == '__main__':
#     t = threading.Thread(target=test, args=(u'xxx',))
#     t.start()
#     print('end input')


if __name__ == "__main__":
    test = Test(u'xxx')
    test.start() #开启线程，会自动执行run方法
    print('end input')
