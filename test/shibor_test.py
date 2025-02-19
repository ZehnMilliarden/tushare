# -*- coding:utf-8 -*-

import unittest
import tushare.stock.shibor as fd


class Test(unittest.TestCase):

    def set_data(self):
        self.year = 2021
#         self.year = None

    def test_shibor_data(self):
        self.set_data()
        print(fd.shibor_data(self.year))

    def test_shibor_quote_data(self):
        self.set_data()
        print(fd.shibor_quote_data(self.year))

    def test_shibor_ma_data(self):
        self.set_data()
        print(fd.shibor_ma_data(self.year))

    def test_lpr_data(self):
        self.set_data()
        print(fd.lpr_data(self.year))

    def test_lpr_ma_data(self):
        self.set_data()
        print(fd.lpr_ma_data(self.year))


if __name__ == '__main__':
    unittest.main()
