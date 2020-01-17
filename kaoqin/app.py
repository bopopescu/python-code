#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-12 11:22
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : kaoqin.py
import pymssql
import pymysql
from tqdm import tqdm
import time
tr = str(time.strftime("%Y-%m-%d", time.localtime()))
# Connect mysql
def mysql():
    sqlr = pymysql.connect(host='127.0.0.1', user='root', password='root', database='kaoqin', charset='utf8')
    print('mysql  ok')
    return sqlr.cursor()

# Connect sql server
def ssql():
    conn = pymssql.connect(server='192.168.0.12', user='xh_dingding_input', password='Write86B2db',database='kaoqin_cs', charset='utf8')
    print('sql_server ok')
    return conn.cursor()
# public function
def data1(vaule):
    r1 = ssql()
    r1.execute(vaule)
    return r1.fetchall()

# public function :Transfer table data
def addlist(table,td,val):

    # id,id_person,check_time,check_date,type,is_count,dj_id,check_tag
    sql="INSERT INTO "+str(table)+"("+str(td)+") VALUES("+str(val)+")"
    r1 = mysql()
    for i in tqdm(data1("select * from "+str(table))):

        r1.execute(sql,i)
# public function :Update table data
def uplist(table,td,val):
    sqle = "select id from "+str(table)+" order by id desc limit 1"
    r1 = mysql()
    r1.execute(sqle)
    rr = r1.fetchall()
    arr= data1("select * from " + str(table) + " where id > "+str(rr[0][0]))
    time.sleep(1)
    sql="INSERT INTO "+str(table)+"("+str(td)+") VALUES("+str(val)+")"
    for i in tqdm(range(len(arr))):
            r1.execute(sql,arr[i])
 # Transfer checkrecord table data
def checkrecord():
    # 13: 27 < 00:00, 4333.79
    # it / s]
    table="checkrecord"
    td="id,id_person,check_time,check_date,type,is_count,dj_id,check_tag"
    val="%s,%s,%s,%s,%s,%s,%s,%s"
    addlist(table,td,val)
    print("checkrecord ok")
 # Transfer and Update checkrecord table data
def upcheckrecord():
    table="checkrecord"
    td="id,id_person,check_time,check_date,type,is_count,dj_id,check_tag"
    val="%s,%s,%s,%s,%s,%s,%s,%s"
    uplist(table,td,val)
    print("checkrecord ok")
 # Transfer depart table data
def depart():
    table="depart"
    td="d_id,d_idpre,d_level,d_departname,note,d_level1name,d_level2name"
    val="%s,%s,%s,%s,%s,%s,%s"
    addlist(table,td,val)
    print("pbcatedt ok")


# Transfer person table data
def person():
    table = "person"
    td = "id_person,empid,empname,d_id,dpt2id,dpt2name,user_finger,if_kq,duty_id,duty_name,note,usedate,ifovertime,if_finger"
    val = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
    addlist(table, td, val)
    print("person ok")



if __name__ =="__main__":
    upcheckrecord()
