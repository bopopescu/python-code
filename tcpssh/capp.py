#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-19 16:18
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : capp.py
from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(('192.168.0.100', 5000))
while 1:
    sendData = input('send:')

    s.send(sendData.encode('gbk'))

    ret = s.recv(1024)

    print(ret.decode('gbk'))

s.close()





