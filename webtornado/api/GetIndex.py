#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-13 10:23
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : GetIndex.py
# 功能：处理html界面数据，可返回html静态页面
import tornado.web
class GetIndex(tornado.web.RequestHandler):
    def get(self):
        return self.render("../index/188.html", title="在线ssh", body="meiyoule")

