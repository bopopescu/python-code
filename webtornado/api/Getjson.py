#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-13 10:16
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : Getjson.py
# 功能：处理格式并返回json
import tornado.web
import json


def set_default_header(self):
    # 后面的*可以换成ip地址，意为允许访问的地址
    self.set_header('Access-Control-Allow-Origin', '*')
    self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
    self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')


def GetJson(self, data):
    set_default_header(self)
    self.set_header('Content-Type', 'application/json; charset=UTF-8')
    return self.write(json.dumps(data, ensure_ascii=False))


class Api_Get(tornado.web.RequestHandler):

    def get(self):


        data = {
            'msg': 'ok'

        }
        GetJson(self, data)

