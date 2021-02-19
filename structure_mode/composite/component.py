# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/19 14:21
@Contact : ziheng.ni@envision-energy.com
@Desc    : 组件模块
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    组件抽象类，声明了复杂对象和简单对象的公共操作方法。
    """
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """用于客户端判断是不是复杂组件"""
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(Component):
    """
    '叶节点'类
    """
    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    用于表示复杂对象类
    """
    def __init__(self):
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())

        return f"Branch({'+'.join(results)})"
