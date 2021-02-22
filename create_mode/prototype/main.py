# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/9 11:24
@Contact : nzh199266@163.com
@Desc    : 
"""
import copy

from create_mode.prototype.product import Product, Component


if __name__ == '__main__':
    listlist_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circul_ref = Product()
    component = Component(23, listlist_of_objects, circul_ref)
    circul_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)
    print(shallow_copied_component)