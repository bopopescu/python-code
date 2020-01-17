#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-19 10:03
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
from ceapi import getapi
arr=['http://127.0.0.1:8888/api',"http://111.231.206.138:5000/api"]
data1={
    'host':6

}
data2={
'page':50
}
data=[data1,data2]
for i in range(len(arr)):
    getapi.getdata(arr[i],data[i])
print("执行完成")