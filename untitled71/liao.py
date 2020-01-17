#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-12 9:44
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : liao.py
from time import sleep
import requests

# while True:
#     s = input("请主人输入话题：")
#     resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': s})
#     resp.encoding = 'utf8'
#     resp = resp.json()
#     sleep(1)
#     print('菲菲：', resp['content'])
# # 3
# # 网上还有一个据说智商比较高的小i机器人，用爬虫的功能来实现一下：

import urllib.request
import re,time
timer=str(str(time.strftime("%Y.%m.%d %H.%M.%S", time.localtime())))
x = "慈溪天气"
x = urllib.parse.quote(x)
link = urllib.request.urlopen(
    "http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
html_doc = link.read().decode()
reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
print("早上好,我是小i：时间"+timer +","+ reply_list[-1])