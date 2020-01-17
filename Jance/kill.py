#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-20 13:14
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : kill.py


import os
import signal

def kill_process(pid):
    try:
        a = os.kill(pid, signal.SIGKILL)

        print('已杀死pid为%s的进程,　返回值是:%s' % (pid, a))
    except IOError:
        print(2)


def get_pid(port):
    try:
        vv = os.popen("netstat -nlp | grep :%s | awk '{print $7}' | awk -F\" / \" '{ print $1 }'" % (port)).read().split('/')[0]
    except IOError:
        print(2)
    # print(vv)
    print(vv)


def run_program(jar_name):
    os.system("nohup java -jar" + jar_name + "&")
    print("正在启动：%s"%(jar_name))


def main():
    portSet = set()
    portSet.add("8080")
    programSet = set()
    programSet.add("xspch.jar")
    for port in portSet:
        try:
            # kill_process(get_pid(port))
            get_pid(port)
        except IOError:
            print(2)

    # for program in programSet:
        # print(1)
        # run_program(program)
#

main()
