#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-15 10:27
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py

import execjs
def get_des_psswd():
    jsstr = get_js()
    ctx = execjs.compile(jsstr) #加载JS文件
    return (ctx.call('a', "66666"))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数



def get_js():
    f = open("./as.js", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr
print(get_des_psswd())