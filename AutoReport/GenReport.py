#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,re,time,subprocess,sys,jinja2,requests,json
from jinja2 import Environment, PackageLoader
from libs.logger import init_logger
logger = init_logger()

project_path = os.path.abspath(os.path.dirname(__file__))
report_folder = os.path.join(project_path,"report")
if not os.path.exists(report_folder):
    os.mkdir(report_folder)
    print("\033[0;32m{0}\033[0m".format("创建报告文件夹:".format(report_folder)))


class GenReport():

    def __init__(self,result_data):
        self.result_data = result_data

    def render_reprot(self,**params):
        '''
        jinja2渲染结果
        :return:
        '''
        db = None
        try:
            env = Environment(loader=PackageLoader('AutoReport', 'template'))
            template = env.get_template("template.html")
            html_content = template.render(result_data=self.result_data)
            current_now = time.strftime("%Y%m%d%H%M%S", time.localtime())
            report_path = os.path.join(report_folder, current_now + "_result.html")
            with open(report_path, "wb") as f:
                f.write(html_content.encode("utf-8"))
                logger.info('报告地址:\n{}'.format(report_path))
        except Exception as e:
            logger.error('生成报告异常!{}'.format(e))
        finally:
            return report_path

