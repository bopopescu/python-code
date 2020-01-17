#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 11:11
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : sql.py
import pymysql
def mysql():
    sqlr = pymysql.connect(host='127.0.0.1', user='root', password='root', database='820012', charset='utf8')
    print('mysql连接成功')
    return sqlr.cursor()

def sql_look(data):
    cur =mysql()
    cur.execute(data)
    return cur.fetchall()
def sql_add(data):
    cur =mysql()
    cur.execute(data)
    return cur.fetchall()
def sql_del(data):
    cur =mysql()
    cur.execute(data)
    return cur.fetchall()
def sql_up(data):
    cur =mysql()
    cur.execute(data)
    return cur.fetchall()