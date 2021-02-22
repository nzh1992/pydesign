# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/9 10:47
@Contact : nzh199266@163.com
@Desc    : 
"""
import copy


class Product(object):
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Product Object, parent: {self.parent.__class__}>"


class Component(object):
    """
    利用python自带的原型接口，通过copy.copy或者copy.deepcopy进行复制。
    任何对象想实现原型模式只需重写__copy__方法和__deepcopy__方法即可。
    """

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __repr__(self):
        return f"<Component Ojbect, some_int: {self.some_int}, some_list_of_objects: {self.some_list_of_objects}, " \
               f"some_circular_ref: {self.some_circular_ref}>"

    def __copy__(self):
        # 复制引用对象
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # 克隆对象本身
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)  # 复制对象的属性

        return new

    def __deepcopy__(self, memodict={}):
        # 保留在当前复制过程中已复制的对象的 "备忘录" （memo） 字典
        # 以及允许用户定义的类重载复制操作或复制的组件集合
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects)
        some_circular_ref = copy.deepcopy(self.some_circular_ref)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memodict)

        return new
