# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/18 11:14
@Contact : ziheng.ni@envision-energy.com
@Desc    : 
"""

from create_mode.singleton.singleton_meta import Configuretion as Config1
from create_mode.singleton.singleton_decorator import Configuretion as Config2
from create_mode.singleton.singleton_newfunc import Configuretion as Config3

if __name__ == '__main__':
    # 1. 使用 元类
    # my_config1 = Config1(1)
    # print(id(my_config1))
    #
    # my_config2 = Config1(2)
    # print(id(my_config2))

    # 2. 使用 装饰器
    # my_config1 = Config2(1)
    # print(id(my_config1))
    #
    # my_config2 = Config2(2)
    # print(id(my_config2))

    # 3. 使用 new 函数
    my_config1 = Config3(1)
    print(id(my_config1))

    my_config2 = Config3(2)
    print(id(my_config2))

