# -*- coding:utf-8 -*-
'''
Created on 2015/3/14
@author: Jimmy Liu
'''
import unittest
import tushare.stock.billboard as fd


class Test(unittest.TestCase):

    def set_data(self):
        self.date = '2022-06-12'
        self.days = 5

    def test_top_list(self):
        pass
        # 接口有两个问题，1）节假日判断问题，2）请求超时问题
        self.set_data()
        print(fd.top_list(date=self.date))

    def test_cap_tops(self):
        self.set_data()
        print(fd.cap_tops(self.days))

    def test_broker_tops(self):
        self.set_data()
        print(fd.broker_tops(self.days))

    def test_inst_tops(self):
        self.set_data()
        print(fd.inst_tops(self.days))

    def test_inst_detail(self):
        print(fd.inst_detail())


if __name__ == "__main__":
    unittest.main()
