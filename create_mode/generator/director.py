# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/9 10:24
@Contact : nzh199266@163.com
@Desc    : 
"""
from create_mode.generator.builder import Builder


class Director(object):
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_mini_product(self) -> None:
        self._builder.produce_part_1()

    def build_full_product(self) -> None:
        self._builder.produce_part_1()
        self._builder.produce_part_2()
        self._builder.produce_part_3()
