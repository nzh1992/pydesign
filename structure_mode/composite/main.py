# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/19 14:36
@Contact : ziheng.ni@envision-energy.com
@Desc    : 客户端代码
"""
from structure_mode.composite.component import Leaf, Component, Composite


def client_code(component: Component) -> None:
    print(f"Result: {component.operation()}")


def client_code2(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)

    print(f"Result: {component1.operation()}")



if __name__ == '__main__':
    # 简单对象
    simple_leaf = Leaf()
    client_code(simple_leaf)

    print("complex object operations")

    # 复杂对象
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    client_code2(tree, simple_leaf)