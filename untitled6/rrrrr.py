#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-06 9:39
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : redis.py
import redis

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379,db=1)
red = redis.Redis(connection_pool=pool)
print(red.mget("name","key2"))


