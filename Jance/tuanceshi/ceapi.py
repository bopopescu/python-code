#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-19 15:25
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : ceapi.py
import requests
class ceapi:

    def printres(self,res,url):

        s='\n\n-----------HTTP response begin ----------------\n\nurl:'+str(url)
        s+="\n\n响应值："+str(res.status_code)+"\n\n"
        for k,v in res.headers.items():
            s+=f'{k}:{v}'+"\n"

        s+='\n'+str(res.content.decode('utf8'))+"\n\n-----------HTTP response end----------------\n\n"
        f = open("log.txt","a+")
        f.write(s)

    def getdata(self,url,data):

        text = requests.get(url,data=data)
        self.printres(text,url)
        return text
    def postdata(self,url,data):

        text = requests.post(url,data=data)
        self.printres(text)
        return text

getapi = ceapi()