# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/19 11:36
@Contact : nzh199266@163.com
@Desc    : 客户端使用
"""
from structure_mode.bridge.abstract import Abstraction, ExtendedAbstraction
from structure_mode.bridge.implementation import ConcreteImplementationA, ConcreteImplementationB


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation())


if __name__ == '__main__':
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    implementation2 = ConcreteImplementationB()
    extend_abstraction = ExtendedAbstraction(implementation2)
    client_code(extend_abstraction)