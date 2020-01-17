#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-16 15:53
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py

import requests as q
import json,chardet
url="http://111.231.206.138:5000/1"
head={
"Content-Type": "text/html; charset=utf-8",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"


}
dat= q.get(url,headers=head)
# data.encoding="utf8"
dat.encoding = "utf-8"
print(dat.apparent_encoding)
obj = json.loads(dat.content.decode("utf-8"))
print(obj)

