#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-23 11:07
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : getapi.py
import json
def geturl(datas,name):
    arr = []
    for i in datas:
        arr.append(str(i)[:int(i.index("="))])
        arr.append(str(i)[int(i.index("=")) + 1:])

    print(arr)
    getdata = {}
    for i in range(0, len(arr), 2):
        getdata[arr[i]] = arr[i + 1]

    return getdata[name]
def index():
    with open('./188.html', 'r') as f:
        r =str(f.read())
    # print(rdg)
    return r
def api(datas):
# # datas = str(environ['QUERY_STRING'])
    if datas=="":
        print(datas)
        data = {

            'code': 1,
            'msg': "数据错误",
            'data': 0,
            'data2': 0

        }
    else:
        r= geturl(datas,'u')
        r1 = geturl(datas, 'y')
        data = {

            'code': 1,
            'msg': "公司",
            'data':r1,
            'data2': r

        }
    return json.dumps(data,ensure_ascii=False)


