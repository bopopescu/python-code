#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-18 15:46
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : web.py
import tornado.ioloop
import tornado.web
from Api_Get import Api_Get
if __name__ == "__main__":
    por=8888
    application = tornado.web.Application([
        ("/", Api_Get),
    ])
    print("服务开启    地址：http://127.0.0.1:"+str(por))
    application.listen(por)
    tornado.ioloop.IOLoop.current().start()

































































































