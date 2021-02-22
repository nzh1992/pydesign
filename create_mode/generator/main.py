# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/8 17:51
@Contact : nzh199266@163.com
@Desc    : 
"""
from create_mode.generator.director import Director
from create_mode.generator.builder import HouseBuilder


if __name__ == '__main__':
    director = Director()
    builder = HouseBuilder()
    director.builder = builder

    print("基础构建：")
    director.build_mini_product()
    director.builder.product.list_parts()

