#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-23 11:06
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : urls.py
from api.getapi import *
def urldata(ur,datas):

    if ur == "api":
        return api(datas)
    if ur == "":
        return index()