#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-17 15:47
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : pys.py
# from imgrt import *
import json
from bs4 import BeautifulSoup
import requests as go
head={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '58',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'testcookie=yes;UM_distinctid=16f12ab2b6e11f-0a67308ebd12b2-32365f08-1fa400-16f12ab2b703ef; CNZZDATA708776=cnzz_eid%3D109585309-1576563001-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1576568403; CNZZDATA1261650895=1620036660-1576561946-https%253A%252F%252Fwww.baidu.com%252F%7C1576567347;',
    'Host': 'www.cxhr.com',
    'Origin': 'https://www.cxhr.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

def looksin():
    s = go.session()
    j =open("cook.txt","r")

    # print(type(cookies1))
    urlct = "https://www.cxhr.com/company/admin/search/searchResume.jsp?keyword=&job_Typevalue=&job_Industryvalue=&job_Areavalue1=&job_Areavalue=&job_Areavalue2=&job_Educationvalue=&wyear=&wmoney=&gender=&wtype=&updateneartime=1&curpage=1"
    rss = s.get(urlct,cookies=dict(j.read()),verify=False)
    rss.encoding = 'utf-8'
    # spp =BeautifulSoup(str(rss.text), 'html.parser', from_encoding='utf-8')
    print(rss.text)

def imgss():
    urlc = 'https://www.cxhr.com/verifyCodeServlet1'
    print(urlc)
    pic = go.get(urlc, timeout=15)
    string = '2.jpg'
    import time

    with open(string, 'wb') as f:
        f.write(pic.content)
        f.close()
# tt=input(">>")
def getcook():
    imgss()
    s = go.session()
    url='https://www.cxhr.com/company/companylogin!clogin.action'

    da={
    'companyaccount': 'xinhaibi',
    'password': 'Xinhai0574',
    # 'veryCode1': imgma('2.jpg')
    'veryCode1': input(">>")

    }
    rs = s.post(url,data=da)
    c = go.cookies.RequestsCookieJar()
    c.set('testcookie', 'yes')
    c.set('UM_distinctid', '16f12ab2b6e11f-0a67308ebd12b2-32365f08-1fa400-16f12ab2b703ef')
    c.set('CNZZDATA708776', 'cnzz_eid%3D109585309-1576563001-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1576568403')
    c.set('CNZZDATA1261650895', '1620036660-1576561946-https%253A%252F%252Fwww.baidu.com%252F%7C1576567347')
    s.cookies.update(c)
    # print(rs.text)
    return s.cookies.get_dict()
cook = getcook()
def gethtml(shu):

    urlct = "https://www.cxhr.com/company/admin/search/searchResume.jsp?keyword=&job_Typevalue=&job_Industryvalue=&job_Areavalue1=&job_Areavalue=&job_Areavalue2=&job_Educationvalue=&wyear=&wmoney=&gender=&wtype=&updateneartime=1&curpage="+str(shu)
    s = go.session()

    # print(cookies)
    s = go.session()
    rs1 = s.get(urlct,cookies=cook,verify=False)
    # print(rss.headers)
    # print(rss.text)
    rs1.encoding = 'utf-8'
    # return rs1.text
    return BeautifulSoup(str(rs1.text), 'html.parser', from_encoding='utf-8')
# shu = str(getdata(1).select("table")[4].tr.findAll('td')[1].text)[4:7]
# shu=1
def getimghtml(shu):

    urlct = "https://www.cxhr.com/company/admin/resume/resume.jsp?resumeids="+str(shu)


    # print(cookies)
    s = go.session()
    rs1 = s.get(urlct,cookies=cook,verify=False)
    # print(rss.headers)
    # print(rss.text)
    rs1.encoding = 'utf-8'
    # return rs1.text
    return BeautifulSoup(str(rs1.text), 'html.parser', from_encoding='utf-8')
def getimg():
        print(getimghtml('1239540').findAll("div", {"class":"content border"}))

def getdata(shu):
    arr=[]
    arr1=[]
    for i in range(int(shu)):
        if i>0:
            for t in gethtml(i).select('table')[3].select('tr'):

                for y in t.select('td'):

                    arr.append(str(y.text).replace("\xa0", " "))

    n=0
    print(int(len(arr)/12))
    for i in range(int(len(arr)/12)):
        arr1.append(arr[n*12:n*12+12])
        n=n+1
    return arr1

    # u = open("s.txt","w")
    # u.write(str(arr1).replace("\u2714", " "))

# u = open("cook.txt","w")
# u.write(str(getcook()))
#
# looksin()

getimg()