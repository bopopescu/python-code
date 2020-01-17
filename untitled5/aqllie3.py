#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-11 8:55
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : aqllie3.py

import sqlite3
conn = sqlite3.connect('test.db')
def sql_colose():
    conn.commit()
    conn.close()
def sql_lite():
    return conn.cursor()
# 建表操作
def new_table():
    cursor = sql_lite()
    cursor.execute('create table user (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(20))')
    cursor.close()
# 删表操作
def del_table():
    cursor = sql_lite()
    cursor.execute('DROP TABLE user;')
    cursor.close()

# 添加操作
def add_td(value):
    cursor = sql_lite()
    cursor.execute('insert into user (name) values ("'+value+'")')
    print(cursor.rowcount)
    cursor.close()

# 查询操作
def get_table():
    cursor = sql_lite()
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print(values)
    cursor.close()

# 删除操作
def del_td(id):
    cursor = sql_lite()
    cursor.execute('DELETE FROM user WHERE name like "%'+str(id)+'";')
    cursor.close()

#更新操作
def up_td(sql_value):
    cursor = sql_lite()
    cursor.execute(sql_value)
    cursor.close()


# add_td("meinv")
# del_td("xiaozhuang")
# new_table()
get_table()
up_td('UPDATE user SET name = "jin" WHERE id = 3;')
get_table()
# del_table()
sql_colose()