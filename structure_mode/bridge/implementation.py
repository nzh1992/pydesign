# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/19 11:29
@Contact : nzh199266@163.com
@Desc    : 实现模块
"""
from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation(self) -> str:
        """overwrite operation"""
        return "ConcreteImplementationA operation."


class ConcreteImplementationB(Implementation):
    def operation(self) -> str:
        """overwrite operation"""
        return "ConcreteImplementationB operation."
