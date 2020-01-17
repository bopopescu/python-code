#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-12 16:02
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
import tornado.ioloop
from api.url import application
if __name__ == "__main__":
    por=8888
    print("服务开启    地址：http://127.0.0.1:"+str(por))
    application.listen(por)
    tornado.ioloop.IOLoop.current().start()
