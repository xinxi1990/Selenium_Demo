#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : xinxi
@Time    : 2018/12/5 18:34
@describe: 运行入口
"""
import sys,os,shutil
reload(sys)
sys.setdefaultencoding( "utf-8" )
import pytest,os,subprocess
import configparser

def clean_data():
    try:
        cmd = shutil.rmtree("./data")
        subprocess.call(cmd, shell=True)
        print("清理环境...")
    except Exception as e:
        print(e)

def init_report():
    cmd = "allure generate --clean data -o reports"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    print("报告地址:{}".format(report_path))

clean_data()
pytest.main(["-q","-v","-s","--reruns=0", "testpage/test_loginpage.py","--alluredir=data"])
init_report()