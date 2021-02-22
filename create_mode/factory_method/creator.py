# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/7 16:57
@Contact : nzh199266@163.com
@Desc    : 
"""
from __future__ import annotations
from abc import ABC, abstractmethod

from create_mode.factory_method.product import Product, Truck, Ship


class Creator(ABC):
    """
    构造器抽象类。
    factory_method方法用于所有子类提供实例化后的对象。
    some_operation方法用于在获取子类对象后做一些操作，比如日志等信息。
    """
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: {product.operation()}"

        return result


class TruckCreator(Creator):
    """
    卡车构造器
    """
    def factory_method(self) -> Product:
        return Truck()


class ShipCreator(Creator):
    """
    船构造器
    """
    def factory_method(self):
        return Ship()
