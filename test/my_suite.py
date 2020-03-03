#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   my_suite.py
@Time    :   2020/03/03 13:59:49
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   test suite的尝试
'''
import unittest
from test_first_unitcases import TestStringMethods
from test_skip import TestSkipCases


def suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(TestStringMethods('test_upper'))   # 按单元测试类、测试函数名添加
    my_suite.addTest(TestSkipCases('test_foo1'))
    # 如要添加一批，则需要使用 discovery 功能
    return my_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
