#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-15 12:45
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
import win32clipboard as wc
import win32con

def getCopyText():
    wc.OpenClipboard()
    copy_text = wc.GetClipboardData(win32con.CF_TEXT)
    wc.CloseClipboard()
    f = open("g.jpg","w+")
    f.write(copy_text.decode())

# test
import chardet
# print (chardet.detect(getCopyText()))  # 找到包含中文内容的字符串编码
print (getCopyText())  # 转码
