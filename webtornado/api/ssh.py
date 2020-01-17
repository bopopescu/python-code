#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-02 10:54
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : ssh.py
import paramiko
import time
class ssh(object):
    def __init__(self, ip,name,passw):
        self.host = ip
        self.username = name
        self.pwd = passw
        self.__k = None
        print(self.host, self.username, self.pwd)
    def SSHrun(self,cmd):
        # 实例化SSHClient
            client = paramiko.SSHClient()
            # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # 连接SSH服务端，以用户名和密码进行认证
            client.connect(hostname=self.host, port=22, username=self.username, password=self.pwd)
            channel = client.invoke_shell()  # 变成交互性终端
        # 打开一个Channel并执行命令
        # stdin, stdout, stderr = client.exec_command(cmd)  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值

            channel.send(cmd + "\n")  #加\n代表回车执行命令
            time.sleep(1)  #执行命令后结果返回可能有延迟，为了保证结果都到缓冲区，最好暂停一下
            buf = channel.recv(10024).decode("utf-8")
            print(buf)
            # 打印执行结果
            return str(buf)

# import paramiko
# import time
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='192.168.0.21', port=22, username='root', password='jinjin')
# channel = ssh.invoke_shell()  #变成交互性终端
#
# while 1:
#     command = input(">>")
#     channel.send(command + "\n")  #加\n代表回车执行命令
#     time.sleep(1)  #执行命令后结果返回可能有延迟，为了保证结果都到缓冲区，最好暂停一下
#     buf = channel.recv(10024).decode("utf-8")
#     print(buf)