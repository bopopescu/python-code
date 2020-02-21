#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-28 8:39
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : shu.py

import pymssql
from tqdm import tqdm, trange
import time
def ssql():
    conn = pymssql.connect(server='192.168.0.7', user='xh_data_reader', password='Reader39A8db',database='UFDATA_002_2011', charset='utf8')
    print('sql_server ok')
    return conn.cursor()
def data1(vaule):
    r1 = ssql()
    r1.execute(vaule)
    return r1.fetchall()
def cha(test):
    sql="select * from hr_hi_person where cPsn_Name like '%"+str(test)+"'"
    return data1(sql)

r = cha(input("输入名字："))
print(r)
