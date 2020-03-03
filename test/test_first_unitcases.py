#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_first_unitcases.py
@Time    :   2020/03/03 13:33:51
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   第一个独立运行的unittest单元测试

'''
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_slit(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # 其他类型的检查：
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
