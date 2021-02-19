# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/18 15:13
@Contact : ziheng.ni@envision-energy.com
@Desc    : 桥接模式
"""

# 桥接模式
# 桥接模式是一种结构型设计模式，可将一个大类或者一系列紧密相关的类拆分为抽象和实现两个独立的层次结构，从而能在开发时分别使用。


# 适用场景
# 1. 如果你想要拆分或者重组一个具有多重功能的庞杂类
# 2. 如果你希望在几个独立维度上扩展一个类，可以用该模式
# 3. 如果你希望在运行时切换不同实现方法，可以使用桥接模式


# 优势：
# 1. 你可以创建与平台无关的类和程序
# 2. 客户端代码仅与高层抽象部分(Abstraction类)进行互动，不会接触到平台的相关信息
# 3. 开闭原则。你可以新增抽象部分和实现部分，但它们之间不会相互影响
# 4. 单一职责原则。抽象部分专注于高层逻辑，实现部分专注于处理平台细节
#
# 劣势：
# 1. 对高内聚的类使用桥接模式可能会让代码变得更加复杂，因为需要分为抽象类和实现类，并通过接口进行交互


# 与其他设计模式的关系
# 1. 桥接模式通常用于开发前期设计，使你能够将程序的各个部分独立出来，以便于开发。
#    适配器模式通常在已有程序中使用，用于兼容已有类。
# 2. 桥接模式、状态模式、策略模式的接口比较相似。
#    实际上，它们都是基于组合模式（将工作委派给其他对象）。
#    模式并不只是以特定的方式组织代码，重点是解决了什么问题。
# 3. 可以将抽象工厂模式和桥接模式搭配使用。
#    如果由桥接模式定义的抽象类只能与特定实现合作，这一模式会非常有用。
#    这种情况下，抽象工厂模式可以对这些关系进行封装，并对客户端隐藏其复杂性。
# 4. 可以结合使用生成器模式和桥接模式，主管类负责抽象工作，各种不同的生成器负责具体实现工作。