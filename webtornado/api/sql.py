#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-13 10:41
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : sql.py
# 功能：操作数据库
import pymysql
# 连接数据库
sqlr = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='root',
                       database='ceshi',
                       charset='utf8')
def mysql():
    if sqlr:
         print('mysql连接成功')
         return sqlr.cursor()
    else:
        print('mysql连接失败')

# 查询数据
# table为表名
# cur.fetchall()返回所有内容
def RedSql(table):
    cur =mysql()
    # cur.execute("ALTER TABLE sheet1 ADD COLUMN name VARCHAR(100) DEFAULT NULL COMMENT '姓名'")
    # sqlr.commit()
    # cur.close()
    # sqlr.close()
    cur.execute('select * from '+str(table))
    return cur.fetchall()
# # 删除数据
# id为目标id
# table为目标表名
def DelSql(table,id):
    cur =mysql()
    cur.execute('DELETE FROM '+str(table)+' WHERE id='+str(id))
    if sqlr.commit():
        return {'msg':'ok'}
    else:
        return {'msg':'no'}
    cur.close()
    sqlr.close()
# 修改数据
# data为sql语句 update my_school set name = %s where id = %s'
def UpSql(data):
    cur =mysql()
    cur.execute(data)
    if sqlr.commit():
        return {'msg':'ok'}
    else:
        return {'msg':'no'}
    cur.close()
    sqlr.close()
# 添加数据
# data为sql语句 insert into table(id, name) values(%s, %s)
def AddSql(data):
    cur =mysql()
    cur.execute(data)
    if sqlr.commit():
        return {'msg':'ok'}
    else:
        return {'msg':'no'}
    cur.close()
    sqlr.close()

# RedSql(1)