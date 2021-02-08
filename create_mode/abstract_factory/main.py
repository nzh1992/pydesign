# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/8 13:08
@Contact : ziheng.ni@envision-energy.com
@Desc    : 
"""
from create_mode.abstract_factory.factory import AbstractFactory, ArtFactory, ModernFactory, VictorianFactory


def user_code(factory: AbstractFactory) -> None:
    chair = factory.create_chair()
    print(chair)

    table = factory.create_table()
    print(table)


if __name__ == '__main__':
    # 指定工厂类型，由工厂类型决定产品类型
    user_code(ArtFactory())

    # 如果想生产现代风格的椅子，只需要切换工厂即可
    user_code(ModernFactory())