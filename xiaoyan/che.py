#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-25 9:24
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : che.py
import pymysql
def mysql():
    sqlr = pymysql.connect(host='127.0.0.1', user='root', password='root', database='820012', charset='utf8')
    # print('mysql连接成功')
    return sqlr.cursor()
def data(vaule):
    cur = mysql()
    cur.execute(vaule)
    return cur.fetchall()  # fetchall() 获取所有记录
sql1 = "select name from che1"
arr1 = data(sql1)



for i in range(len(arr1)):
    sql = "select name from che where name = '" + str(arr1[i][0]) + "'"
    arr = data(sql)

    print(arr)