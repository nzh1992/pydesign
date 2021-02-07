# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/7 17:06
@Contact : ziheng.ni@envision-energy.com
@Desc    : 工厂方法模式——客户端代码
    对于用户而言，仅需要知道要哪些构造器(*Creator)即可，其余细节皆被隐藏在构造器类中
"""
from create_mode.factory_method.creator import Creator, TruckCreator, ShipCreator


def user_code(creator: Creator) -> None:
    print("client:")
    print(f"{creator.some_operation()}")


if __name__ == '__main__':
    # 1. 创建 卡车类
    truck_creator = TruckCreator()
    user_code(truck_creator)

    # 2. 创建 船类
    ship_creator = ShipCreator()
    user_code(ship_creator)