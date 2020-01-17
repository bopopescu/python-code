#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-18 15:48
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : Api_Get.py
import tornado.web
from pys import getdata
import json
def set_default_header(self):
    # 后面的*可以换成ip地址，意为允许访问的地址
    self.set_header('Access-Control-Allow-Origin', '*')
    self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
    self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')
def GetJson(self,data):
    set_default_header(self)
    self.set_header('Content-Type', 'application/json; charset=UTF-8')
    return self.write(json.dumps(data,ensure_ascii=False))
class Api_Get(tornado.web.RequestHandler):

    def get(self):
        get = self.get_argument('page')
        # g = open("s.txt", "r")

        data={
            'msg':'ok',
            'data':getdata(int(get)),
            'code':1


        }
        GetJson(self,data)