# -*- coding:utf-8 -*-
'''
Created on 2017/9/24
@author: Jimmy Liu
'''
import unittest
import tushare.stock.trading as fd


class Test(unittest.TestCase):

    def set_data(self):
        self.code = '600848'
        self.start = ''
        self.end = ''

    def test_bar_data(self):
        self.set_data()
        self.cons = fd.get_apis()
        if self.cons is not None:
            print(fd.bar(code=self.code, conn=self.cons))
            fd.close_apis(self.cons)
            self.cons = None


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
