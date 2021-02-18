# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@Author  : ziheng.ni
@Time    : 2021/2/18 15:03
@Contact : ziheng.ni@envision-energy.com
@Desc    : 
"""
from structure_mode.adapter.raw_module import Target


class Adaptee(object):
    """适配后的方法"""
    def specific_request(self):
        return "Target special behavior"


class Adapter(Target, Adaptee):
    def request(self):
        """Target.request() -> Adaptee.specific_request()"""
        return self.specific_request()

