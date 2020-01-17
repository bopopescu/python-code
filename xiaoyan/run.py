#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-17 8:37
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : run.py



import requests
import json
url = "http://127.0.0.1/miao/api.php"  # 接口地址

# 消息头数据

payload = {
'code': '1',
'data': '{"id":2,"title":"鼠标"}'

           }
# verify = False 忽略SSH 验证
while 1:
    r = requests.post(url, data=payload)
    print(r.text)

