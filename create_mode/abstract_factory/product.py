# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/8 11:49
@Contact : ziheng.ni@envision-energy.com
@Desc    : 产品模块
"""
from abc import ABC, abstractmethod


############### 椅子 ###################
class Chair(ABC):
    @abstractmethod
    def produce(self):
        pass


class ArtChair(Chair):
    def produce(self):
        return "Art chair"


class VictoriaChair(Chair):
    def produce(self):
        return "Victoria chair"


class ModernChair(Chair):
    def produce(self):
        return "Modern chair"


############### 桌子 ###################
class Table(ABC):
    @abstractmethod
    def produce(self):
        pass


class ArtTable(Table):
    def produce(self):
        return "Art table"


class VictoriaTable(Table):
    def produce(self):
        return "Victoria table"


class ModernTable(Table):
    def produce(self):
        return "Modern table"
