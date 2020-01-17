#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-17 9:23
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : ssh.py
import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host=input("host:")
user=input("user:")
pas=input("password:")
ssh.connect(hostname=host, port=22, username=user, password=pas)
channel = ssh.invoke_shell()  #变成交互性终端

while 1:
    command = input(">>")
    channel.send(command + "\n")  #加\n代表回车执行命令
    time.sleep(1)  #执行命令后结果返回可能有延迟，为了保证结果都到缓冲区，最好暂停一下
    buf = channel.recv(10024).decode("utf-8")
    print(buf)