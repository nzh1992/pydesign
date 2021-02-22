# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/22 9:54
@Contact : ziheng.ni@envision-energy.com
@Desc    : 
"""
from structure_mode.decorator.component import ConcreteDecoratorA, ConcreteDecoratorB, ConcreteComponent, Component


def client_code(component: Component) -> None:
    print(f"client: {component.operation()}")


if __name__ == '__main__':
    simple = ConcreteComponent()
    client_code(simple)


    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    client_code(decorator2)
