# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/7 17:07
@Contact : nzh199266@163.com
@Desc    : 
"""
from abc import ABC, abstractmethod


class Product(ABC):
    """
    产品抽象类
    """
    @abstractmethod
    def operation(self) -> str:
        pass


class Truck(Product):
    """
    具体产品：卡车
    """
    def operation(self) -> str:
        return "create truck."


class Ship(Product):
    """
    具体产品：船
    """
    def operation(self) -> str:
        return "create ship."
