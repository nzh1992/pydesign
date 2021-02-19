# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/19 13:59
@Contact : ziheng.ni@envision-energy.com
@Desc    : 组合模式
"""

# 组合模式
# 也称为‘对象树’、Object Tree、Composite
# 组合模式是一种结构型设计模式，你可以使用它将对象组合成树状结构，并且能像使用独立对象一样使用它们。


# 适用场景
# 1. 如果你需要实现树状对象结构，可以使用组合模式。
# 2. 如果你希望客户端代码以相同的方式处理简单和负责元素，可以使用该模式。
#    组合模式中定义的所有元素公用同一个接口，所以客户端不必在意所使用对象的具体类别。


# 优势：
# 1. 你可以利用多态和递归机制更方便地使用复杂树结构。
# 2. 开闭原则。无需更改现有代码，你就可以在应用中添加新元素，使其成为对象树的一部分。
#
# 劣势：
# 1. 对于功能差异较大的类，提供公用接口会非常困难。在特定情况下，你需要统一化组件接口，使其变接口变得难以理解。


# 与其他设计模式的关系
# 1. 你可以在创建复杂的组合树时使用生成器模式，因为这可以使其构造步骤以递归的方式运行。
# 2. 责任链模式通常和组合模式结合使用。
#    在这种情况下，‘叶节点’接受到请求后，可以将请求沿着包含全体父类的链一直传递至对象树的底部。
# 3. 你可以使用迭代器模式遍历组合模式的复杂对象。
# 4. 你可以使用‘访问者’对整个组合树对象执行操作。
# 5. 你可以使用享元模式实现组合树的共享‘叶节点’，用以节省内存。
# 6. 组合模式和装饰模式的结构图很相似，因为两者都依赖递归组合来组织无限数量的对象。
# 7. 大量使用组合模式和装饰模式的设计通常可以应用原型模式，方便克隆对象，而非重新构造。
