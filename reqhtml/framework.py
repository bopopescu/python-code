#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-21 10:57
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : framework.py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return 'Hello World!'