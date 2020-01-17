#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-13 9:34
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : Api_get.py
# 功能：获取数据返回接口数据
from api.Getjson import *
from api.sql import *
import time
class Api_Get(tornado.web.RequestHandler):

    def get(self):
        remote_ip = self.request.remote_ip
        host = self.get_arguments('host')
        sr = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))+str(123)+str(remote_ip)
        print(host)
        print(sr)
        if sr == host[0]:
            host = self.get_arguments('host')
            data = {
                'msg': 'err',
                'data': remote_ip,
                'code': 0

            }
            GetJson(self, data)
        else:

            GetJson(self, "错误")

    def post(self):
        code1 = "123456"
        code = self.get_arguments('code')
        # print(code[0])
        if code[0]==code1:
            user = self.get_arguments('user')
            pas = self.get_arguments('pass')
            arr=[]
            for i in RedSql("sheet1"):
                # print(i[3])
                # print(pas[0])
                if i[3]==user[0]:
                    if i[2]==pas[0]:
                        data = {
                            'msg': '登录成功',
                            'data': i,
                        }
                    else:
                        data = {
                            'msg': '密码错误！',
                            'data': user[0]

                        }
                    break
                else:
                    data = {
                        'msg': '没有此用户',
                        'data': user[0]

                    }

            GetJson(self, data)
        else:
            data = {
                'msg': '接口未授权',
                'data': 0,

            }
            GetJson(self, data)

