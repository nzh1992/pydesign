# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/18 15:07
@Contact : ziheng.ni@envision-energy.com
@Desc    : 
"""
from structure_mode.adapter.raw_module import Target
from structure_mode.adapter.adapter_module import Adapter


if __name__ == '__main__':
    # 原来的方法
    target = Target()
    print(target.request())

    # 适配器修改后的方法
    adapter = Adapter()
    print(adapter.request())
