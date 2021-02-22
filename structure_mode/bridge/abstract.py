# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/19 11:28
@Contact : nzh199266@163.com
@Desc    : 抽象模块
"""
from structure_mode.bridge.implementation import Implementation


class Abstraction(object):
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self) -> str:
        """depend on class of implementation module"""
        return f"Abstraction base operation with: {self.implementation.operation()}"


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return f"ExtendedAbstraction operation with: {self.implementation.operation()}"

