#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-05 11:12
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : mysql.py
import pymysql,json
def mysql():
    sqlr = pymysql.connect(host='127.0.0.1', user='root', password='root', database='820012', charset='utf8')
    print('mysql连接成功')
    return sqlr.cursor()
def data(vaule):
    cur = mysql()
    cur.execute(vaule)
    return cur.fetchall()  # fetchall() 获取所有记录
def getjson(test):
    return json.dumps(test, ensure_ascii=False)