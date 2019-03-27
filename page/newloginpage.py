#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,sys,unittest,os
from page_objects import PageObject, PageElement
from selenium import webdriver


class LoginPage(PageObject):
        '''
        登录页面
        '''
        logintab = PageElement(class_name='account-tab-account')
        username = PageElement(id_='username')
        password = PageElement(name='password')
        login = PageElement(link_text='登录豆瓣')