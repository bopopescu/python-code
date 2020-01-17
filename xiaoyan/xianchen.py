#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-25 11:04
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : xianchen.py
import threading
import os
import time

class demo():
    def __init__(self,d):
        self.dic = d


    def check_ticket(self):
        print('剩余【%s】票' % self.dic['ticket'])
    def deal_ticket(self):
        if self.dic['ticket'] > 0:
            self.dic['ticket'] -= 1
            print('%s购票成功' % os.getpid())
        else:
            print('%s购票失败' % os.getpid())
    def buy_ticket(self,):
        time.sleep(2)
        locks.acquire()
        self.check_ticket()
        self.deal_ticket()
        locks.release()



if __name__ == '__main__':
    locks = threading.Lock()
    d = demo({'ticket': 5})
    for i in range(10):
        t = threading.Thread(target=d.buy_ticket,)

        t.start()

