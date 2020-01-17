#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-10 10:41
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : dui.py
from multiprocessing import Queue
# 调用队列类，实例化队列对象
# def duilei(shu,arr):
#
#     q = Queue(int(shu))# 队列中存放5个数据
#
#     # put添加数据，若队列里的数据满了就会卡住
#     if int(shu)>0:
#         for i in range(int(shu)):
#             if q.full():
#                 break
#             else:
#                 q.put(arr)
#
#         # 查看队列是否满了
#     # 添加数据, 若队列满了也会报错
#     # q.get() 获取的数据遵循先进先出
#     arr1=[]
#     for i in range(int(shu)):
#         arr1.append(str(q.get()))
#
#     print(arr1)
# def run(arr):
#     duilei(5,arr)
#
#
#
# from multiprocessing import Process
# for i in range(10): # 模拟10个用户抢票
#     run(i)
# from multiprocessing import Process, Queue
#
#
# def task1(q,data):
#     q.put(data)
#     print('进程1添加数据到队列')
#
#
# def task2(q):
#     print(q.get())
#     print('进程2从队列中获取数据')
#
#
# if __name__ == '__main__':
#     q = Queue(1)
#     p1 = Process(target=task1, args=(q,i))
#     p2 = Process(target=task2, args=(q,))
#     p1.start()
#     p2.start()
#     print('主进程')
import json
import time
from multiprocessing import Process, Lock
def search(user):
    with open('data.json', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    print(f'用户{user}查看余票，还剩{dic.get("ticket_num")}...')


def buy(user):
    with open('data.json', 'r', encoding='utf-8') as f:
        dic = json.load(f)

    time.sleep(0.2)
    if dic['ticket_num'] > 0:
        dic['ticket_num'] -= 1
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print(f'用户{user}抢票成功!')
        # 加入购物车
        return 1

    else:
        return 0


def run(user, mutex):
    search(user)
    mutex.acquire()  # 加锁
    r = buy(user)
    mutex.release()  # 释放锁
    return r


def rundui(id):
    mutex = Lock()
    return run(id,mutex)
    # for i in range(10):  # 模拟10个用户抢票
    #         p = Process(target=run, args=(f'用户{i}', mutex))
    #         p.start()
t = rundui(3)
if t>0:
    print("ok")