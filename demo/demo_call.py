#!/usr/bin/env python
# -*- coding: utf-8 -*-



# https://foofish.net/magic-method.html
# 简述 __init__、__new__、__call__ 方法

class A(object):
    def __init__(self):
        print("__init__ ")
        super(A, self).__init__()

    def __new__(cls):
        print("__new__ ")
        return super(A, cls).__new__(cls)

    def __call__(self):  # 可以定义任意参数
        print('__call__')

a = A()
print(callable(a))
a() # 实例像函数一样可调用


# 单例模式
# 这就是通过 __new__ 方法是实现单例模式的的一种方式，
# 如果实例对象存在了就直接返回该实例即可，
# 如果还没有，那么就先创建一个实例，再返回
class BaseController(object):
    _singleton = None
    def __new__(cls, *a, **k):
        if not cls._singleton:
            cls._singleton = object.__new__(cls, *a, **k)
        return cls._singleton








