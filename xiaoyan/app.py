#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Function    : 效验数据库数据准确性
# @Time    : 2019-10-16 16:40
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
# @Project : 数字工厂，十二分厂仓库系统
import pymssql
import pymysql
def mysql():
    sqlr = pymysql.connect(host='192.168.0.100', user='xh_barcode', password='xinhai0574', database='xh_barcode', charset='utf8')
    print('mysql连接成功')
    return sqlr.cursor()
import time

def ssql():
    conn = pymssql.connect(server='192.168.0.7', user='xh_data_reader', password='Reader39A8db',database='UFDATA_001_2011', charset='utf8')
    print('sql_server连接成功')
    return conn.cursor()



def data2(vaule):
    cur = mysql()
    cur.execute(vaule)
    return cur.fetchall()  # fetchall() 获取所有记录
def mysqlTime():
    sqlr = pymysql.connect(host='localhost', user='wapjin', password='jinjin', database='820012', charset='utf8')
    print('mysqltime连接成功')
    return sqlr.cursor()

def data1(vaule):
    r1 = ssql()
    r1.execute(vaule)
    return r1.fetchall()




def data3(vaule):
    cur = mysqlTime()
    cur.execute(vaule)
    return cur.fetchall()
    # fetchall() 获取所有记录

def data4(vaule):
    cur = mysqlTime()
    cur.execute(vaule)

    # fetchall() 获取所有记录
def sums(t1,t2,ku,KU2,title):
    st3 = 'select time from newtime order by id desc limit 0,1'
    arr3 = data3(st3)
    rtime = int(arr3[0][0][8:])
    rtimecha = int(str(str(time.strftime("%Y-%m-%d", time.localtime())))[8:])-int(arr3[0][0][8:])
    timeNew = str(str(time.strftime("%Y-%m-%d", time.localtime())))
    # timeNew = "2019-10-17"
    if rtime>0:
        for rg in range(rtimecha):
            st1 ="SELECT rd.cCode,rd.cRdCode,rd.cDefine1,rd.cWhCode,rd.dDate,rd.dnmaketime,rd.cDefine3,rds.cInvCode,rds.iQuantity,rds.iUnitCost,rds.iPrice,inv.cInvName,inv.cComUnitCode,cu.cComUnitName  FROM "+t1+" rd,"+t2+" rds,Inventory inv,ComputationUnit cu WHERE rd.ID = rds.ID AND rds.cInvCode = inv.cInvCode AND inv.cComUnitCode = cu.cComUnitCode AND rd.cRdCode= '"+ku+"' AND Convert(varchar,rd.dnmaketime,120) LIKE '"+timeNew[:8]+str(rtime+rg)+"%'"
            arr1 = data1(st1)
            st2='select * from xh_erp_product_in where typeID = "'+KU2+'" and add_time like "%'+timeNew[:8]+str(rtime+rg)+'%"'
            arr = data2(st2)

            L1 ='erp：共' + str(len(arr1)) + '条'
            L2 = '本地：共' + str(len(arr)) + '条'
            strl =""
            if len(arr1)!=len(arr):
                if len(arr) < len(arr1):
                    sum = len(arr1) - len(arr)
                    sum = "本地数据缺失:" + str(sum) + "条"
                    # for at in arr1:
                    #     print(at)
                    if 0 == len(arr):
                        for at in arr1:
                            strl += str(at)
                    for i in range(len(arr)):
                        for t in range(len(arr1)):
                            if arr[i][32] != arr1[t][0]:
                                strl += str(arr1[t])
                    strl =str(L1 + "|\n" + L2 + "|\nerp多|" + sum + "\n") + str(strl)
                    st4 = 'INSERT INTO xiaoyan(time,title,data) VALUES ("' + timeNew + '","' + title + '","' + str(
                        strl) + '")'
                    data4(st4)


                else:
                    sum = len(arr) - len(arr1)
                    sum = "erp本地数据缺失:" + str(sum) + "条"
                    if 0 == len(arr1):
                        for at in arr:
                            strl += str(at)
                    for i in range(len(arr)):
                        for t in range(len(arr1)):
                            if arr[i][32] != arr1[t][0]:
                                strl +=str(arr[i])

                    strl =str(L1 + "\n|" + L2 + "|\n本地多|" + sum + "\n") + str(strl)
                    st4 = 'INSERT INTO xiaoyan(time,title,data) VALUES ("' + timeNew + '","' + title + '","' + str(
                        strl) + '")'
                    data4(st4)
    else:
         print('今天已经执行过了')


def new1():
    timeNew = str(str(time.strftime("%Y-%m-%d", time.localtime())))
    st3 = 'INSERT INTO newtime(time) VALUES ("' + timeNew + '")'
    data3(st3)



# def chu(t1,t2):
#     st1 = "SELECT rd.cCode,rd.cRdCode,rd.cDefine1,rd.cWhCode,rds.cInvCode,rds.iQuantity,inv.cInvName,cu.cComUnitName  FROM " + t1 + " rd," + t2 + " rds,Inventory inv,ComputationUnit cu where rd.ID = rds.ID AND rds.cInvCode = inv.cInvCode AND inv.cComUnitCode = cu.cComUnitCode AND Convert(varchar,rd.dnmaketime,120) LIKE '"+str(str(time.strftime("%Y-%m-%d", time.localtime())))+"%'"
#
#     st2 = 'select erp_id,typeid,Form_No,Store_location,Model_ID,Quantity_in,Good_Name,Unit from xh_erp_product_in where add_time like "'+str(str(time.strftime("%Y-%m-%d", time.localtime())))+'%"'
#     arr = data2(st2)
#     arr1 = data1(st1)
#     print(arr)
#     print(arr1)
# chu("RdRecord01","rdrecords01")

if __name__ =="__main__":

    print("采购入库")
    sums("RdRecord01","rdrecords01","1101","W","采购入库")
    # print('普通原材料')
    # sums("rdrecord11","rdrecords11","1201",'普通原材料')
    print('委外半成品入库')
    sums("rdRecord10","rdrecords10","2106","WZ",'委外半成品入库')
    # print('委外半成品出库')
    # sums("rdrecord11","rdrecords11","2212",'委外半成品出库')
    print("半成品入库")
    sums("rdrecord10","rdrecords10","2101","Z","半成品入库")
    # print("半成品出库")
    # sums("rdrecord11","rdrecords11","2201","半成品出库")
    new1()
    # 记录时间
