# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/8 17:31
@Contact : ziheng.ni@envision-energy.com
@Desc    : 
"""
from __future__ import annotations
from abc import ABC, abstractmethod

from create_mode.generator.product import Product1


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @property
    @abstractmethod
    def produce_part_1(self) -> None:
        pass

    @property
    @abstractmethod
    def produce_part_2(self) -> None:
        pass

    @property
    @abstractmethod
    def produce_part_3(self) -> None:
        pass


class HouseBuilder(Builder):
    def __init__(self) -> None:
        self._product = None
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> None:
        product = self._product
        self.reset()
        return product

    def produce_part_1(self) -> None:
        self._product.add("part 1")

    def produce_part_2(self) -> None:
        self._product.add("part 2")

    def produce_part_3(self) -> None:
        self._product.add("part 3")


