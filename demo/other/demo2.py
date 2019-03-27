#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import pytest
from parameterized import parameterized

class TestCase(object):

    # @pytest.mark.parametrize("a,b", [
    # ("3+5", 8),
    # ("2+4", 6),
    # ("6*9", 42),
    # ])
    # def test_1(self, a, b):
    #     print(a)
    #     print(b)
    #     assert eval(a) == b


    @parameterized.expand([["One", "Two"], ["Three", "Four"], ["Five", "Six"], ])
    def test_p(self, arg1, arg2):
        print("test_parameterized")
        print("arg1:{}".format(arg1))
        print("arg2:{}".format(arg2))




import configparser
import os
from PIL import Image
class TestDemo():


    cf = configparser.ConfigParser()
    # 修改配置文件的内容

    # remove_section(section)  删除某个section的数值
    # remove_option(section,option) 删除某个section下的option的数值
    print(cf.read("pwd.ini"))
    sections = cf.items("username")
    print(sections)
    # cf.remove_option("kafka", "user")
    # cf.remove_section("mq")
    #
    # # write to file
    # with open("test1.ini", "w+") as f:
    #     cf.write(f)
    #
    # im = Image.SAVE("my.jpg")  ##文件存在的路径
    # im.show()

if __name__ == '__main__':
    TestDemo()
