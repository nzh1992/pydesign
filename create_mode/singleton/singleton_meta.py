# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/18 11:09
@Contact : nzh199266@163.com
@Desc    : 
"""
from threading import Lock


class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            # 若要程序支持多线程，必须在此处放置线程锁
            Lock.acquire()
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
            Lock.release()

        return cls._instance[cls]


class Configuretion(metaclass=SingletonMeta):
    def __init__(self, x):
        print("Initialize, ", x)

