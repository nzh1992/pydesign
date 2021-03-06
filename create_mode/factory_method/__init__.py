# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/7 15:03
@Contact : nzh199266@163.com
@Desc    : 工厂方法模式
"""

# 工厂方法模式
#
# 也称：虚拟构造函数、Virtual Constructor、Factory Method。
# 核心理念是：在父类中提供一个创建对象的方法，允许子类决定实例化对象的类型。
# 优势：
#   1. 将创建”产品“的代码和实际使用”产品“的代码分离，从而能在不影响其他代码的情况下进行扩展。
#   2. 单一职责原则。你可以将“产品”创建的代码放在程序的单一位置，从而提高可维护性。
#   3. 开闭原则。无需更改现有客户端代码，就可以在程序中引入新的“产品”类型。
# 劣势：
#   1. 应用了工厂方法会引入许多新的子类，代码因此变得更加复杂。最好的情况是将该模式引入创建者类的现有层次结构中。


# 业务场景
# 假设你正在开发一款物流应用，最初版本只能处理卡车运输，因此大部分代码都在名为“卡车”的类中。
# 一段时间后，你每天都能收到十几次来自海运公司的请求，希望应用能够支持海上物流功能。


# 改动分析
# 如果代码其余部分与现有类已经存在耦合关系，那么向程序中添加新类并不容易，因为所有的“卡车”类都要被修改。
# 更糟糕的是，下次再有其他类型的运输方式加入时，还会对“卡车”类和“海运”类进行大幅修改。


# 解决方案
# 用工厂方法替代对象的直接调用，换句话来说就是，修改对象的构造阶段（直接构造->工厂方法构造）。


# 使用场景
# 1. 当你在编写代码的过程中，如果无法预知对象确切类别及其依赖关系时。
# 2. 当你希望用户扩展你的框架或者内部组件时。
# 3. 当你希望复用现有对象来节省系统资源，而不是每次都重新创建对象时。比如数据库连接、文件系统和网络资源。

# ================================================================================================
# 与其他模式的关系
# 1. 在许多设计的初期都会采用工厂方法模式，可以更方便的通过子类进行定制，随后演化为抽象工厂模式、原型模式、生成器模式
# 2. 抽象工厂模式通常基于一组工厂方法，但你也可以使用原型模式来生成这些类的方法。
# 3. 可以同时使用工厂方法模式和迭代器模式，来让子类集合返回不同类型的迭代器，并使得迭代器与集合相匹配。
# 4. 原型模式并不基于继承，因此没有继承的缺点。另一方面，原型模式需要对被复制对象进行复杂的初始化。工厂方法模式基于继承，但是它不需要初始化步骤。
# 5. 工厂方法模式是模板方法模式的一种特殊形式。同时，工厂方法可以作为一个大型模板方法中的一个步骤。
