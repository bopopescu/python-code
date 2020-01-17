#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-15 8:26
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
import pymysql
from tqdm import tqdm
def getmysql():
    # 建库和建表
    con = pymysql.connect(host='10.168.5.223', user='wapjin',passwd='wapjin', charset='utf8')
    return con.cursor()
    # 开始建库
    # cur.execute("create database awesome character set utf8;")
    # 使用库

# 建表
def new_table(table):
    cur=getmysql()
    cur.execute("use wapjin")

    cur.execute(table)

f= open("jin.sql","r")
arr = f.read().replace("\n","").split(';')
# exit()
# table='''CREATE TABLE `user` (
# `id` int(2) NOT NULL AUTO_INCREMENT,
# `name` varchar(20) NULL,
# PRIMARY KEY (`id`)
# );'''
for i in tqdm(arr):
    if len(i)>0:
        try:
            new_table(i)
            print("处理成功")
        except BaseException:
            print("禁止重复操作！")
