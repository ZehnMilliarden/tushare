# -*- coding:utf-8 -*-

from ast import And
from genericpath import isfile
from importlib.resources import path
import os
# from sqlalchemy import create_engine
from pandas.io.pytables import HDFStore
import tushare as ts


def get_data_fullpath(file: str):
    strFullPath: str = os.path.join(os.getcwd(), file)
    strFullPathFolder: str = os.path.dirname(strFullPath)

    if os.path.exists(strFullPathFolder) == False:
        os.makedirs(strFullPathFolder)

    if os.path.exists(strFullPath):
        if os.path.isfile(strFullPath):
            os.remove(strFullPath)

    return strFullPath


def csv(stoke: str):
    df = ts.get_hist_data(code=stoke, ktype="5")
    strTempPath = 'data/day/{stoke_id}.csv'.format(stoke_id=stoke)
    df.to_csv(get_data_fullpath(strTempPath),
              columns=['open', 'high', 'low', 'close'])


def xls(stoke: str):
    df = ts.get_hist_data('stoke')
    # 直接保存
    strTempPath = 'data/day/{stoke_id}.xlsx'.format(stoke_id=stoke)
    strDataPath = get_data_fullpath(strTempPath)
    df.to_excel(strDataPath, startrow=0, startcol=0)


def hdf():
    df = ts.get_hist_data('000875')
#     df.to_hdf('c:/day/store.h5','table')

    store = HDFStore('./data/day/store.h5')
    store['000875'] = df
    store.close()


def json():
    df = ts.get_hist_data('000875')
    df.to_json('./data/day/000875.json', orient='records')

    # 或者直接使用
    print(df.to_json(orient='records'))


def appends():
    filename = './data/day/bigfile.csv'
    for code in ['000875', '600848', '000981']:
        df = ts.get_hist_data(code)
        if os.path.exists(filename):
            df.to_csv(filename, mode='a', header=None)
        else:
            df.to_csv(filename)


def db():
    pass

    df = ts.get_tick_data('600848', date='2014-12-22')
    engine = create_engine(
        'mysql://root:jimmy1@127.0.0.1/mystock?charset=utf8')
#     db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='jimmy1',db="mystock",charset="utf8")
#     df.to_sql('TICK_DATA',con=db,flavor='mysql')
#     db.close()
    df.to_sql('tick_data', engine, if_exists='append')


def nosql():
    pass

    import pymongo
    import json
    conn = pymongo.Connection('127.0.0.1', port=27017)
    df = ts.get_tick_data('600848', date='2014-12-22')
    print(df.to_json(orient='records'))

    conn.db.tickdata.insert(json.loads(df.to_json(orient='records')))

#     print conn.db.tickdata.find()


if __name__ == '__main__':
    csv('600848')
    csv('601696')
