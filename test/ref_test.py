# -*- coding:utf-8 -*-
'''
Created on 2015/3/14
@author: Jimmy Liu
'''
import unittest
from tushare.stock import reference as fd


class Test(unittest.TestCase):

    def set_data(self):
        self.code = '600848'
        self.start = '2022-01-03'
        self.end = '2022-04-07'
        self.year = 2022
        self.quarter = 4
        self.top = 60
        self.show_content = True

    def test_profit_data(self):
        self.set_data()
        print(fd.profit_data(year=2021, top=60))

    def test_forecast_data(self):
        self.set_data()
        print(fd.forecast_data(year=2022, quarter=2))

    def test_xsg_data(self):
        print(fd.xsg_data())

    def test_fund_holdings(self):
        self.set_data()
        print(fd.fund_holdings(year=2022, quarter=1))

    def test_new_stocksa(self):
        print(fd.new_stocks())

    def test_sh_margin_details(self):
        self.set_data()
        print(fd.sh_margin_details(self.start, self.end, self.code))

    def test_sh_margins(self):
        self.set_data()
        print(fd.sh_margins(self.start, self.end))

    def test_sz_margins(self):
        self.set_data()
        print(fd.sz_margins(self.start, self.end))

    def test_sz_margin_details(self):
        self.set_data()
        print(fd.sz_margin_details(self.end))


if __name__ == "__main__":
    unittest.main()
