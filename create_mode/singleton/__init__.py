# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/9 16:13
@Contact : nzh199266@163.com
@Desc    : 单例模式
"""

# 单例模式
# 让你的类有且仅有一个实例，并提供一个访问该实例的全局节点。
#
#


# 业务场景
# 控制某些共享资源（例如数据库、文件）的访问权限


# 解决方案
# 所有单例的实现都包含以下两个相同的步骤
# 1. 将默认构造函数设为私有，防止其他对象使用单例类的new运算符。
# 2. 新建一个静态构建方法作为构造函数，改方法会偷偷调用私有构造函数来创建对象，并将其保存在一个静态成员变量中。
#    此后，所有对于该函数的调用都将返回这一缓存对象。


# 适用场景
# 1. 如果程序中的某个类对于所有客户端只有一个可用的实例，可以使用单例模式。
# 2. 如果希望严格的控制全局变量，也可以使用单例模式。
#

