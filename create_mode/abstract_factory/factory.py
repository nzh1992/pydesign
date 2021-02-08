# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/8 11:45
@Contact : ziheng.ni@envision-energy.com
@Desc    : 工厂模块
"""
from abc import ABC, abstractmethod

from .product import ArtChair, ArtTable, VictoriaChair, VictoriaTable, ModernChair, ModernTable


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class ArtFactory(AbstractFactory):
    def create_chair(self):
        return ArtChair().produce()

    def create_table(self):
        return ArtTable().produce()


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return VictoriaChair().produce()

    def create_table(self):
        return VictoriaTable().produce()


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return ModernChair().produce()

    def create_table(self):
        return ModernTable().produce()