# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/20 16:13
@Contact : ziheng.ni@envision-energy.com
@Desc    : 装饰器组件
"""


class Component(object):
    """所有组件基类"""
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """具体的业务组件"""
    def operation(self) -> str:
        return "ConcreteComponent operation."


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    具体的组件实现类
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorA: {self.component.operation()}"


class ConcreteDecoratorB(Decorator):
    """
    具体的组件实现类
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorB: {self.component.operation()}"