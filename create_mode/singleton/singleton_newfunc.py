# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/18 11:29
@Contact : ziheng.ni@envision-energy.com
@Desc    : 
"""


class Configuretion(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self, x):
        print("Initialize, ", x)