#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-20 15:01
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : url.py
import tornado.web
from api.Api_Get import Api_Get
from api.GetIndex import GetIndex
application = tornado.web.Application([
            ("/", GetIndex),
            ("/user_api", Api_Get),
        ])