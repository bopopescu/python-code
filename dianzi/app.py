#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-14 10:50
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py
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


def getcook(user,pas):
    s = go.session()
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
    s = go.session()
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
    s = go.session()
    url="http://192.168.0.100:8088/dzkb0/home/deleteUserTemplet"
    cokk = getcook(user, pas)

    data = {

        'userTempId': shu

    }
    tr = s.post(url, cookies=cokk, data=data, verify=False)
    # return tr.text
def gettitleid(user,pas):
    s = go.session()
    url = 'http://192.168.0.100:8088/dzkb0/home/userTempletList'
    cokk = getcook(user,pas)
    tr = s.post(url, cookies=cokk, verify=False)
    return json.loads(tr.text)["userTempletList"]
def getimgid(user,pas,imgid):
    s = go.session()
    url = 'http://192.168.0.100:8088/dzkb0/home/productImg'
    cokk = getcook(user,pas)
    data={
        'imgName':'',
        'type': 0
    }
    tr = s.post(url, cookies=cokk,data=data, verify=False)
    return json.loads(tr.text)["productImg"][int(imgid)]['productImgId']



def setimg(user,pas,id,imgid):
    s = go.session()
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
def addwoke(arr,pas,title,id,getid):
    userTempId = []
    for i in tqdm(arr):
        settitle(i,pas,title,id)
        # print("建立标签")
        ar = gettitleid(i, pas)
        for t in ar:
            if t['title']==title:
                userTempId.append(t["userTempId"])
                # print("获取标签id成功")
        imgid = getimgid(i, pas,getid)
        # print("获取imgid成功")
        for it in userTempId:
            setimg(i,pas,it,imgid)
        shur = len(arr)-1
        if shur<=0:
            return '完成'
            # print("关联图片成功")
def dells(user, pas,id):
    s = go.session()
    url = 'http://192.168.0.100:8088/dzkb0/home/deleteUserTemplet'
    cokk = getcook(user, pas)

    data = {
        'userTempId': id

    }
    tr = s.post(url, cookies=cokk, data=data, verify=False)
    # return tr.text

def dellist(arr,pas,title):
    userTempId=[]
    for i in tqdm(arr):
        ar = gettitleid(i, pas)
        for t in ar:
            if t['title'] == title:
                userTempId.append(t["userTempId"])
                # print("获取标签id成功")
        for it in userTempId:
            dells(i, pas,it)
            # print("删除任务")
        shur = len(arr) - 1
        if shur <= 0:
            return '完成'
    pass

def main():
    while 1:
        # 用户
        arr=['9001','010','011','012','013','014','015','052','070','10','1006','1006s','1006t','1007','1007b','101','102','102ledl','102ledt','102t','108611','120','121','122','123','124','125','126','127','128','129','501','502','503','504','ja01','pub-1','shitang']
        # 密码
        # arr = ['admin']
        pas = "123456"
        print('1.穿件和添加图片到栏目\n2.删除已建立栏目\n3.输入exit退出')
        code = input("输入功能号码：")
        # 标题
        # title="人人为大家 大家为人人                   "

        if code=='exit':
            exit()

        # 标题id
        userTempId = []


        if code == '1':
            print("--------开始任务--------\n")
            title = input("请输入标题：\n")
            id = input("请输入ID：\n")
            imgid = input("图片id：\n")
            print(addwoke(arr,pas,title,id,imgid))

        # 删除任务
        if code == '2':

            print("------------开始删除任务---------\n")
            title = input("请输入标题：\n")
            print(dellist(arr,pas,title))
        # print(imgid)

if __name__ =="__main__":
    # 建立任务
    main()