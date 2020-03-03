#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_skop.py
@Time    :   2020/03/03 13:47:07
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   unittest的skip属性
'''

import unittest


class TestSkipCases(unittest.TestCase):

    my_condition = 'abc123'

    def test_foo1(self):
        print('foo1')
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.skip('跳过测试 FOO 2')
    def test_foo2(self):
        print('foo 2')
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.skipIf(my_condition=='abc', '满足条件才跳过')
    # 带条件的跳过
    # @unittest.skipUnless(sys.platform.startswith("win"), "满足条件不跳过")
    def test_foo3(self):
        print('foo 3')
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.expectedFailure
    # 假设这个用例是失败的，如果真失败则回显为成功！
    def test_foo_must_failed(self):
        print('这个用例无论如何必定失败')
        self.assertEqual('foo'.upper(), 'FOO111')


if __name__ == "__main__":
    unittest.main()

