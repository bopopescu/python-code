#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 10:51
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : api.py

from bottle import *
import json
from sql import *
@hook('after_request')
def after_request():
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

def get_json(data):
    return json.dumps(data, ensure_ascii=False)
@route('/')
def index():
    return template("./index.html")


@route('/get')
def index_list1():
    times = str(str(time.strftime("%Y%m%d%H%M", time.localtime())))
    code = request.GET.get('code')
    time_get=request.GET.get('time')
    print(times)
    print(time_get)
    # if int(time_get)==int(times):
    if code=="1":
        arr = sql_look("select * from jin")
        data = {
            'code': 1
            , 'msg': 'ok'
            , 'data': arr
        }

    elif code=="2":
        arr = sql_add("insert into sheet1(name,pass) values('jin','jinjin')")
        data = {
            'code': 1
            , 'msg': 'ok'
            , 'data': arr
        }
    elif code == "3":
        arr = sql_del("delete from sheet1 where id=1")
        data = {
            'code': 1
            , 'msg': 'ok'
            , 'data': arr
        }
    elif code == "3":
        arr = sql_up("update sheet1 set name = '123', pass = 'llll' where id=1")
        data = {
            'code': 1
            , 'msg': 'ok'
            , 'data': arr
        }
    else:
        data = {
            'code': 0
            , 'msg': '请求有误'
            , 'data': ""
        }
    # else:
    #     data = {
    #         'code': 0
    #         , 'msg': '请求有误'
    #         , 'data': ""
    #     }
    return get_json(data)
@route('/post', method='POST')
def index_list():
    code = request.POST.get('code')
    if code=="1":
        arr = sql_look("select * from sheet1")
        data={
            'code':1
            ,'msg':'ok'
            ,'data':arr
        }
        return get_json(data)
    else:
        data = {
            'code': 0
            , 'msg': '请求有误'
            , 'data': ""
        }
        return get_json(data)

if __name__ == "__main__":
    run(host='127.0.0.1', port=8080, debug=True)
