#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-04 8:46
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
# 电子看板批量任务工具
import requests as go
import json,time
from tqdm import tqdm
# timeStamp = 1578102855864
# timeStamp = 1578102855864
# dateArray = datetime.datetime.fromtimestamp(timeStamp)
# otherStyleTime = dateArray.strftime("%Y--%m--%d %H:%M:%S")
# print(otherStyleTime)   # 2013--10--10 23:40:00
# 任务配置
# 用户
arr=['010','011','012','013','014','015','052','070','10','1006','1006s','1006t','1007','1007b','101','102','102ledl','102ledt','102t','108611','120','121','122','123','124','125','126','127','128','129','501','502','503','504','ja01','pub-1','shitang']
# 密码
# arr=['501','502','503']
pas="123456"
# 标题
title="二十四节气之小寒"
# 标题顺序
id=16
# 标题id
userTempId=[]
s = go.session()
def getcook(user,pas):
    millis = int(round(time.time() * 1000))
    # print(millis)
    url="http://192.168.0.100:8088/dzkb0/login_login"
    data={
    'loginname': user,
    'password': pas,
    'quickLogin': 'no',
    'tm': millis

    }
    r = s.post(url,data=data)
    c = go.cookies.RequestsCookieJar()
    s.cookies.update(c)
    return s.cookies.get_dict()
    # url ="http://192.168.0.100:8088/dzkb0/main/index"

def settitle(user,pas,title,id):
    cokk = getcook(user,pas)
    url="http://192.168.0.100:8088/dzkb0/home/addUserTemplet"
    data={

    'templetId': 7,
    'title': title,
    'sort': id

    }

    tr = s.post(url,cookies=cokk,data=data,verify=False)
    # return tr.text
def deltitle(user, pas,shu):
    url="http://192.168.0.100:8088/dzkb0/home/deleteUserTemplet"
    cokk = getcook(user, pas)

    data = {

        'userTempId': shu

    }
    tr = s.post(url, cookies=cokk, data=data, verify=False)
    # return tr.text
def gettitleid(user,pas):
    url = 'http://192.168.0.100:8088/dzkb0/home/userTempletList'
    cokk = getcook(user,pas)
    tr = s.post(url, cookies=cokk, verify=False)
    return json.loads(tr.text)["userTempletList"]
def getimgid(user,pas):
    url = 'http://192.168.0.100:8088/dzkb0/home/productImg'
    cokk = getcook(user,pas)
    data={
        'imgName':'',
        'type': 0
    }
    tr = s.post(url, cookies=cokk,data=data, verify=False)
    return json.loads(tr.text)["productImg"][0]['productImgId']



def setimg(user,pas,id,imgid):
    url = 'http://192.168.0.100:8088/dzkb0/home/addUserTempletInfo'
    cokk = getcook(user,pas)

    data = {
        'tempUrl': 'home_image1',
        'userTempId': id,
        'productImgId': imgid

    }
    tr = s.post(url, cookies=cokk, data=data, verify=False)
    # return tr.text

# # id
# imgidarr=[]
# for i in arr:
#     print(settitle(i,pas,title,id))
    # print(setimg(i,pas))
# print(deltitle("admin", "123456",2088))
def addwoke():
    for i in tqdm(arr):
        settitle(i,pas,title,id)
        # print("建立标签")
        ar = gettitleid(i, pas)
        for t in ar:
            if t['title']==title:
                userTempId.append(t["userTempId"])
                # print("获取标签id成功")
        imgid = getimgid(i, pas)
        # print("获取imgid成功")
        for it in userTempId:
            setimg(i,pas,it,imgid)
            # print("关联图片成功")
def dells(user, pas,id):
    url = 'http://192.168.0.100:8088/dzkb0/home/deleteUserTemplet'
    cokk = getcook(user, pas)

    data = {
        'userTempId': id

    }
    tr = s.post(url, cookies=cokk, data=data, verify=False)
    # return tr.text

def dellist():
    for i in tqdm(arr):
        ar = gettitleid(i, pas)
        for t in ar:
            if t['title'] == title:
                userTempId.append(t["userTempId"])
                # print("获取标签id成功")
        for it in userTempId:
            dells(i, pas,it)
            # print("删除任务")

    pass
if __name__ =="__main__":
    # 建立任务
    # print("开始任务:")
    # addwoke()
    # 删除任务
    print("开始删除任务：")
    dellist()
    # print(imgid)