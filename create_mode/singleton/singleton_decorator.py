# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/18 11:19
@Contact : ziheng.ni@envision-energy.com
@Desc    : 
"""
# 方法一，函数装饰器
def singleton(cls):
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)

        return _instance[cls]

    return inner


# 方法二，类装饰器
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls(*args, **kwargs)

        return self._instance[self._cls]


# @singleton
@Singleton
class Configuretion(object):
    def __init__(self, x):
        print("Initialize, ", x)
