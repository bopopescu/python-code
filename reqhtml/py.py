#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-17 10:27
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : py.py
import threading
import requests
import datetime
import time
'''
@THREAD_NUM :线程数
@ONE_WORKER_NUM :每个线程循环数
'''

THREAD_NUM = 2000
ONE_WORKER_NUM = 1
SUMTIME = 0.00
SUCCESSCOUNT = 0
def getdatar(url):
    # url = 'http://wxbt.jcms.top:8080/hongbao'
    # url = 'http://10.168.5.120:8500'
    headers = {

    'Content-Type':'text/html;charset=utf-8',

    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',

    }

    return requests.post(url, headers=headers)
def test(url):
    global a
    global SUMTIME
    global SUCCESSCOUNT
    global SUCCESSCOUNT
    response = getdatar(url)
    res_time = response.elapsed.microseconds/1000000
    c = response.status_code
    if c!=200:
        f=open("a.txt","a+")
        f.write(str(c))
    print(response.status_code)

    # print(datetime.datetime.now(),"—",response.text)
    print(1)
    SUMTIME = SUMTIME + res_time
    SUCCESSCOUNT = SUCCESSCOUNT + 1
url='http://10.168.5.164:8006/6A2255C958C2C155'
def working():
    global ONE_WORKER_NUM
    for i in range(0,ONE_WORKER_NUM):

        test(url)

def t():
    global THREAD_NUM
    Threads = []
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working,name='T'+str(i))
        t.setDaemon(True)
        Threads.append(t)
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()

if __name__ == '__main__':
    t()
    # print(a)
    print('并发数：' + str(THREAD_NUM * ONE_WORKER_NUM))
    print('成功数：' + str(SUCCESSCOUNT))
    print('成功率：' + str(SUCCESSCOUNT / (THREAD_NUM * ONE_WORKER_NUM) * 100) + '%')
    print('成功请求总响应时间：' + str(SUMTIME))
    (lambda x=SUMTIME, y=SUCCESSCOUNT: print('成功订单平均响应时间：' + str(x / y)) if y != 0 else print('成功数为0'))()
    (lambda x=SUMTIME, y=SUCCESSCOUNT: print('TPS：' + str(y / (x / y))) if x != 0 and y != 0 else print('成功数或响应时间为0'))()
