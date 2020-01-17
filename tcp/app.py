#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-23 9:53
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from api.urs import *
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/json;charset=utf-8')])
    url = environ['PATH_INFO'][1:]

    if environ['QUERY_STRING']=="":
        datas=""
    else:
        datas = str(environ['QUERY_STRING']).split('&')
    return [(urldata(url, datas)).encode()]
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()